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

**How to set up an Obsidian to sync a vault with a GitHub repository on an iOS device.**

I read several guides on this which were ultimate more confusing than they need to be. So, here is my simplified guide. I hope it helps.

---
## 1. Create your vault's repository

1. Create a new GitHub repository.
2. Copy the repo URL — use the **HTTPS form**: `https://github.com/<user>/<repo>.git`
3.  Create a personal access token (GitHub user global settings > Developer Setting > Personal access tokens > Tokens (classic))
	1. Note: It **must** be a classic token. It will not work with the newer fine-grained token.
4. copy the PAT, e.g. `ghp_<your_36_digit_PAT>` 


---
## 4. iOS Setup

1. Install and launch the Obsidian app on iOS. Install must be done first as it initializes the Obsidian directory.
2. Close the Obsidian app
3. install **[iSH](https://ish.app/)** via iOS app store
4. Via `iSH` app, clone the repository in the Obsidian directory. You must use the `http` method for connecting to GitHub (not because it's not possible to set up ssh keys on iOS with iSH, but because the Obsidian git plugin does not support ssh.)

```bash
cd ~/Obsidian
git clone https://github.com/username/repo.git
```

When prompted for credentials, use your user name and the PAT you generated before:

```bash
git clone https://github.com/username/repo.git 
	Username: your_username
	Password: your_token
```


### iSH Setup

You will eventually need to use iSH for merge conflicts, etc. 
Use git's credential store to avoid having to enter the PAT token on password prompt:

```
# 1) Tell Git to use the store helper and where to keep the file
git config --global credential.helper "store --file ~/.config/git/credentials"

# 2) (Optional) pre-set your GitHub username to avoid extra prompts
git config --global credential.username YOUR_GITHUB_USERNAME

# 3) Create the credentials file with tight perms
mkdir -p ~/.config/git
touch ~/.config/git/credentials
chmod 600 ~/.config/git/credentials
```

Now do **one** HTTPS operation (e.g., `git fetch` or `git push`) and enter:

```
- Username: `YOUR_GITHUB_USERNAME`
- Password: `<your PAT>`
```

Git will write a line like this to `~/.config/git/credentials`:
```
`https://YOUR_GITHUB_USERNAME:PAT_HERE@github.com`
```

---

## 2. Desktop Setup

1. Clone the repository, use whichever authentication method you prefer (e.g. ssh)
2. Either add the whole `.obsidian/` directory to your `.gitignore` (*see below*) or at least ignore the content of the Obsidian git plugin if you're using it. It will mess up your iOS setup.

---

## Notes

-  If you are moving between multiple devices with different operating systems, especially if iOS is involved, I strongly suggest adding the entire `.obsidian/` directory to `.gitignore`. You'll need to manage your locally Obsidian configurations manually for each device, but that's not a lot of work. You will otherwise spend a bunch of time managing merge conflicts related to Obsidian files and plugins. 

```gitignore
.obsidian/core-plugins.json
```

## GPG + Obsidian Setup (macOS + iOS)

### Obsidian (gpgCrypt plugin)

To work with iOS, use **OpenPGP.js backend** setting in the gpgCrypt plugin settings. Generate keys with plugin, copy keys created in vault (e.g. `.keys/pub.asc`, `.keys/sec.asc`) to other devices.

Add keys, or `*.asc` to `.gitignore`

On desktop (e.g. macOS), configure **GnuPG CLI Wrapper backend** settings:
- Path: `/opt/homebrew/bin/gpg`
- Select your imported GPG key.

<br>

**and, VOILÀ, finally notes markdown notes with gruvbox theme synced across iPhone and my computers 🥹**

<div style="text-align: center;">
  <img src="/assets/img/blog/Obsidian/obsidian-ios-init-50.jpeg" alt="Obsidian iOS Setup" />
</div>

## The original post, an outdated guide
<details>
  <summary>Expand here for a much stranger way of doing this manually</summary>

This was the initial way I did this and I wrote down the steps. This is much too complicated, and makes no sense. I'm keeping the steps here for prosterity until I have time to fully validate my new guide on a clean installation.
  
### How to setup Obsidian to sync as GitHub repository including iOS device sync

1. Create repository on GitHub and initialize it with a README.md
2. Clone repo on desktop device using https and ghb private access token (must be classic token), e.g.: `https://ghp_<token>@github.com/<user-name>/<repo>.git`
   3. Suggest making a test commit & push to remote to ensure it's working, then `git fetch` back to local on PC
3. Launch Obsidian app on desktop, open vault and select the git repository location
4. Enable community plugins, install Obsidian-git, enter author name and author email (use the do-not-reply GitHub email)
5. Do a test `commit-and-sync` in the Obsidian-git panel to validate
6. Install Obsidian on iOS, create a new local vault. Vault name is unimportant, the purpose is to initialize the `On My iPhone/Obsidian/` directory in iOS Files
7. Copy the repository folder from desktop to iOS device to `On My iPhone/Obsidian/<repo>` (initialize the Obsidian vault with the same name, e.g. "notes", and use `replace` when copying)
8. Launch iOS Obsidian app
9. Go to Settings > Community Plugins. Enable Community Plugins. Install Obsidian Git
10. Enter GitHub username & Personal Access Token (use the same one from step 2)
11. You should see status messages that your repo is synced
12. Navigate to your README.md, make a test edit and use the git panel (swipe left from right side of screen), make a test `commit-and-push`

</details>