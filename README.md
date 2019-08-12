# Tuesmon blog

Tuesmon blog (https://blog.tuesmon.com/) made with Pelican (https://github.com/getpelican/pelican).

#### For developers:

- Install python dependencies:
  ```
  mkvirtualenv -p /usr/bin/python3 tuesmon-blog
  workon tuesmon-blog
  pip install -r requirements.txt
  ```

- Install SASS:
  ```
  gem install sass scss-lint
  export PATH="/usr/bin/core_perl:$(ruby -e "print Gem.user_dir")/bin:$PATH"
  ```
  
- Run in devel mode
  ```
  make compile_styles
  make devserver
  ```
