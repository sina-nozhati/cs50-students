---
id: tool-cs50-dev
type: tool
title: Visual Studio Code for CS50
week: null
parent: tools
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/cs50.dev/
- https://cs50.dev/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:40:41+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- cs50-dev
- tool
checksum: sha256:10c8fd1cc542840dbf67cd9d3e88826bf4630ca84da82f6041f20eb3466c6959
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Visual Studio Code for CS50

## 1. Source metadata
- **Title:** Visual Studio Code for CS50
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/cs50.dev/>, <https://cs50.dev/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:40:41+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/cs50.dev/>, <https://cs50.dev/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="visual-studio-code-for-cs50"></a>

### Visual Studio Code for CS50

Visual Studio Code for CS50 is a web app at [cs50.dev](https://cs50.dev/) that adapts [GitHub Codespaces](https://github.com/features/codespaces) for students and teachers. It automates the process of creating a [repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories) inside of CS50’s [GitHub organization](https://github.com/code50), pushing to it an initial [`.devcontainer.json`](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project), and creating a “codespace,” which is a [Docker](https://en.wikipedia.org/wiki/Docker_(software)) “container” in the cloud (akin to your very own virtual server). Ultimately, it allows students to start programming with just a browser, without needing to install or configure anything locally on their own computer. Within their browser is a full-fledged version of [Visual Studio Code](https://code.visualstudio.com/), aka VS Code, including a tabbed text editor, terminal window (connected to a Docker container running [`cs50/codespace`](https://cs50.readthedocs.io/cs50/codespace/)), and graphical file explorer.

You can also [use VS Code locally](https://cs50.readthedocs.io/cs50.dev/#vs-code-desktop), even offline without internet, particularly if feeling more comfortable.

<a id="settings"></a>

#### Settings

VS Code supports quite a few [settings](https://code.visualstudio.com/docs/getstarted/settings) via which you can customize a codespace:

1. User settings, which “apply globally to any instance of VS Code you open” and can be applied to codespaces as well via [Settings Sync](https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-codespaces-for-your-account#settings-sync).
2. Remote settings, which are set by CS50 via `.devcontainer.json` file in a codespace. [Remote settings override User settings](https://code.visualstudio.com/docs/getstarted/settings#_settings-precedence).
3. Workspace settings, which can be set by you via VS Code’s GUI (or by editing `.vscode/settings.json` manually). [Workspace settings override Remote settings](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#creating-a-custom-codespace-configuration).

In other words, Workspace settings override Remote settings, and Remote settings override User settings.

If you use VS Code outside of CS50, you might thus want to store most of your settings in User settings (and enable Settings Sync). And if you would like to override any of [CS50’s Remote settings](https://cs50.dev/settings.json), you can do so via Workspace settings.

<a id="themes"></a>

##### Themes

See [code.visualstudio.com/docs/getstarted/themes](https://code.visualstudio.com/docs/getstarted/themes).

<a id="user-interface"></a>

##### User Interface

See [code.visualstudio.com/docs/getstarted/userinterface](https://code.visualstudio.com/docs/getstarted/userinterface).

<a id="shortcuts"></a>

#### Shortcuts

* Visit [cs50.dev/codespaces](https://cs50.dev/codespaces) to access your codespaces in CS50’s GitHub organization.
* Visit [cs50.dev/commits](https://cs50.dev/commits) to access all of the commits that have been pushed to your repository in CS50’s GitHub organization.
* Visit [cs50.dev/devcontainer.json](https://cs50.dev/.devcontainer.json) for the latest version of CS50’s `.devcontainer.json` template.
* Visit [cs50.dev/repo](https://cs50.dev/repo) to access your repository in CS50’s GitHub organization.
* Visit [cs50.dev/restart](https://cs50.dev/restart) to restart your codespace.
* Visit [cs50.dev/rstudio-prefs.json](https://cs50.dev/rstudio-prefs.json) for the latest version of CS50’s RStudio preferences.
* Visit [cs50.dev/settings.json](https://cs50.dev/settings.json) for CS50’s default settings for VS Code.
* Visit [cs50.dev/stop](https://cs50.dev/stop) to stop your codespace.
* Visit [cs50.dev/update50.sh](https://cs50.dev/update50.sh) for the latest version of `update50`.

<a id="vs-code-desktop"></a>

#### VS Code Desktop

If feeling more comfortable, you can also use VS Code locally:

* without Docker, but with internet access, so that you can connect to a codespace remotely
* with Docker, via which you’d run a codespace-like container on your own computer, even without internet access

<a id="online-without-docker"></a>

##### Online, without Docker

To use VS Code locally without Docker, but with internet access, connecting to a codespace remotely:

1. Download and install [VS Code](https://code.visualstudio.com/download) itself on your computer.
2. Install VS Code’s [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) extension.
3. Visit [cs50.dev](https://cs50.dev/), check **Open in VS Code desktop**, and log in as usual; you should be prompted to open the codespace in VS Code itself.

Alternatively, if already logged into a codespace, click the codespace’s “hamburger” menu (**☰**) and select **Open in VS Code**.

Alternatively still, if already logged into a codespace, open the codespace’s [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), as via **Ctrl+Shift+P** on Linux, **⇧⌘P** on macOS, and **Ctrl+Shift+P** on Windows, select **>Codespaces: Open in VS Code**.

<a id="offline-with-docker"></a>

##### Offline, with Docker

To use VS Code locally with Docker, running a [codespace-like container](https://code.visualstudio.com/docs/remote/containers) on your own computer, even without internet access, and opening a folder like `foo` therein:

1. Download CS50’s latest `.devcontainer.json` file from <https://cs50.dev/.devcontainer.json>, saving it in `foo`. Because the file’s name starts with a dot (i.e., period), it might seem to “disappear” when you download it. But, in a terminal window on Linux or macOS, you should see it with `ls -a`, and at a command prompt in Windows, you should see it with `dir /a`.
2. Download, install, and start [Docker](https://cs50.readthedocs.io/docker/) on your computer.
3. Download and install [VS Code](https://code.visualstudio.com/download) itself on your computer.
4. Install VS Code’s [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
5. Open VS Code’s [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), as via **Ctrl+Shift+P** on Linux, **⇧⌘P** on macOS, and **Ctrl+Shift+P** on Windows, select **>Dev Containers - Open Folder in Container…**, and open `foo`.

Alternatively, select **>Dev Containers: Install devcontainer CLI**, and then, in VS Code’s terminal window, `cd` to `foo` and execute `devcontainer open .`.

Once the container finishes building and starting, you should find that `foo` is mounted within the container at `/workspaces/foo`.

<a id="git"></a>

#### Git

Because a codespace is already associated with a Git repository in CS50’s `code50` organization at <https://github.com/code50>, which is used for automated backups, CS50 effectively disables `git` anytime you’re inside of `/workspaces/$RepositoryName` (which is a codespace’s default directory), wherein `$RepositoryName` is your (numeric) GitHub ID.

However, you can still use `git` outside of that directory, as by cloning other repositories into `/workspaces` itself. For instance, if you’d like to clone <https://github.com/octocat/Hello-World> into a codespace, you could execute

```
cd /workspaces
git clone https://github.com/octocat/Hello-World
cd Hello-World
```

at which point you could use `git` within that `/workspaces/Hello-World` directory as usual. Note that only `/workspaces/$RepositoryName` will be automatically backed up to CS50’s `code50` organization; repositories that you clone into `/workspaces` will not.

<a id="gitignore"></a>

##### gitignore

Currently, only these files will be backed up to your Codespace GitHub repository:

* *.c
* *.cpp
* *.css
* *.db
* *.h
* *.html
* *.java
* *.js
* *.md
* *.py
* *.sql
* *.ts
* *.txt
* Makefile

<a id="github"></a>

#### GitHub

<a id="authorization"></a>

##### Authorization

Visual Studio Code for CS50 is implemented as an [OAuth App](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps#about-oauth-apps) that “lets external applications request authorization to private details in a user’s GitHub account without accessing their password.” When you log into Visual Studio Code for CS50 using your GitHub account, CS50 receives, via a [web application flow](https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#web-application-flow), an “access token” from GitHub (but not your password) via which CS50 can execute certain operations (i.e., API calls) on your behalf.

But you’ll first be prompted to “authorize” CS50. Only then will that access token have certain permissions, limited by [scopes](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps). CS50 currently requests these scopes:

* `codespace`, via which CS50 can create and manage [codespaces](https://github.com/features/codespaces) on your behalf
* `read:org`, so that you can use the [GitHub CLI](https://cli.github.com/)
* `repo`, via which CS50 can manage a [repository](https://docs.github.com/en/repositories) for you and accept your invitation thereto, and via which `git` can access repositories to which your GitHub account has access
* `user:email`, via which CS50 can access the email address with which you’ve registered for GitHub, but not your actual emails

Note that scopes are not as granular as would be ideal. The `codespace` scope technically allows CS50 to manage any of your codespaces, not just the one(s) you use for CS50. And the `repo` scope technically allows CS50 to access any of your repositories, not just the one(s) you use for CS50. In practice, CS50 only uses those scopes to manage CS50-specific resources. But if you have any concerns, you are welcome to create a (separate) GitHub account that you only use for CS50!

<a id="organization-access"></a>

##### Organization Access

When you log into Visual Studio Code for CS50, your codespace is configured with a “token” that has `repo` [scope](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes), which lets `git` access repositories to which your GitHub account has access.

If you try to access a repository that’s owned by an [organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations) that has not granted access to Visual Studio Code for CS50, though, `git` might err with “Repository not found.” (And `gh` might err with “Could not resolve to a Repository.”) To grant (or request) access for that organization, visit [github.com/settings/connections/applications/d1a90a524497a69391fa](https://github.com/settings/connections/applications/d1a90a524497a69391fa). Alternatively, you can configure your codespace to use [SSH](https://cs50.readthedocs.io/github/#ssh) or a [personal access token](https://cs50.readthedocs.io/github/#personal-access-token) instead, both of which would have access to any repositories to which your GitHub account has access, whether or not owned by an organization.

<a id="domains"></a>

##### Domains

Visual Studio Code for CS50 is built atop [GitHub Codespaces](https://github.com/features/codespaces), which requires that you can also access these domains:

* `*.github.com`
* `*.api.github.com`
* `*.azureedge.net`
* `*.github.dev`
* `*.microsoft.com`
* `*.msecnd.net`
* `*.visualstudio.com`
* `*.vscode-webview.net`
* `*.windows.net`

If on a corporate or school network that blocks any of the above, you might need to ask your IT department if they can “allowlist” all of the above.

<a id="copilot"></a>

#### Copilot

Per CS50’s policy on academic honesty, it is *not* reasonable to use AI-based software other than CS50’s own (e.g., ChatGPT, Claude, Copilot, Gemini, et al.) that suggests or completes answers to questions or lines of code, unless explicitly allowed by some assignment, problem set, or project. For example, for CS50x’s final project, it *is* reasonable to use AI-based software other than CS50’s own, but the essence of the work must still be your own. By that point in the course, you’ve learned enough to use such tools as helpers, but you should treat such tools as amplifying, not supplanting, your productivity.

To enable one such tool, [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview), in your codespace, click the gear icon in VS Code’s bottom-left corner (at the bottom of your activity bar), select **Command Palette…**, and search for and select **> Preferences: Open Workspace Settings (JSON)**. If the editor that opens is empty, paste the below into the editor:

```
{
    "extension-uninstaller.skip": [
        "github.copilot"
    ]
}
```

Or, if the editor already contains one or more key/value pairs, paste just the below between the file’s outermost curly braces, ensuring it’s separated by a comma from any key/value pair before it or after it:

```
"extension-uninstaller.skip": [
    "github.copilot"
]
```

Next, close that editor, click the gear icon in VS Code’s bottom-left corner (at the bottom of your activity bar), select **Extensions**, search for and click on **GitHub Copilot**, click **Install**, and then, when it appears, click **Reload Window**.

Finally, once your window has reloaded, click the gear icon in VS Code’s bottom-left corner (at the bottom of your activity bar), select **Command Palette…**, and search for and select **> Chat: Open Chat**.

<a id="troubleshooting"></a>

#### Troubleshooting

<a id="could-not-register-service-workers"></a>

##### Could not register service workers

If using Firefox, [disable Enhanced Tracking Protection](https://support.mozilla.org/en-US/kb/report-breakage-due-blocking), or use a different browser.

<a id="the-workbench-failed-to-connect-to-the-server"></a>

##### The workbench failed to connect to the server

If using Firefox, [disable Enhanced Tracking Protection](https://support.mozilla.org/en-US/kb/report-breakage-due-blocking), or use a different browser.

<a id="i-m-seeing-oh-no-it-looks-like-you-are-offline-error-message"></a>

##### I’m seeing “Oh no, it looks like you are offline” error message.

First of all, make sure all the required [domains](https://cs50.readthedocs.io/cs50.dev/#domains) are not blocked by your device or internet environment.

Check that you have a stable internet connection and that your home, school, or company network is not blocking the connection. If possible, check logging for rejected connections on your device.

<a id="firewall-and-network-configuration"></a>

###### Firewall and Network Configuration

* **Certificate Inspection**: If the school’s network is injecting TLS certificates, it could be flagged as a man-in-the-middle attack. This issue might be resolved by installing the school’s root TLS certificate on students’ local machines or by allowing traffic from trusted domains such as *.github.com, *.windows.net, and *.visualstudio.com.
* **Packet Inspection**: Investigate the packet inspection settings on the firewall to ensure they are not inadvertently blocking or altering secure traffic required for Codespaces connections.

<a id="browser-extensions-and-local-network-configurations"></a>

###### Browser Extensions and Local Network Configurations

* Certain browser extensions or individual network configurations (e.g., VPNs, proxies) may be contributing to the problem.
* Verifying the browsers, extensions, and network settings on affected student devices could help identify additional issues.

The issues are very likely correlated to the **Connectivity V2** feature rolled out by GitHub. Please check their announcement and related troubleshooting guidelines:
<https://github.blog/changelog/2024-02-12-enhanced-codespaces-connection>

To inspect network activity in your browser, follow one of these instructions:

* [Chrome](https://developer.chrome.com/docs/devtools)
* [Firefox](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/)
* [Safari](https://developer.apple.com/documentation/safari-developer-tools/inspecting-safari-macos)

If you see rejected connections, make sure the domains documented by the `/meta` REST API endpoint are not blocked by your firewall. Again, in other words, none of [these domains](https://cs50.readthedocs.io/cs50.dev/#domains) should be blocked.

Optional: For more information, see [REST API endpoints for meta data](https://docs.github.com/en/rest/meta/meta#get-github-meta-information).

You can run this command in your terminal to get the list of domains required by GitHub Codespaces:

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/meta
```

Follow [this instruction](https://cs50.readthedocs.io/github/#personal-access-token) to generate a GitHub personal access token.

Alternatively, to get the list of domains required by GitHub Codespaces, execute the following command using [GitHub CLI](https://cli.github.com/):

```
gh api meta | jq .domains.codespaces
```

<a id="how-to-monitor-global-variables-in-debugger"></a>

##### How to monitor global variables in debugger

In debug50’s **RUN AND DEBUG** pane, there’s a section labeled **WATCH**. You can add expressions to this section, and the debugger will show you the values of these expressions as you step through the program. The expressions can include global variables and array names.

Consider the `plurality` problem, for example. If the arrow to the left of the **WATCH** heading is pointing to the right **>**, click it to expand the section. Then click the plus sign in the section heading to insert a new expression to be watched.

For example, you could type this: `candidates[0]@candidate_count`. Though this is not a legal expression in C, the `@` operator is specially treated by the debugger. This particular watch expression means `display candidate_count elements of the candidates array, starting with the first (i.e., the element at index 0)`.

When the debugger stops at a breakpoint, it will show you the value of the expressions it’s watching. In this example, the array elements are structs, so you may need to expand them using their individual **>** buttons.

<a id="i-can-t-type-anything-in-the-terminal"></a>

##### I can’t type anything in the terminal

If you can’t type anything in the terminal, please do the following:

1. Click the Settings icon (the gear icon on the bottom-left icon).
2. Search for **terminal.integrated.gpuAcceleration**.
3. Click **Workspace**.
4. Set it to **off**.

<a id="getting-command-not-found-error-in-terminal"></a>

##### Getting “command not found” error in terminal

First, double-check that you are typing in the command correctly. Not only must the command be typed exactly as instructed, but spaces and capitalization must be exact as well.

Second, if you are absolutely sure that you are typing the command exactly as it should be and you are still receiving a `command not found` notification, please make sure:

* Your input method does not introduce special characters.
* Your codespace is not currently in recovery mode.
* You are using a codespace provided by CS50.

<a id="codespaces-run-into-recovery-mode"></a>

##### Codespaces run into recovery mode

Occasionally, your codespace might run into a “recovery mode” due to service outage, a container creation error, or the `.devcontainer.json` had been modified incorrectly. Most CS50 commands, such as `check50` and `submit50`, will not work and you can’t compile your code using CS50 libraries.

In recovery mode, your terminal prompt would look like:

```
@githubUserName -> /workspaces/githubId (master) $
```

Normally, your terminal prompt should look like a single dollar sign:

```
$
```

To get out of the recovery mode, please do the following:

1. Confirming there is no ongoing GitHub outage: [githubstatus.com](https://githubstatus.com)
2. Run this command (copy-paste it to your Codespace terminal):

   ```
   curl https://cs50.dev/devcontainer.json > /workspaces/$RepositoryName/.devcontainer.json
   ```
3. Click the “Extensions” icon on the left, search for the “GitHub Codespaces” extension and install it (if not installed)
4. After installing “GitHub Codespaces” extension, press “Command + Shift + P” (if on macOS) or “Ctrl + Shift + P” (if on Windows), search for “Codespaces: Rebuild Container” then press `Enter` on the keyboard,select the `Full Rebuild` (not `Rebuild`) option to perform a codespace rebuild.
5. Your codespace will be launched once the rebuild process is completed.

<a id="creating-a-new-codespace"></a>

##### Creating a new Codespace

If your codespace repeatedly runs into recovery mode and the above steps do not resolve the issue, you might want to try creating a new codespace:

1. Visit [cs50.dev/codespaces](https://cs50.dev/codespaces).
2. Click **Create codespace on main** (the green button).
3. Wait for your codespace to launch.

Please do NOT delete your old codespace unless you are sure all your files have been synced properly with repository at [cs50.dev/repo](https://cs50.dev/repo).

<a id="gitdoc-failed-to-sync-with-backing-repository"></a>

##### GitDoc failed to sync with backing repository

If GitDoc is showing a GitHub Authentication error, please do the following:

1. Visit [cs50.dev](https://cs50.dev/).
2. Click **Login via GitHub**.
3. Click to **Authorize cs50**.
4. Once your codespace is launched, visit [cs50.dev/restart](https://cs50.dev/restart).

<a id="missing-files-in-codespace"></a>

##### Missing files in Codespace

If you believe some of your files might be missing on your current Codespace, please first check to see if you have more than one Codespace by visiting: <https://github.com/codespaces> and you should see a list of Codespaces under “Owned by code50”.

Some of your files could exist on previous Codespaces, in which it is indicated as “`Last used XXX hours/days ago`”. To access these Codespaces and retrieve the files, please do the followings:

1. Click on the Codespace name to launch it
2. Once your Codespace is launched, go to File Explorer
3. Right-click a file or folder
4. Click “Download…” to download files to your local computer

If you can’t find your missing files in any of your codespaces, look for them in your repository at <https://cs50.dev/repo> instead.

Alternatively, if you have submitted any assignments via `submit50`, you can access those at <https://github.com/me50>. Or, if you have submitted any assignments via Gradescope, you can access those at <https://www.gradescope.com/>.

<a id="other-common-questions"></a>

##### Other Common Questions

1. Why is an extension not installable in the browser?
2. How do I allow VS Code to access my clipboard for reading?
3. How do I allow VS Code to always open new tabs and windows?
4. How do I allow VS Code in a browser to access local files and folders?

See <https://code.visualstudio.com/docs/remote/codespaces#_common-questions>.

<a id="deleting-a-codespace"></a>

##### Deleting a Codespace

**Deleting a codespace will delete all files and folders therein.** If you are sure you want to delete a codespace:

1. Visit [cs50.dev/codespaces](https://cs50.dev/codespaces).
2. Under **Your codespaces**, to the right of `main`, click ***…***, select **Delete**, and click **OK**.

You can then create a new codespace by logging back into [cs50.dev](https://cs50.dev/).

<a id="acknowledgements"></a>

#### Acknowledgements

Special thanks to CS50’s friends at [GitHub](https://github.com/) and [Microsoft](https://www.microsoft.com/) for their support of this app!

### cs50.dev home page (verbatim text)

Log In

Toggle Dropdown

or browse [documentation](https://cs50.readthedocs.io/cs50.dev/)

* Open in VS Code Desktop
* ---
* [Restart Codespace](https://cs50.dev/restart)
* ---
* Backups
* [Commits](https://cs50.dev/commits)
* [Repository](https://cs50.dev/repo)

![Codespaces](https://cs50.dev/static/dependencies-3.png)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [CS50 tools (index)](README.md) (`tools`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
مستند ابزار رسمی CS50؛ برای راهنمای فارسی نصب و استفاده و پاسخ‌گویی به سؤال‌های فنی دانشجویان.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- فقط بر اساس محتوای رسمی بخش ۲ پاسخ بده و لینک دقیق (با anchor) را ذکر کن.
- اگر پاسخ در منبع نیست، صریحاً بگو «در منبع رسمی ذکر نشده» و حدس نزن.


### ایده‌های پیاده‌سازی در سایت
- نمایش این سند به‌صورت یک صفحه/کارت در بخش منابع (`Resource`) با پیوند به منبع رسمی و درج ذکر منبع و مجوز CC BY-NC-SA.
- نمایه‌سازی بخش‌های این سند در search.jsonl برای جست‌وجو و RAG.


## 6. References, review, gaps
- https://cs50.readthedocs.io/cs50.dev/ — retrieved 2026-10-18T05:40:41+03:30, sha256 `10c8fd1cc542840d…`
- https://cs50.dev/ — retrieved 2026-10-18T05:40:44+03:30, sha256 `e6568f70acf65f1d…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
