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

**origin** refers to the forked repository. Let's add the **upstream** repository as well:

    git remote add upstream https://github.com/OpenAcademy-OpenStack/playground.git
    git remote -v
    
There should be two remote repositories:

    origin	git@github.com:<your-repository>/playground.git (fetch)
    origin	git@github.com:<your-repository>/playground.git (push)
    upstream	https://github.com/OpenAcademy-OpenStack/playground.git (fetch)
    upstream	https://github.com/OpenAcademy-OpenStack/playground.git (push)
    
Next add a file or modify an existing one:

    echo "Adding a new file" > myfile.txt
    
*git status* commmand should list "myfile.txt" as *untracked*. It can be added via this command:

    git add myfile.txt
    
Next commit this change to the local repository with:

    git commit -m "my first commit"
    
Let's add another line to "myfile.txt" and modify the first commit to include this change:

    echo "\nThis is another line" >> myfile.txt
    git add myfile.txt
    git commit --amend
    
Modify the message as necessary and commit the change. Both changes can be pushed to the remote repository "origin" with this command:

    git push origin master
    
In a browser go to the repository and verify that "myfile.txt" is there. While there you can go ahead and create a new pull request to get it merged to the **upstream** repository, that is the one in OpenAcademy-OpenStack organization.

Overtime your forked repository will get out of sync with the **upstream**. It is, therefore, important to sync it from time to time. Here's how:

    git fetch upstream
    git merge upstream/master
    git push origin master
    
The first command brings in the latest from **upstream** repository. The second command merges all changes from the **master** branch in the upstream to the current local branch. And the last command pushes the new changes to the forked repository, thereby bringing it in sync with upstream.

There's much more to Git, but mastering those basic commands should suffice for now.


Python
------
Python is the language of choice for OpenStack. You're expected to code in Python for the project.

Python isn't hard to learn. However, it takes some time to write *Pythonic* code. For example, here's a piece of code that is *translated* from some other languages to Python:

    languages = ["james", "john", "josh", "jay"]
    found = False
    for l in languages:
        if l.find("ay") >= 0:
            found = True
    if found:
        print("Found a name that contains 'ay'")
        
Here's the *pythonic" version:

    if [l for l in languages if "ay" in l]:
        print("Found a name that contains 'ay'")
        
If you marvel at the second version, you're in for a good ride. If not, it's just a matter of time. Here's a book that we've found useful, https://www.jeffknupp.com/writing-idiomatic-python-ebook-experiment. There are many other more out there.

We also recommend using [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

As for IDE, [PyCharm](http://www.jetbrains.com/pycharm/download/index.html) is a good one, and there's a free community version. Regardless of which IDE you use, the expectation is that you follow the [Style Guide for Python Code](http://www.python.org/dev/peps/pep-0008/). It makes the code readable, and helps tremendously with code review.


Devstack
--------
For this project you'll need access to a cloud environment. **devstack** is basically cloud-in-a-box. It deploys all OpenStack components and gives you your very own cloud deployment. You'll be testing your code against **devstack**.

### Install Devstack with Vagrant

Install [virtualbox](https://www.virtualbox.org/wiki/Downloads)

Install [vagrant](http://downloads.vagrantup.com/)

Download vagrant box

```
vagrant box add base http://files.vagrantup.com/precise64.box
```

Use the following `Vagrantfile` to launch a vagrant VM

```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.network :private_network, ip: "192.168.50.4"
  config.vm.provider "virtualbox" do |vm|
    vm.customize ["modifyvm", :id, "--memory", 8192]
  end
end
```

Use `vagrant ssh` to login to VM.

Setup devstack using the following commands.

```
sudo apt-get update -y
sudo apt-get install git-core -y
git clone https://github.com/openstack-dev/devstack.git
cd devstack
git checkout stable/havana
```

Create a `localrc` file.

```
DATABASE_PASSWORD=password
RABBIT_PASSWORD=password
SERVICE_TOKEN=password
SERVICE_PASSWORD=password
ADMIN_PASSWORD=password
```

and run

```
./stack.sh
```

From your Mac, go to `http://192.168.50.4`. You should see OpenStack
dashboard (called Horizon).

### Manual Verification

First download the settings to use OpenStack command line interface (CLI)
tools. Here is how.

1. Login to the dashboard with username `admin` and password `password`.
2. Click on the "Project" tab.
3. Create a VM. Then click on the VM. Switch to the "Console" tab. You should be
   able to login to verify. Note that we're not going to focus on networking
   aspects in this project and hence do not expect to use the VMs for anything
   other than testing OpenStack functionality.
4. Click on "Access and Security" link and then on the "API Access" tab. Click on "Download
   OpenStack RC File" to download a script with settings. Copy this file to
   your vagrant VM.
5. Load these settings via `source demo-openrc.sh`. Enter `password`.

Add a new image.

1. Download the file `http://cloud-images.ubuntu.com/releases/12.04.2/release/ubuntu-12.04-server-cloudimg-amd64-disk1.img`
2. Upload the image via `glance image-create --name ubuntu
--disk-format=qcow2 --container-format=bare --is-public=True --file=./ubuntu-12.04-server-cloudimg-amd64-disk1.img`
3. Run `glance index` and note the UUID of the image you uploaded.
4. Create a VM via `nova boot --image {image UUID} --flavor m1.small myubuntu`
5. Wait for a minute or so and then run `nova list` to see the new VM listed.

Then run the following commands in debug mode.

1. `glance --debug index`
2. `nova --debug list`
3. `nova --debug show {UUID of the VM}`

You will notice that the CLI makes HTTP requests to OpenStack APIs. Study the sequence of requests, request and response headers and bodies.

Project Structure
-----------------
More to come

Exercises
==========

Browse the *exercises* folder for various exercises that you can pick up.




