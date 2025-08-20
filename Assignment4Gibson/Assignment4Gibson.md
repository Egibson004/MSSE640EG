Assignment 4: Git Branching and Pull Requests
This document outlines the process of working with a feature branch in Git, from creation to merging via a pull request on GitHub.

1. Creating a Feature Branch
To begin, I created a new feature branch named feature-update-readme directly within Visual Studio Code. This is done by clicking the branch icon in the bottom-left corner and selecting + Create new branch....

After creating the branch, I can verify it exists locally using the command line.
<img src="BranchPublish.JPG">

Bash

$ git branch
  main
* feature-update-readme
The * indicates that feature-update-readme is my current active branch.

Does a remote branch exist yet?
No. Creating a branch locally does not automatically create it on the remote repository. I can confirm this by listing the remote branches with git branch -r.

Bash

$ git branch -r
  origin/main
As you can see, only the origin/main branch exists on the remote.

2. Committing and Publishing the Branch
Next, I made a small change to a file in my project. I then committed this change to my new local branch and used the "Publish Branch" button in VS Code to push it to the remote GitHub repository.

What is different when you run git branch and git branch -r?
The difference is that git branch lists your local branches, while git branch -r lists your remote-tracking branches. A remote-tracking branch is a local reference to the state of a branch on the remote repository.

After publishing my new branch, the output of these commands is now different:

Local Branches: (git branch)
The local list remains the same.

Bash

$ git branch
  main
* feature-update-readme
Remote-Tracking Branches: (git branch -r)
The new branch now appears in the remote list, prefixed with origin/.

Bash

$ git branch -r
  origin/main
  origin/feature-update-readme
3. Creating and Merging a Pull Request
With my changes pushed to the feature-update-readme branch on GitHub, I navigated to the repository's URL. GitHub automatically prompted me to create a Pull Request (PR). I created the PR to merge my feature branch into the main branch.

After reviewing the changes, I merged the PR and selected the option to delete the remote feature branch since its work was complete.

Will the local feature branch still exist?
Yes. Deleting the remote branch on GitHub after a merge does not affect the local branch on my machine. I can verify it's still there using git branch.

Bash

$ git branch
  main
* feature-update-readme
4. Cleaning Up Local and Remote Branches
To sync my local repository with the remote and remove the obsolete reference to the deleted remote branch, I run git fetch -p (the -p stands for --prune).

Bash

$ git fetch -p
From github.com:YourUsername/YourRepo
 - [deleted]         (none)     -> origin/feature-update-readme
This command updates my local list of remote-tracking branches, removing the one that was deleted on GitHub. Now, running git branch -r shows that the remote-tracking branch is gone.

Bash

$ git branch -r
  origin/main
Finally, since the feature is merged and the branch is no longer needed, I will switch back to my main branch and delete the local feature branch.

Bash

# Switch to the main branch first
$ git checkout main

# Delete the local feature branch
$ git branch -d feature-update-readme
Deleted branch feature-update-readme (was 1a2b3c4).

# Verify it's gone
$ git branch
* main