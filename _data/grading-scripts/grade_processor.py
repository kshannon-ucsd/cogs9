import pandas as pd
import numpy as np
import yaml
import warnings
import os
import argparse
from pandas.errors import SettingWithCopyWarning

warnings.simplefilter("ignore", SettingWithCopyWarning)
warnings.simplefilter("ignore", FutureWarning)

# Loading configuration from a YAML file
def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

# Convert % to letter grade
def to_letter(percentage, grade_cutoffs):
    for grade, cutoff in grade_cutoffs.items():
        if percentage >= cutoff:
            return grade
    return "F"

# Determine file type and read accordingly
def read_file(file_path):
    """Read a file as either CSV or Excel based on extension"""
    _, ext = os.path.splitext(file_path)
    if ext.lower() == '.csv':
        return pd.read_csv(file_path)
    elif ext.lower() in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def save_file(df, file_path):
    """Save dataframe to file based on extension"""
    _, ext = os.path.splitext(file_path)
    if ext.lower() == '.csv':
        df.to_csv(file_path, index=False)
    elif ext.lower() in ['.xlsx', '.xls']:
        df.to_excel(file_path, index=False)
    else:
        raise ValueError(f"Unsupported output format: {ext}")

def create_master(config, gradescope_df):
    """Create master grades file from gradescope data"""
    print("Creating master grade file...")
    
    # Create mappings
    master_to_gradescope_map = {k: v for k, v in config['column_mappings'].items()}
    gradescope_to_master_map = {v: k for k, v in config['column_mappings'].items()}
    
    # Initialize master DataFrame
    master = pd.DataFrame()
    
    # Handle the Name column special case
    if 'NAME' in master_to_gradescope_map and master_to_gradescope_map['NAME'] == 'Name':
        # Check if 'Name' exists in gradescope
        if 'Name' in gradescope_df.columns:
            master['NAME'] = gradescope_df['Name'].copy()
        # If not, try to create it from First Name and Last Name
        elif 'First Name' in gradescope_df.columns and 'Last Name' in gradescope_df.columns:
            master['NAME'] = gradescope_df['Last Name'] + ', ' + gradescope_df['First Name']
            # Add 'Name' to gradescope for later processing
            gradescope_df['Name'] = master['NAME']
            print("Created 'Name' column from 'First Name' and 'Last Name'")
        else:
            raise KeyError("Cannot find 'Name' or 'First Name'/'Last Name' columns in gradescope file")
    
    # Process the rest of the columns
    for key, val in master_to_gradescope_map.items():
        if key == 'NAME' and val == 'Name':
            # Already handled above
            continue
            
        if val not in gradescope_df.columns:
            print(f"Warning: Column '{val}' not found in gradescope file")
            master[key] = np.nan
        else:
            master[key] = np.nan_to_num(gradescope_df[val].copy())
    
    # Calculate raw points
    master["RAW_POINTS"] = sum(
        master[val] for key, val in gradescope_to_master_map.items() 
        if key not in config['excluded_columns']
        and val in master.columns  # Only include columns that exist
    )
    
    # Calculate lateness deductions
    max_avail_pts = 0
    for key, val in gradescope_to_master_map.items():
        if key in config['excluded_columns'] or val not in master.columns:
            continue
            
        lateness_col = key + " - Lateness (H:M:S)"
        max_points_col = key + " - Max Points"
        
        if lateness_col not in gradescope_df.columns:
            print(f"Warning: Lateness column '{lateness_col}' not found")
            master[val + "-D"] = 0
            continue
            
        if max_points_col not in gradescope_df.columns:
            print(f"Warning: Max points column '{max_points_col}' not found")
            master[val + "-D"] = 0
            continue
        
        # Convert lateness to hours
        hours = gradescope_df[lateness_col].copy()
        if hours.dtype == object:  # String format
            hours = hours.map(
                lambda el: int(str(el).split(":")[0]) if pd.notna(el) else 0
            )
        
        master[val + "-D"] = 0
        
        if key in config['penalties']:
            small_penalty, large_penalty = config['penalties'][key]
            lateness_threshold = config['lateness'].get(key, 0)
            
            # Apply penalties
            master.loc[(hours > 0) & (hours < lateness_threshold), val + "-D"] = (
                small_penalty * gradescope_df[max_points_col]
            )
            master.loc[hours >= lateness_threshold, val + "-D"] = (
                large_penalty * gradescope_df[max_points_col]
            )
        
        max_avail_pts += gradescope_df[max_points_col].iloc[0] if len(gradescope_df) > 0 else 0
    
    master["DEDUCTIONS"] = sum(
        master[val + "-D"] 
        for key, val in gradescope_to_master_map.items() 
        if key not in config['excluded_columns']
        and val in master.columns
        and val + "-D" in master.columns
    )
    
    # Calculate adjusted points
    for key, val in gradescope_to_master_map.items():
        if key in config['excluded_columns'] or val not in master.columns:
            continue
        if val + "-D" not in master.columns:
            master[val + "- Adj"] = master[val]
        else:
            master[val + "- Adj"] = master[val] - master[val + "-D"]
    
    master["ADJ_POINTS"] = sum(
        master[val + "- Adj"] 
        for key, val in gradescope_to_master_map.items() 
        if key not in config['excluded_columns']
        and val in master.columns
        and val + "- Adj" in master.columns
    )
    
    # Calculate category scores
    reading_cols = [col for col in master.columns if col.startswith('R') and col.endswith('- Adj')]
    assignment_cols = [col for col in master.columns if col.startswith('A') and col.endswith('- Adj')]
    
    # Grading distribution (200 total points)
    # 3 Assignments: 30% (60 points, 20 each)
    # 5 Reading Quizzes (lowest quiz score dropped): 20% (40 points, 10 each)
    # Final Project pt. 1: 10% (20 points)
    # Final Project pt. 2: 20% (40 points)
    # Final Project video: 20% (40 points)
    
    # Print what categories were found
    print(f"Found {len(reading_cols)} reading quizzes: {reading_cols}")
    print(f"Found {len(assignment_cols)} assignments: {assignment_cols}")
    
    # Final Project components
    final_project_components = {}
    if "F1- Adj" in master.columns:
        final_project_components["FINAL P1"] = "F1- Adj"
        master["FINAL P1"] = master["F1- Adj"]
    else:
        print("Warning: Final Project part 1 not found")
        master["FINAL P1"] = 0
        
    if "F2- Adj" in master.columns:
        final_project_components["FINAL P2"] = "F2- Adj"
        # Final Project Part 2 includes video component (40% total - 20% for Part 2 + 20% for video)
        # This means Part 2 is worth 80 points out of 200 total
        master["FINAL P2"] = master["F2- Adj"]
        print("Using Final Project Part 2 score (includes video component)")
    else:
        print("Warning: Final Project part 2 not found")
        master["FINAL P2"] = 0
    
    # Calculate component scores
    
    # Readings (drop lowest score if we have more than one)
    if len(reading_cols) > 0:
        if len(reading_cols) > 1:
            # Drop lowest reading quiz
            print(f"Dropping lowest score from {len(reading_cols)} reading quizzes")
            master["READINGS_RAW"] = (
                master[reading_cols].sum(axis=1) -
                master[reading_cols].min(axis=1)
            )
            # Scale to 40 points (4 out of 5 quizzes at 10 points each)
            master["READINGS"] = master["READINGS_RAW"]
        else:
            # If only one reading, just use it directly
            master["READINGS_RAW"] = master[reading_cols].sum(axis=1)
            master["READINGS"] = master["READINGS_RAW"]
    else:
        master["READINGS_RAW"] = 0
        master["READINGS"] = 0
    
    # Assignments (scale to 60 points total)
    if len(assignment_cols) > 0:
        # Create a copy of the assignments dataframe for scaling
        assignments_df = master[assignment_cols].copy()
        
        # Scale Assignment 2 and 3 if they're out of 40 points
        if 'A2- Adj' in assignments_df.columns:
            # Check if A2 is out of 40 points in gradescope
            a2_max_col = "Assignment 2 - Max Points"
            if a2_max_col in gradescope_df.columns and gradescope_df[a2_max_col].iloc[0] == 40:
                print("Scaling Assignment 2 from 40 points to 20 points")
                assignments_df['A2- Adj'] = assignments_df['A2- Adj'] / 2
                
        if 'A3- Adj' in assignments_df.columns:
            # Check if A3 is out of 40 points in gradescope
            a3_max_col = "Assignment 3 - Max Points"
            if a3_max_col in gradescope_df.columns and gradescope_df[a3_max_col].iloc[0] == 40:
                print("Scaling Assignment 3 from 40 points to 20 points")
                assignments_df['A3- Adj'] = assignments_df['A3- Adj'] / 2
        
        master["ASSIGNMENTS_RAW"] = assignments_df.sum(axis=1)
        # Each assignment is worth 20 points (60 points total for 3 assignments)
        master["ASSIGNMENTS"] = master["ASSIGNMENTS_RAW"]
    else:
        master["ASSIGNMENTS_RAW"] = 0
        master["ASSIGNMENTS"] = 0
    
    # Calculate weighted total based on the grading distribution
    # Using raw scores and scaling them to the appropriate weight
    master["TOTAL_POINTS"] = (
        master["READINGS"] +  # 20% - 40 points
        master["ASSIGNMENTS"] +  # 30% - 60 points
        master["FINAL P1"] +  # 10% - 20 points
        master["FINAL P2"]  # 40% - 80 points (includes 20% for Part 2 and 20% for video)
    )
    
    # Set maximum possible points (200 total)
    master["MAX_POINTS"] = 200.0
    
    # Calculate draft letter grade
    master["DRAFT_PERCENTAGE"] = (master["TOTAL_POINTS"] / master["MAX_POINTS"] * 100).round(2)
    master['DRAFT_GRADE'] = master['DRAFT_PERCENTAGE'].apply(lambda x: to_letter(x, config['grade_cutoffs']))
    
    # Adjustments and final grades 
    master["CAPES_CREDIT"] = None
    master["EC_MID_EVAL"] = None
    master["ADJUSTMENTS"] = None
    master["FINAL_POINTS"] = None
    master["FINAL_PERCENTAGE"] = None
    master["LETTER_GRADE"] = master['DRAFT_GRADE']
    master["NOTES"] = None
    
    # Sort values
    if 'PID' in master.columns:
        master = master.sort_values('PID', ascending=True)
        
    return master

