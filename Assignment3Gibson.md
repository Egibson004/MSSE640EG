## ACTIVITY 1:

- Perform the following activities in Git and post the commands and the results in your Markdown file for the week.
- Ensure that your commands and output are enclosed in a code fence.

### Configuration

1. What are the commands to configure your user.name and your user.email. Should this be configured globally or in your repo. Why or why not?

    The commands to configure your `user.name` and `user.email` are:

    ```bash
    git config --global user.name "Ethan Gibson"
    git config --global user.email "egibson004@regis.edu"
    ```

    These should generally be configured *globally*. Configuring them globally sets your identity for all Git repositories on your system, which is usually what you want. If you configure them only in a specific repository (by omitting `--global`), those settings will only apply to that single repository. While this can be useful in specific scenarios (e.g., contributing to an open-source project with a different identity), for general use, global configuration is more convenient and prevents you from having to set it up for every new repository.

2. How do you configure the core editor for git?

    You configure the core editor for Git using the `core.editor` setting. For example, to set VS Code as your default editor:

    ```bash
    git config --global core.editor "code --wait"
    ```

    Or for Nano:

    ```bash
    git config --global core.editor "nano"
    ```

3. How do you view your global config and your local (for the repo) config.

    To view your global configuration:

    ```bash
    git config --global --list
    ```

    To view your local configuration (from within a Git repository):

    ```bash
    git config --local --list
    ```

    Or simply:

    ```bash
    git config --list
    ```
    (This will show both local and global settings, with local settings overriding global ones if there's a conflict.)

### Working with a local repo

4. What are the steps to create a new local repo via the CLI?

    1. Create a new directory:
        ```bash
        mkdir my-new-repo
        ```
    2. Navigate into the directory:
        ```bash
        cd my-new-repo
        ```
    3. Initialize a new Git repository:
        ```bash
        git init
        ```

    Example output:
    ```
    $ mkdir my-new-repo
    $ cd my-new-repo
    $ git init
    Initialized empty Git repository in /c/Users/YourUser/my-new-repo/.git/
    ```

5. How do you clone a repo and what's the difference between cloning and creating a new repo from scratch? Practice cloning a public repo from somewhere.

    To clone a repo, you use the `git clone` command followed by the repository's URL. For example, cloning my own repository:

    ```bash
    git clone [https://github.com/Egibson004/MSSE640EG.git](https://github.com/Egibson004/MSSE640EG.git)
    ```

    Example output:
    ```
    $ git clone [https://github.com/Egibson004/MSSE640EG.git](https://github.com/Egibson004/MSSE640EG.git)
    Cloning into 'MSSE640EG'...
    remote: Enumerating objects: 3, done.
    remote: Counting objects: 100% (3/3), done.
    remote: Compressing objects: 100% (2/2), done.
    remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    Receiving objects: 100% (3/3), 2.29 KiB | 2.29 MiB/s, done.
    ```

    **Difference between cloning and creating a new repo from scratch:**

    * **Cloning:** When you `git clone` a repository, you are creating a local copy of an *existing* remote repository. This local copy includes all the project's files, commit history, branches, and a remote tracking connection to the original repository. It's used when you want to start working on a project that someone else (or you) has already started.

    * **Creating a new repo from scratch (`git init`):** When you use `git init`, you are initializing an *empty* Git repository in your current directory. It creates the necessary `.git` directory to track changes, but there are no files or commit history yet. You then add your project files and start making initial commits. This is used when you are starting a brand new project and want to begin tracking its version control.

6. How do you look at the status of your repo? What information does this give you?

    You look at the status of your repo using the `git status` command:

    ```bash
    git status
    ```

    Example output (after creating a new file `test.txt`):
    ```
    $ git status
    On branch main

    No commits yet

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            test.txt

    nothing added to commit but untracked files present (use "git add" to track)
    ```

    The `git status` command provides vital information about the current state of your repository, including:
    * **Current branch:** Which branch you are currently on (e.g., `On branch main`).
    * **Untracked files:** Files that are in your working directory but are not yet being tracked by Git.
    * **Changes to be committed:** Files that have been staged and are ready for the next commit.
    * **Changes not staged for commit:** Files that have been modified but have not yet been staged.
    * **Your branch is up to date/ahead/behind:** Information about the synchronization status of your local branch with its remote counterpart.

7. How do you stage changes to your local repo in preparation for a commit?

    You stage changes using the `git add` command.
    * To stage a specific file:
        ```bash
        git add filename.txt
        ```
    * To stage all changes in the current directory and its subdirectories:
        ```bash
        git add .
        ```
    Example (after creating `new_file.txt` and modifying `existing_file.txt`):
    ```bash
    $ echo "This is a new file." > new_file.txt
    $ echo "Adding a new line." >> existing_file.txt
    $ git status
    On branch main
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            new_file.txt

    nothing added to commit but untracked files present (use "git add" to track)

    $ git add .
    $ git status
    On branch main
    No commits yet

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)
            new_file.txt
    ```

8. How do you commit changes to your local repo?

    You commit changes using the `git commit` command.
    * With a message directly in the command:
        ```bash
        git commit -m "Your commit message here"
        ```
    * To open your configured editor for a longer message:
        ```bash
        git commit
        ```
    Example (after staging `new_file.txt`):
    ```bash
    $ git commit -m "Add new_file.txt"
    [main (root-commit) 6a3b2c1] Add new_file.txt
     1 file changed, 1 insertion(+)
     create mode 100644 new_file.txt
    ```

9. Include an example of a file that will allow you to "ignore" files in your repo. What kinds of files should not be part of your version control?

    To ignore files, you create a file named `.gitignore` in the root of your repository. Here's an example `.gitignore` file:

    ```
    # Ignore all .log files
    *.log

    # Ignore a specific file
    my_secret_key.pem

    # Ignore all files in the 'build' directory
    /build/

    # Ignore all .DS_Store files (macOS specific)
    .DS_Store

    # Ignore Node.js module dependencies
    node_modules/

    # Ignore compiled Python files
    __pycache__/
    *.pyc

    # Ignore environment variables file
    .env
    ```

    Kinds of files that should generally **not** be part of your version control include:
    * **Compiled code or build artifacts:** Files generated during the build process (e.g., `.class` files, `.o` files, `target/` directories). These can be regenerated from source code.
    * **Operating system specific files:** Files created by the OS (e.g., `.DS_Store` on macOS, `Thumbs.db` on Windows).
    * **Dependencies/packages:** Directories for downloaded libraries or packages (e.g., `node_modules/`, `vendor/` for PHP, `venv/` for Python). These should be managed by package managers and installed separately.
    * **Sensitive information:** API keys, passwords, private certificates, or other credentials. These should be kept out of version control for security reasons.
    * **User-specific configuration files:** Files that contain settings unique to a developer's local environment.
    * **Log files:** Files that contain application logs.
    * **Temporary files:** Files created as temporary storage during program execution.

10. When files are under version control, you can't delete them using the OS commands. How do you delete files using git.

    When files are under Git version control, you *can* delete them using OS commands, but Git will mark them as "deleted" (or "missing") in your working directory. To properly delete a file from Git's tracking and from your working directory, you should use `git rm`.

    To delete a file using Git:

    ```bash
    git rm filename.txt
    ```

    This command removes the file from your working directory and stages the deletion for the next commit.

    Example:
    ```bash
    $ touch file_to_delete.txt
    $ git add file_to_delete.txt
    $ git commit -m "Add file to delete"
    [main abcd123] Add file to delete
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 file_to_delete.txt

    $ git rm file_to_delete.txt
    rm 'file_to_delete.txt'

    $ git status
    On branch main
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            deleted:    file_to_delete.txt

    $ git commit -m "Delete file_to_delete.txt"
    [main efgh456] Delete file_to_delete.txt
     1 file changed, 0 insertions(+), 0 deletions(-)
     delete mode 100644 file_to_delete.txt
    ```

    If you want to remove a file from Git's tracking but keep it in your local working directory (e.g., you added it by mistake and now want to ignore it), you can use `git rm --cached`:

    ```bash
    git rm --cached filename.txt
    ```

### Working with a remote

11. How do you view the remote repo that is associated with your local repo?

    You view the remote repositories associated with your local repo using the `git remote` command:

    ```bash
    git remote -v
    ```

    The `-v` (verbose) flag shows the URL for each remote.

    Example output after cloning your repo:
    ```
    $ git remote -v
    origin  [https://github.com/Egibson004/MSSE640EG.git](https://github.com/Egibson004/MSSE640EG.git) (fetch)
    origin  [https://github.com/Egibson004/MSSE640EG.git](https://github.com/Egibson004/MSSE640EG.git) (push)
    ```

12. What is the function of the ```git fetch``` command?

    The `git fetch` command is used to download commits, files, and refs from a remote repository into your local repository without merging them into your current working branch. It updates your *remote-tracking branches* (e.g., `origin/main` or `origin/master`) with the latest changes from the remote.

    Its primary function is to:
    * **See what's new on the remote:** It allows you to inspect changes that have occurred on the remote repository without affecting your local work.
    * **Update remote-tracking branches:** It brings your local knowledge of the remote's branches up to date.
    * **Prepare for a pull:** It's often the first step before a `git pull` if you want to review changes before integrating them.

    Example:
    ```bash
    $ git fetch origin
    remote: Enumerating objects: 5, done.
    remote: Counting objects: 100% (5/5), done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (3/3), 642 bytes | 642.00 KiB/s, done.
    From [https://github.com/Egibson004/MSSE640EG](https://github.com/Egibson004/MSSE640EG)
       a1b2c3d..e4f5g6h  main       -> origin/main
    ```

13. What is the difference between fetch and pull. Practice using both and show the results.

    **`git fetch`**:
    * **Downloads changes:** Retrieves changes from the remote repository.
    * **Does NOT merge:** It updates your remote-tracking branches (e.g., `origin/main`), but does not integrate these changes into your local working branch.
    * **Safe:** It's a safe way to see what others have been working on without altering your current local branch.

    **`git pull`**:
    * **Downloads AND merges:** It performs a `git fetch` followed by a `git merge` (or `git rebase`, depending on configuration). This means it downloads changes and then attempts to integrate them into your current local working branch.
    * **Can cause conflicts:** If there are conflicting changes between your local work and the fetched changes, a merge conflict can occur, which you'll need to resolve.
    * **Convenient for quick updates:** It's a common command for bringing your local branch fully up-to-date with its remote counterpart.

    **Practice and Results:**

    * **Scenario:** Assume your remote repository (`https://github.com/Egibson004/MSSE640EG.git`) has some changes that are not yet on your local `main` branch.

    * **Using `git fetch`:**

        ```bash
        # (Inside your local repository)
        $ git status
        On branch main
        Your branch is up to date with 'origin/main'.

        # (Someone else pushes a change to the remote 'main' branch of your repo)

        $ git fetch origin
        remote: Enumerating objects: 5, done.
        remote: Counting objects: 100% (5/5), done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3), 642 bytes | 642.00 KiB/s, done.
        From [https://github.com/Egibson004/MSSE640EG](https://github.com/Egibson004/MSSE640EG)
           a1b2c3d..e4f5g6h  main       -> origin/main

        $ git status
        On branch main
        Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
          (use "git pull" to update your local branch)
        ```
        *Result:* `git fetch` updated `origin/main` and `git status` now tells you your local `main` is behind. Your local files are unchanged.

    * **Using `git pull`:**

        ```bash
        # (Assuming you are in the same state as after the fetch, or have not fetched yet)
        $ git pull origin main
        remote: Enumerating objects: 5, done.
        remote: Counting objects: 100% (5/5), done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3), 642 bytes | 642.00 KiB/s, done.
        From [https://github.com/Egibson004/MSSE640EG](https://github.com/Egibson004/MSSE640EG)
           a1b2c3d..e4f5g6h  main       -> origin/main
        Updating a1b2c3d..e4f5g6h
        Fast-forward
         new_file.txt | 1 +
         1 file changed, 1 insertion(+)

        $ git status
        On branch main
        Your branch is up to date with 'origin/main'.
        ```
        *Result:* `git pull` downloaded the changes and automatically merged them into your local `main` branch. Your local files are now updated.

14. Make some changes in your repo and using the command line to sync those changes with your remote repo. Show the results.

    1.  **Make changes:**
        ```bash
        $ echo "This is a new line for syncing." >> README.md
        ```

    2.  **Stage the changes:**
        ```bash
        $ git add README.md
        ```

    3.  **Commit the changes:**
        ```bash
        $ git commit -m "Add a new line to README for syncing"
        [main 7f8e9d0] Add a new line to README for syncing
         1 file changed, 1 insertion(+)
        ```

    4.  **Push the changes to the remote:**
        ```bash
        $ git push origin main
        Enumerating objects: 5, done.
        Counting objects: 100% (5/5), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (3/3), done.
        Writing objects: 100% (3/3), 324 bytes | 324.00 KiB/s, done.
        Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
        To [https://github.com/Egibson004/MSSE640EG.git](https://github.com/Egibson004/MSSE640EG.git)
           e4f5g6h..7f8e9d0  main -> main
        ```
        *Result:* The changes made locally (`Add a new line to README for syncing` commit) have been successfully sent to the `main` branch on the `origin` remote repository (`https://github.com/Egibson004/MSSE640EG.git`). You can verify this by checking your GitHub repository online.

### Branches

14. How do you view the local and the remote branches for your repositories?

    To view local branches:
    ```bash
    git branch
    ```
    Example output:
    ```
    $ git branch
    * main
    ```
    (The asterisk indicates the currently active branch.)

    To view remote branches (including remote-tracking branches):
    ```bash
    git branch -r
    ```
    Example output:
    ```
    $ git branch -r
      origin/HEAD -> origin/main
      origin/main
    ```

    To view all local and remote branches:
    ```bash
    git branch -a
    ```
    Example output:
    ```
    $ git branch -a
    * main
      remotes/origin/HEAD -> remotes/origin/main
      remotes/origin/main
    ```

15. View the local branches and create a new branch. Look again. Show before and after.

    **Before creating a new branch:**

    ```bash
    $ git branch
    * main
    ```

    **Create a new branch:**

    ```bash
    $ git branch new-feature-branch
    ```

    **After creating the new branch (and still on `main`):**

    ```bash
    $ git branch
    * main
      new-feature-branch
    ```

16. What are different ways to switch to a new branch?

    * **Switch to an existing branch:**
        ```bash
        git switch new-feature-branch
        ```
        or the older command:
        ```bash
        git checkout new-feature-branch
        ```
        Example:
        ```bash
        $ git switch new-feature-branch
        Switched to branch 'new-feature-branch'
        $ git branch
          main
        * new-feature-branch
        ```

    * **Create a new branch AND switch to it in one command:**
        ```bash
        git switch -c another-new-branch
        ```
        or the older command:
        ```bash
        git checkout -b another-new-branch
        ```
        Example:
        ```bash
        $ git switch -c another-new-branch
        Switched to a new branch 'another-new-branch'
        $ git branch
          main
          new-feature-branch
        * another-new-branch
        ```

17. Delete your local branch without pushing to a remote or merging to your main branch. Show that it's gone.

    To delete a local branch that has unmerged changes (or hasn't been pushed) you need to use the force delete flag `-D`. If it's a merged branch, you can use `-d`.

    **Current branches (before deletion):**

    ```bash
    $ git branch
      main
    * new-feature-branch
    ```
    (Assume we are on `new-feature-branch` and want to delete it. You must switch to another branch first to delete the one you're on.)

    **Switch to `main` branch:**

    ```bash
    $ git switch main
    Switched to branch 'main'
    ```

    **Delete the `new-feature-branch`:**

    ```bash
    $ git branch -D new-feature-branch
    Deleted branch new-feature-branch (was abc1234).
    ```

    **Show that it's gone (view branches again):**

    ```bash
    $ git branch
    * main
    ```
    ![Delete Branch](branch_delete.JPG)
    
