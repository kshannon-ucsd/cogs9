[![Deploy Jekyll site to Pages](https://github.com/kshannon-ucsd/cogs9/actions/workflows/jekyll.yml/badge.svg)](https://github.com/kshannon-ucsd/dsc40a/actions/workflows/jekyll.yml)

# ucsd-cogs9
Class Website for UCSD's COGS 9 Introduction to Data Science

## Up and Running
### Dev Environment initial set up
#### If building from scratch
1. Install chruby and ruby-install with Homebrew (install ruby 3.1.2)
2. cd to project dir and chruby for ruby-3.1.2 #this should be default from the `.ruby-version` file going forward.
3. `bundle init` to create gemfile
4. Set up gems to be installed locally in project dir: `bundle config set --local path 'vendor/bundle'` This creates a `.bundle` file
5. Install Jekyll 4.2: `bundle add jekyll` At this time (9/5/2022) 4.2 auto installs
6. Create jekyll scaffold: `bundle exec jekyll new --force --skip-bundle .` `bundle install`
7. `bundle add webrick`
8. Give it a test run by following the local dev build instructions below!

#### Using devcontainer
1. Install the Remote - Containers extension in VSCode
2. Open the project in VSCode
3. Click on the green icon in the bottom left corner of the window and select "Reopen in Container"
4. This will build the container and open the project in a containerized environment with all the necessary dependencies installed.

### Building for Local
All dev builds will be built into a `dev-docs/` dir. This dir is included in `.gitignore` and is only used for development builds. Any specific dev config should bd included in the `_config_dev.yml` file. Your absolute path to `dev-docs` will be different.
1. `bundle exec jekyll serve --config _config.yml,_config_dev.yml --destination ./dev-docs` #builds and starts local server on localhost
2. navigate to http://localhost:4000/cogs9/

### Building for Prod
1. A merge or direct push to main branch will automatically trigger the jekyll workflow which will build and deploy the main branch to production.
2. Check status in github actions for build results.
3. Navigate to https://kshannon-ucsd.github.io/cogs9/

### /data/ directory
This dir is excluded from the jekyll build chain (excluded in the config.yaml file).
Set this up correctly fopr the next iteration:
`Change this to choose where to pick data from`
`data_folder: su24` becomes e.g. wi25

This folder includes data that changes from quarter to quarter, e.g. course calender. I don't want to recreate these data, so I dump them here to use for later. Eventually I would like to create variables to pull this data, but for now this is a fine solution.

## Course Calendar
The following tags can be applied within a row for each course activity, set within the `_data/term/course_calendar.csv` file.
  - LECT --> lecture
  - DEMO --> in-class demo
  - CNCL --> no class, or canceled class
  - ASSG --> assignment due date
  - EXAM --> exam due date
  - GRPW --> groupwork
  - PRAC --> practice problems

 Any other tag used will default to a black colored tag

