Git Notes from Udacity Version Control with Git
#Git Cheat Sheet
## Mac Terminal Set Up

Switch between Bash and Zsh
	Bash: `chsh -s /bin/bash`
	Zsh: `chsh -s /bin/zsh`
	Relaunch terminal for changes to take place

## First Time Git Configuration:
 [udacity-terminal-config.zip](https://video.udacity-data.com/topher/2017/March/58d31ce3_ud123-udacity-terminal-config/ud123-udacity-terminal-config.zip)

To configure the terminal, perform the following steps:
1.  download the zipped file from the Resources pane, or the bottom of this page
2.  move the directory udacity-terminal-config to your home directory and name it .udacity-terminal-config(there's a dot at the front, now!)
3.  move the bash_profile file to your home directory and name it .bash_profile (there's a dot at the front, now!)
-   if you already have a .bash_profile file in your home directory, transfer the content from the downloaded bash_profile to your existing .bash_profile
    
Before you can start using Git, you need to configure it. Run each of the following lines on the command line to make sure everything is set up.

### sets up Git with your name
`git config --global user.name "<Your-Full-Name>"`
  
### sets up Git with your email
`git config --global user.email "<your-email-address>"`

### makes sure that Git output is colored
`git config --global color.ui auto`

  
### displays the original state in a conflict

`git config --global merge.conflictstyle diff3`

`git config --list`

### Code Editor Setup

#### Sublime Text Setup

`git config --global core.editor "'/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl' -n -w"`

#### VSCode Setup
`git config --global core.editor "code --wait"`


[https://stackoverflow.com/questions/30024353/how-to-use-visual-studio-code-as-default-editor-for-git](https://stackoverflow.com/questions/30024353/how-to-use-visual-studio-code-as-default-editor-for-git)

Mac: Make sure you can run code --help from the command line and you get help.

-   if you do not see help, please follow these steps:
    
-   Mac: Select Shell Command: Install 'Code' command in path from the Command Palette.
    
-   Command Palette is what pops up when you press shift + ⌘ + P while inside VS Code. (shift + ctrl+ P in Windows)

Git stores configuration options in three separate files, which lets you scope options to individual repositories (local), user (Global), or the entire system (system):

-   Local: /.git/config – Repository-specific settings.
    
-   Global: /.gitconfig – User-specific settings. This is where options set with the --global flag are stored.
    
-   System: $(prefix)/etc/gitconfig – System-wide settings.
    
When options in these files conflict, local settings override user settings, which override system-wide.

### Personal Access Token
ERROR:
```Command line error when attempting to push:
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com...
```
SOLUTION: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token


## Vocabulary
commit - the fundamental unit in Git

repository - is a directory which contains your project work, as well as a few files (hidden by default on Mac OS X) which are used to communicate with Git. Repositories can exist either locally on your computer or as a remote copy on another computer. A repository is made up of commits.

Working Directory - is the files that you see in your computer's file system.

checkout - is when content in the repository has been copied to the Working Directory.

staging area - as a prep table where Git will take the next commit. Files on the Staging Index are poised to be added to the repository. file in the Git directory that stores information about what will go into your next commit

SHA - shorthand for "Secure Hash Algorithm”. Is an ID number for each commit.

branch - is when a new line of development is created that diverges from the main line of development. 
* This alternative line of development can continue without altering the main line.  
* The key thing that makes branches incredibly powerful is that you can make save points on one branch, and then switch to a different branch and make save points there, too.

Git Workflow - 3 distinct areas Working Directory - > Staging Indes/Area -> Repository

### Create a Repository
`git init`

#### Empty Directory

Initialize an empty Git repository in the current directory. Creating a .git/ directory with several directories. The hooks directory - this is where we could place client-side or server-side scripts that we can use to hook into Git's different lifecycle events, the only directory we can modify. All others should be avoided.

#### Existing Directory with Files

If you want to start version-controlling existing files (as opposed to an empty directory), you should probably begin tracking those files and do an initial commit. You can accomplish that with a few git add commands that specify the files you want to track, followed by a git commit:

$ `git add *.c`

$ `git add LICENSE`

$ `git commit -m 'Initial project version'`

Example:

$ cd /path/to/my/codebase

$ `git init` (1)

$ `git add .` (2)

$ `git commit` (3)

1.  Create a /path/to/my/codebase/.git directory.
    
2.  Add all existing files to the index.
    
3.  Record the pristine state as the first commit in the history.
    
#### Cloning an Existing Repo

`git clone`

1. creates a named directory, (you can specify the new directory name as an additional argument: space directoryName)

2. initializes a .git directory inside it,

3. pulls down all the data for that repository, and

4. checks out a working copy of the latest version.

5. will automatically configure your repo with a remote pointed to the Git URL you cloned it from. This means that once you make changes to a file and commit them, you can git push those changes to the remote repository.

6. creates remote-tracking branches for each branch in the cloned repository (visible using git branch --remotes), and creates and checks out an initial branch that is forked from the cloned repository’s currently active branch.

After the clone, a plain `git fetch` without arguments will update all the remote-tracking branches, and a git pull without arguments will in addition merge the remote master branch into the current master branch,

This default configuration is achieved by creating references to the remote branch heads under refs/remotes/origin and by initializing remote.origin.url and remote.origin.fetch configuration variables.

If you used `git init` to make a fresh repo, you'll have no remote repo to push changes to.

Once you have a remote repo setup, you will need to add a remote repo url to your local git config, and set an upstream branch for your local branches. The git remote command offers such utility.

`git remote add <remote_name> <remote_repo_url>`

This command will map remote repository at to a ref in your local repo under . Once you have mapped the remote repo you can push local branches to it.

`git push -u <remote_name> <local_branch_name>`

This command will push the local repo branch under < local_branch_name > to the remote repo at < remote_name >.

Advanced: [https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)

Git Hooks: [https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)

### Customizing Git with Scripts

1.  Client Side
    
2.  Server Side
    

Triggered by operations ie. commits, merges

-   [Initializing a Repository in an Existing Directory](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#Initializing-a-Repository-in-an-Existing-Directory)
    
-   [git init docs](https://git-scm.com/docs/git-init)
    
-   [git init Tutorial](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
    

Helpful Links

-   [Checking the Status of Your Files](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Checking-the-Status-of-Your-Files)
    
-   [git status docs](https://git-scm.com/docs/git-status)
    
-   [git status Tutorial](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-status)
    

### Git History

  

#### Git log

-   git log
    
-   git log --oneline
    
-   git log --stat
    
-   git log -p
    

providing the SHA of the commit you want to see to git log

$ git log -p fdf5493

#### Git show

`git show` command will show only one commit

output of the git show command is exactly the same as the git log -p command

can be combined with most of the other flags we've looked at:

-   --stat - to show the how many files were changed and the number of lines that were added/removed
    
-   -p or --patch - this the default, but if --stat is used, the patch won't display, so pass -p to add it again
    
-   -w - to ignore changes to whitespace
    
`git add` - command is used to move files from the Working Directory to the Staging Index

The act of moving a file from the Working Directory to the Staging Index is called "staging"

$ git add css/app.css js/app.js

would become

$ git add .

The period refers to the current directory and can be used as a shortcut to refer to all files and directories (including all nested files and directories!).

git commit command, this command will open the code editor

Write message on the first line

save the file and close the editor window (closing just the pane/tab isn't enough, you need to close the code editor window that the git commit command opened).

## Bypass The Editor With The -m Flag

$ git commit -m "Initial commit"

The goal is that each commit has a single focus. Each commit should record a single-unit change.

isn't limiting the number of lines of code or the number of files that are added/removed/modified

git diff command can be used to see changes that have been made but haven't been committed, yet.

### Further Research

-   [git diff](https://git-scm.com/docs/git-diff) from the Git Docs
    

Git Ignor Files

.gitignore file with files to ignore

To add multiple files at once:

Globbing lets you use special characters to match patterns/characters. In the .gitignore file, you can use the following:

-   blank lines can be used for spacing
    
-   '#' - marks line as a comment
    
-   '*' - matches 0 or more characters
    
-   ? - matches 1 character
    
-   [abc] - matches a, b, _or_ c
    
-   ** - matches nested directories - a/**/z matches

-   a/z
    
-   a/b/z
    
-   a/b/c/z

To add 50 images are JPEG images in the "samples" folder to .gitignore

samples/*.jpg

### Further Research
-   [Ignoring files](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Ignoring-Files) from the Git Book
-   [gitignore](https://git-scm.com/docs/gitignore#_pattern_format) from the Git Docs
-   [Ignoring files](https://help.github.com/articles/ignoring-files/) from the GitHub Docs
-   [gitignore.io](https://www.gitignore.io/)
    

Tagging, Branching and Merging

create a branch with the git branch command and then switch to that newly created branch with the git checkout command

git checkout command can actually create a new branch, too? If you provide the -b flag, you can create a branch and switch to it all in one command.

$ git checkout -b footer master.

## See All Branches At Once

$ `git log --oneline --graph --all`

The --graph flag adds the bullets and lines to the leftmost part of the output. This shows the actual branching that's happening. The --all flag is what displays all of the branches in the repository.

### Further Research
-   [Basic Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#Basic-Merging) from Git Book
-   [git-merge](https://git-scm.com/docs/git-merge) from Git Docs
-   [git merge](https://www.atlassian.com/git/tutorials/git-merge) from Atlassian blog
