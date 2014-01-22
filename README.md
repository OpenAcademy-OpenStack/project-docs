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
    
