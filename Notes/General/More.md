
# GoogleCloud
- Create a project:
[https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run](https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run?authuser=2)
- https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run
- Connect to a proxy: cloud_sql_proxy -instances=mygreyarea-1:us-central1:mga-db=tcp:3306
- Authenticate with key: gcloud auth activate-service-account --key-file Key/GreyKey.json

# GIT 

Generic Notes:

- Create Repo: git remote add origin

[git@github.com](mailto:git@github.com)

:User/UserRepo.git

- Set remote repo: git remote set-url origin

[git@github.com](mailto:git@github.com)

:User/UserRepo.git

- Reset to origin:	git reset --hard origin/master

Push/Pull:

- Push to origin: git push -u origin master
- Pull: git pullgit

Branches:

- All branches: git branch -a.
- Delete branch: git branch -d <branch name>
- Create branch: git branch <new branch>
- Checkout branch: git checkout

Git Clone:

- Creates repository... must step inside to start making changes

Reset to before changes made in order to pull

git reset --hard

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/219f6c49-b4ac-4794-ae8c-d7a88eb447cd/Untitled.png)

## Wiki notes

## Remotes

- git remote add origin "url"

## Branchs

- git branch -v
- show branches - git branch
- create branch - git branch "name"
- checkout branch - git checkout "branch name"

## Process flow

- show changes since merge - git status
- add files git add:
    - . - allfiles
    - files
- git commit -m "comment of changes"
- switch back to main branch
- git merge old branch


# Linux

General Notes for Linux:

- Get help on command: man (command)
- List files in location: ls
- This location: .
- Create Directory: mkdir

sudo -i

## VNC Viewer

vnc setup helper [script](https://help.realvnc.com/hc/en-us/community/posts/5021325365917-VNC-Server-wont-work-on-a-new-Ubuntu-Desktop-Install)

# Troubleshooting
Trouble with chrome and connecting - [Delete Local Host](https://stackoverflow.com/questions/33524826/localhost-not-working-in-chrome-127-0-0-1-does-work)

- [Snippets](https://github.com/Microsoft/vscode/issues/28048)