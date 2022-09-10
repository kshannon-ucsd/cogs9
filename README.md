# ucsd-cogs9
Class Website for UCSD's Cogs 9 Introduction to Data Science


## Up and Running
### Dev Environment initial set up
1. Install chruby and ruby-install with Homebrew (install ruby 3.1.2)
2. cd to project dir and chruby for ruby-3.1.2 #this should be default from the `.ruby-version` file going forward.
3. `bundle init` to create gemfile
4. Set up gems to be installed locally in project dir: `bundle config set --local path 'vendor/bundle'` This creates a `.bundle` file
5. Install Jekyll 4.2: `bundle add jekyll` At this time (9/5/2022) 4.2 auto installs
6. Create jekyll scaffold: `bundle exec jekyll new --force --skip-bundle .` `bundle install`
7. `bundle add webrick`
8. Give it a test run! `bundle exec jekyll serve`

### Building for Local
1. `bundle exec jekyll build --config _config.yml,_config_dev.yml`
2. navigate to http://localhost:4000/about/

### Building for Prod
1. checkout `main` and merge any changes
2. `bundle exec jekyll build` #this dumps the site into docs/ dir which GitHub looks for when building
3. commit new site in `docs/` to `main` then `push` to github #github looks for new pushes to main for auto deploying
4. Check status in github actions for build results.
5. Navigate to https://kshannon.github.io/ucsd-cogs9/