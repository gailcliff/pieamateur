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