def create_egrades(master_df, canvas_df):
    """Create egrades file from master and canvas data"""
    print("Creating egrades file...")
    
    # Create egrades DataFrame
    egrades = pd.DataFrame()
    egrades["Last Name"] = canvas_df["Last Name"].copy()
    egrades["First Name"] = canvas_df["First Name"].copy()
    egrades["Student ID"] = canvas_df["Student ID"].copy()
    egrades["SectionId"] = canvas_df["Section ID"].copy()
    
    # Merge with master file to get letter grades
    if 'PID' in master_df.columns and 'LETTER_GRADE' in master_df.columns:
        egrades = (
            egrades.merge(
                master_df[['PID', 'LETTER_GRADE']],
                left_on='Student ID',
                right_on='PID',
                how='left'
            )
            .drop(columns=['PID'])
            .rename(columns={
                'LETTER_GRADE': 'Final_Assigned_Egrade'
            })
            .sort_values('Student ID')
        )
    else:
        print("Warning: Required columns for egrades not found in master dataframe")
        egrades["Final_Assigned_Egrade"] = None
    
    # Replace NaN with None for cleaner output
    egrades['Final_Assigned_Egrade'] = egrades['Final_Assigned_Egrade'].replace({np.nan: None})
    
    return egrades

def process_grades(config_path='config.yaml', output_master=True, output_egrades=True):
    """Main function to process grades"""
    try:
        # Load configuration
        config = load_config(config_path)
        print(f"Loaded configuration from {config_path}")
        
        # Get file paths
        canvas_path = config['files']['canvas']
        gradescope_path = config['files']['gradescope']
        
        # Check if files exist
        if not os.path.exists(canvas_path):
            raise FileNotFoundError(f"Canvas file not found: {canvas_path}")
        if not os.path.exists(gradescope_path):
            raise FileNotFoundError(f"Gradescope file not found: {gradescope_path}")
        
        # Load data files
        canvas_df = read_file(canvas_path)
        gradescope_df = read_file(gradescope_path)
        
        print(f"Loaded canvas file: {canvas_path} with {len(canvas_df)} rows")
        print(f"Loaded gradescope file: {gradescope_path} with {len(gradescope_df)} rows")
        
        # Process master grades
        master_df = create_master(config, gradescope_df)
        
        # Save master file if requested
        if output_master:
            output_path = config['files']['output']
            save_file(master_df, output_path)
            print(f"Saved master file to {output_path}")
        
        # Process egrades
        if output_egrades:
            egrades_df = create_egrades(master_df, canvas_df)
            
            # Save egrades
            egrades_path = "egrades.csv"
            save_file(egrades_df, egrades_path)
            print(f"Saved egrades file to {egrades_path}")
            
            return master_df, egrades_df
        
        return master_df, None
        
    except Exception as e:
        print(f"Error processing grades: {str(e)}")
        raise

def main():
    """Command-line entry point"""
    parser = argparse.ArgumentParser(description='Process grades from Gradescope and Canvas')
    parser.add_argument('--config', default='config.yaml', help='Path to config file')
    parser.add_argument('--master-only', action='store_true', help='Only output master file')
    parser.add_argument('--egrades-only', action='store_true', help='Only output egrades file')
    parser.add_argument('--test', action='store_true', help='Use test files (gradescope-test.csv and canvas-test.csv)')
    
    args = parser.parse_args()
    
    # Load config
    config = load_config(args.config)
    
    # Override with test files if requested
    if args.test:
        config['files']['gradescope'] = 'gradescope-test.csv'
        config['files']['canvas'] = 'canvas-test.csv'
        config['files']['output'] = 'master-test.csv'
        print(f"Using test files: {config['files']['gradescope']} and {config['files']['canvas']}")
    
    output_master = not args.egrades_only
    output_egrades = not args.master_only
    
    try:
        process_grades(
            config_path=args.config,
            output_master=output_master,
            output_egrades=output_egrades
        )
        print("Grade processing completed successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    main()