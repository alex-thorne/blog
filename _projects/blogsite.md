---
layout: project
title: 'blog site'
caption: A personal blog site to showcase projects
description: >
  This project is this site itself. It's a simple blog site which will serve as a platform for documenting my journey through various projects. The development, deployment and hosting of the blog site is the "project" that it documented here. 
date: '14-07-2024'
accent_color: '#4fb1ba'
# accent_image:
#   background: '#ffffff'
#   theme_color: '#ffffff'
image: 
  path: /assets/img/projects/blogsite.jpg
  srcset: 
    1920w: /assets/img/projects/blogsite.jpg
    960w:  /assets/img/projects/blogsite@0,5x.jpg
    480w:  /assets/img/projects/blogsite@0,25x.jpg
links:
  - title: GitHub Link 
    url: https://github.com/alex-thorne/blog
sitemap: false
---


# Blog Site

I wanted to put up a site to host a resume and share some other content. I also knew I'd rather move to other more intereting projects than spend too much time on the site itself. I had some exposure to using Jekyll sites from collaborating with my brother, Erik, and friends on our indie-community-radio station, [The Pork Chop Express](http://porkchopexpress.live/). I especially liked the simplicity of building a Jekyll site with [GitHub Actions](https://jekyllrb.com/docs/continuous-integration/github-actions/) and hosting it via [GitHub Pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll). I found a nice theme I liked in [Hydejack](https://hydejack.com/), a fork of the popular [Hyde](https://jekyllthemes.io/theme/hyde) theme. I like HydeJack's support for [JSON resume](https://jsonresume.org/), dark theme support, and several other features. 

## Process

### Getting Started with Jekyll
I struggled with some dependencies issues with Jekyll. Especially when moving between development on my [WSL2]{:.heading.flip-title} development environment on my main home PC and my M1 Silicon MacBook Pro. After a little bit of time I did get Jekyll working with Ruby v. 3.3.3. The more interesting result was that this caused experience caused me to look for a version manager for switching between versions of Ruby. I chose to go with [`asdf`](https://github.com/asdf-vm/asdf), using the [`asdf-ruby`](https://github.com/asdf-vm/asdf-ruby?tab=readme-ov-file) plugin rather than the several alternatives, chruby, rbenv or rvm. I primarily chose asdf for its reusability as it supports many languages and tools with its existing [plugins](https://github.com/asdf-vm/asdf-plugins). 

Jekyll itself is extremely easy once you get your development environment set up for it. 

Summed up, my setup looked something like this:

(_from root dir of jekyll site content, where _config is located_)

  ```bash
  brew install coreutils curl git\
  git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.0\
  echo -e "\n. $(brew --prefix asdf)/libexec/asdf.sh" >> ${ZDOTDIR:-~}/.zshrc\
  asdf plugin-add ruby
  asdf install ruby 3.3.3
  asdf local ruby 3.3.3
  bundle install
  bundle exec jekyll build
  bundle exec jekyll serve
  ```

### Site Content

Getting the site content filled in is, of course, the lion's share of the work here. As far as structure goes, I won't describe it here, as it's covered in Jekyll documentation and the specifics of the Hyde & HydeJack's themes. I ended up spending a bit of time using some AI powered tools to prepare graphic design related content for the site, e.g. background removal for headshots, resizing of images for logos/favicon. For these purposes, those tools worked amazingly well; just a shame really that kids these days will never get to experience the patience-training tedium of isolating content with the pen tool in Photoshop. 

### Domain Registry

This is extremely simple. Still, I'd never done it before for lack of any need. I spent more time searching for which domain registrar to choose. I landed on one, and from there it's a very [simple task](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain) to set up DNS to point the GitHub Pages site to my new registered domain.

### Delivery

Jeykll plays very well with GitHub Pages, and they both play well together with GitHub Actions, so this project was a very accesible initial exploration of GitHub Actions. I played around with several approaches, I wanted to find a way to set up a simple continuous integration and deployment approach. "Staging" with GitHub pages is a little tricky, I played around with some options of fully deploying the site in a "staging" approach. I did find one interesting workflow, [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages) that adds support for publishing to an external repository. I decided however that building and viewing the Jekyll site locally is plenty for this purpose. 

As of writing, the workflow I'm using is a slightly modified version of th suggested [Jekyll workflow](https://github.com/alex-thorne/blog/commit/7dbb6ba785f38f1d2b825f59c9a98ccc15860bc4https://github.com/actions/starter-workflows/blob/main/pages/jekyll.yml). I adjusted the workflow to trigger the build job on both on push _and_ merge to `main` and `develop` branch, but only deploy when run on triggers for `main`. Then set branch rules to require successful build checks for those two branche from the action, and set up the settings for GitHub Pages to use GitHub Actions as its source, and tada, CI/CD. Neat.

```yaml
name: Deploy Jekyll site to Pages
on:
  push:
    branches: [main, develop]
  pull_request:
    types: [opened, synchronize, reopened]
    branches: [main, develop]

    # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
# However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  # Build job
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Ruby
        uses: ruby/setup-ruby@086ffb1a2090c870a3f881cc91ea83aa4243d408 # v1.195.0
        with:
          ruby-version: '3.2.2' # Not needed with a .ruby-version file
          bundler-cache: true # runs 'bundle install' and caches installed gems automatically
          cache-version: 0 # Increment this number if you need to re-download cached gems
      
      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5
      
      - name: Build with Jekyll
        # Outputs to the './_site' directory by default
        run: bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"
        env:
          JEKYLL_ENV: production
          PAGES_REPO_NWO: alex-thorne/blog

      - name: Upload artifact
        # Automatically uploads an artifact from the './_site' directory by default
        uses: actions/upload-pages-artifact@v3

  # Deployment job
  deploy:
    if: github.ref == 'refs/heads/main'
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

my slightly modified jekyll github actions workflow
{:.figcaption}

## Take-away

learnings:

- finding asdf for version management
- low-cost of entry initial experience with GitHub Actions
- Forced to use some AI tools (Canva, ChatGPT-based Image Generator for site graphic assets (icons, headshots, logo))
- finding the JSON Resume format
- Having to think closely about sensitive content control if maintaining this project as a public repository

### Project Details
- Date started: 14-07-2024

[WSL2]: WSL2.md