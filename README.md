Welcome to the Open Academy OpenStack project. Browse around this repo for project docs.

Getting Started
===============

Source Code Management with Git
-------------------------------
Familiarity with basic Git commands is needed for the success of this project. If you are new to Fork and Pull Requests, jump over to [Fork](https://help.github.com/articles/fork-a-repo) and [Pull Requests](https://help.github.com/articles/using-pull-requests) for a quick overview. Let's play with some of these commands.

First fork from https://github.com/OpenAcademy-OpenStack/playground into your own organization. The new repository can be cloned with the following command:

    git clone git@github.com:<your-repository>/playground.git
    
Now try

    cd playground
    git remote -v
    
The output of the last command should look like this:

    origin	git@github.com:<your-repository>/playground.git (fetch)
    origin	git@github.com:<your-repository>/playground.git (push)

"origin" refers to the forked repository. Let's add the "upstream" repository as well:

    git remote add upstream https://github.com/OpenAcademy-OpenStack/playground.git
    git remote -v
    
There should be two remote repositories:

    origin	git@github.com:<your-repository>/playground.git (fetch)
    origin	git@github.com:<your-repository>/playground.git (push)
    upstream	https://github.com/OpenAcademy-OpenStack/playground.git (fetch)
    upstream	https://github.com/OpenAcademy-OpenStack/playground.git (push)
    
Next add a file or modify an existing one:

    echo "Adding a new file" > myfile.txt
    
"git status" commmand should list "myfile.txt" as untracked. It can be added via this command:

    git add myfile.txt
    
Next commit this change to the local repository with:

    git commit -m "my first commit"
    
Let's add another line to "myfile.txt" and modify the first commit to include this change:

    echo "\nThis is another line" >> myfile.txt
    git add myfile.txt
    git commit --amend
    
Modify the message as necessary and commit the change. Both changes can be pushed to the remote repository "origin" with this command:

    git push origin master
    
In a browser go to the repository and verify that "myfile.txt" is there. While there you can go ahead and create a new pull request to get it merged to the "upstream" repository, that is the one in OpenAcademy-OpenStack organization.

Overtime your forked repository will get out of sync with the "upstream". It is, therefore, important to sync it from time to time. Here's how:

    git fetch upstream
    git merge upstream/master
    git push origin master
    
The first command brings in the latest from "upstream" repository. The second command merges all changes from the "master" branch in the upstream to the current local branch. And the last command pushes the new changes to the forked repository, thereby bringing it in sync with upstream.

There's much more to Git, but mastering those basic commands should suffice for now.




