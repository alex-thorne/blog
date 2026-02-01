# Personal Blog Site

A personal blog site for sharing projects, blogs, and links to various other communities, platforms, or ideas I'm interested in.

## Running locally
1. Clone repository
3. Run `bundle install` [^1] from project root (where `_config` is located.)
4. Run `bundle exec jekyll serve`
5. Open <http://localhost:4000/>

## Dependencies 
- ruby
    - currently built using 3.3.3 (suggest managing via asdf)
- Bundler. Install with `gem install bundler`.

## Tools
- The site is presented as a [Jekyll](https://jekyllrb.com/) site
- It's using the [hydejack](https://github.com/hydecorp/hydejack) theme

## CI/CD Pipeline

The repository includes an automated CI/CD pipeline that:
- **Builds** the Jekyll site on every push and pull request
- **Runs E2E visual tests** to capture screenshots of key pages
- **Deploys** to GitHub Pages (on `main` branch only)

### Visual Snapshot Testing

The CI pipeline includes end-to-end visual testing using [Playwright](https://playwright.dev/). For every build:
1. The site is served locally in the CI environment
2. Visual snapshots are captured for:
   - Homepage
   - Blog page
3. Screenshots are uploaded as artifacts with 30-day retention

**Viewing snapshots in PRs:**
- Navigate to the "Actions" tab in the PR
- Find the workflow run for your commit
- Download the `visual-snapshots` artifact to view the screenshots

This provides immediate visual confidence during code review that the site builds correctly and looks as expected.

