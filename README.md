HOW TO CREATE AND PUSH GIT REPO

Initialize git repo
    git init

Add files in directory to the repo
    git add .

Commit
    git commit -m "first commit"

Check status (optional)
    git status

Add the url origin of your remote github repo
    git remote add origin https://access_token@github.com/username/repo_name.git

Set the branch
    git branch -M main

Push the repo to remote
    git push -u origin main

How to create a new file and add content to it simultaneously (Windows):
    echo "content here" > filename.extension
    echo . > filename.extension (adds a new line)

How to change git url origin
    git remote set-url origin https://access_token@github.com/username/repo_name.git

After creating a virtual environment in vscode, you have to activate it so that you can access it in terminal (to stuff like pip install, otherwise pip install might occur in global python instead of local venv python)

    How to activate:
        Run this command: source .venv/bin/activate
