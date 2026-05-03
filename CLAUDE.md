# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Site overview

Personal blog at `alexthorne.site`, built with Jekyll 3.10 (`gem "jekyll", "~> 3.10"`) using the **Hydejack** theme. The theme is consumed as the `github-pages` gem (not as a remote_theme — both `theme:` and `remote_theme:` are commented out in `_config.yml`), which constrains us to GitHub-Pages-compatible plugins only. Output is deployed to GitHub Pages from `main` via `.github/workflows/jekyll.yml`.

## Local dev

Ruby is managed with **asdf**. The pinned version is `3.3.3` (see `.tool-versions`). Bundler version is locked to `2.5.11` by `Gemfile.lock`'s `BUNDLED WITH`.

```bash
bundle install              # first time / after Gemfile changes
bundle exec jekyll serve    # http://localhost:4000, with live reload
bundle exec jekyll build    # one-shot build into _site/
```

`hydejack.no_search: false` only enables search in `JEKYLL_ENV=production` builds — local serve intentionally skips it for build speed (see `_config.yml` `hydejack:` block, which also has `no_inline_css`, `no_page_style`, `use_lsi` flags that affect build time vs. fidelity).

## Content model

Three Jekyll collections plus posts, all surfaced via `permalink:` rewrites in `_config.yml`:

- **Blog posts** — `blog/_posts/YYYY-MM-DD-slug.md`, permalink `/blog/:categories/:year-:month-:day-:title/`. Front matter `date:` is **`'DD-MM-YYYY'`** (quoted, day-first) — this is a Hydejack convention and does not match the filename's `YYYY-MM-DD`. Filename order still drives chronology.
- **Projects** — `_projects/*.md`, permalink `/projects/:path/`, layout `project`.
- **Reading list** — `_reading-list/*.md`, permalink `/reading-list/:path/`.
- **Featured categories / tags** — `_featured_categories/*.md`, `_featured_tags/*.md`. These are landing pages for category/tag archives; configured as Jekyll collections with `seo.type: WebPage` so they aren't tagged as `BlogPosting`.

Pagination is 10 per page (`paginate: 10`, `paginate_path: /blog/:num/`). Use `jekyll-compose` (`bundle exec jekyll post "Title"`) to scaffold posts with the default front matter from `_config.yml`'s `jekyll_compose:` block.

## Assets

Post images live under `assets/img/blog/<topic>/`. The Hydejack image front matter expects a `srcset` map (1920w/960w/480w/240w). Use `scripts/imageresize.py <file>` (Pillow) to generate the 50/25/12.5% variants Hydejack expects — it writes `name@0,5x.ext` etc. alongside the original.

### Header image specs (Hydejack Pro 9.1.6)

Author the master at **1920×1080 JPEG, 16:9**, then export 960×540 and 480×270 variants. Theme docs (`docs/basics.md:38-40`) prescribe the ImageMagick recipe:

```
-sampling-factor 4:2:0 -strip -quality 85 -interlace JPEG -colorspace RGB
```

i.e. q85, progressive/interlaced, 4:2:0 chroma subsampling, sRGB, metadata stripped. PNG is only for UI screenshots/diagrams, not header images. The reference `hydejack-9.jpg` and other bundled samples ship at 1920×1080 — some use 16:10 or 3:2 but 16:9 is the recommended default.

Wire up the variants in front matter:

```yaml
image:
  path:    /assets/img/blog/your-post.jpg          # 1920×1080 (fallback + social preview)
  srcset:
    1920w: /assets/img/blog/your-post.jpg          # 1920×1080
    960w:  /assets/img/blog/your-post@0,5x.jpg     #  960×540
    480w:  /assets/img/blog/your-post@0,25x.jpg    #  480×270
```

`path` is the fallback for browsers without `srcset` support and the source for `jekyll-seo-tag` social previews — keep the full-res file there.

## CI/CD

`.github/workflows/jekyll.yml` runs on push and PR to `main` and `develop`:

1. **build** — `ruby/setup-ruby` with **Ruby 3.2.2** (note: diverges from local 3.3.3), `bundler-cache: true`, builds with `JEKYLL_ENV=production` and `--baseurl` from `actions/configure-pages`.
2. **e2e-test** — downloads the build artifact, serves it with `npx serve`, and runs Playwright snapshots of `/` and `/blog/` with `--update-snapshots` (so this generates baselines, not regressions — to enforce regressions, commit the snapshots and drop the flag).
3. **deploy** — only on `main`, uses `actions/deploy-pages@v4`.

`.github/workflows/merge-to-main.yml` opens an automated `develop → main` PR after checks pass on `develop`.

## Things that bite

- The `bundler-cache` step in CI keys on `Gemfile.lock`, so bumping gem versions locally requires committing the updated lockfile.
- `_config.yml` excludes `Gemfile`/`Gemfile.lock` from the build but **includes** `.well-known` and `LICENSE.md`.
- `optional_front_matter.remove_originals: true` and `readme_index.remove_originals: true` mean the source `README.md` and any frontmatter-less markdown get rewritten — be aware when adding root-level `.md` files.
- `relative_links.collections: true` means cross-collection links work with relative paths; absolute URLs aren't required.
