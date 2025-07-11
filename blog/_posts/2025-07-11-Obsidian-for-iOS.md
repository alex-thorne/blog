---
layout: post
title: 'Setting Up Obsidian for iOS'
caption: Free, app-less, iOS sync for Obsidian
description: >
  Setting up Obsidian to sync between PC and iOS devices as a GitHub repository
date: '11-07-2025'
accent_color: '#4fb1ba'
image: 
  path: /assets/img/blog/Obsidian/obsidian-git-ios.jpeg
  srcset: 
    1920w: /assets/img/blog/Obsidian/obsidian-git-ios.jpeg
    960w:  /assets/img/blog/Obsidian/obsidian-git-ios.jpeg
    480w:  /assets/img/blog/Obsidian/obsidian-git-ios.jpeg
    240w:  /assets/img/blog/Obsidian/obsidian-git-ios.jpeg
sitemap: false
categories: [Obsidian, writing]
tags: [Obsidian, writing]
---

More details on Obsidian and why I love this coming soon. For now, just a quick post to make sure these setup steps get captured, because I spent too long using too many misleading guides before I figured this out. 

## How to setup Obsidian to sync as GitHub repository including iOS device sync

1. Create repository on GitHub and initialize it with a README.md
2. Clone repo on desktop device using https and ghb private access token (must be classic token), e.g.: `https://ghp_<token>@github.com/<user-name>/<repo>.git`
	3. suggest making a test commit & push to remote to ensure it's working, then `git fetch` back to local on pc
3. Launch Obsidian app on desktop, open vault and select the git repository location
4. Enable community plugins, install Obsidian-git, enter author name name and author email (use the do-not-reply github email). 
5. Do a test `commit-and-sync` in the Obsidian-git panel to validate
6. Install Obsidian on iOS, create a new local vault. Vault name is unimportant, the purpose is to initialize the `On My iPhone/Obsidian/` directory in iOS Files.  
7. Copy the repository folder from desktop to iOS device to `On My iPhone/Obsidian/<repo>` (I created the initializing Obsidian vault with the same name, "notes", and used `replace` when copying there)
8. Launch iOS Obsidian app
9. Go to Setting > Community Plugins. Enable Community Plugins. Install Obsidian Git. 
10. Enter GitHub username & Personal Access Token (use the same one from step 2)
11. You should see status messages that your repo is synced
12. Navigate to your README.me, make a test edit and use the git panel (swipe left from right side of screen), make a test `commit-and-push`.

<br>

**and, VOILÀ, finally notes markdown notes with gruvbox theme synced across iPhone and my computers 🥹**

<div style="text-align: center;">
  <img src="/assets/img/blog/Obsidian/obsidian-ios-init-50.jpeg" alt="Obsidian iOS Setup" />
</div>