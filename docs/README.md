# ucsd-cogs9
Class Website for UCSD's Cogs 9 Introduction to Data Science


## Up and Running

### Dev Environment initial set up
1. Install chruby and ruby-install with Homebrew (install ruby 3.1.2)
2. cd to project dir and chruby for ruby-3.1.2
3. `bundle init` to create gemfile
4. Set up gems to be installed locally in project dir: `bundle config set --local path 'vendor/bundle'` This creates a `.bundle` file
5. Install Jekyll 4.2: `bundle add jekyll` At this time (9/5/2022) 4.2 auto installs
6. Create jekyll scaffold: `bundle exec jekyll new --force --skip-bundle .` `bundle install`
7. `bundle add webrick`
8. Give it a test run! `bundle exec jekyll serve`
