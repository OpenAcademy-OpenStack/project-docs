# Python Client App

In this exercise you will exercise the following OpenStack APIs

- Keystone for identity
- Glance for images
- Nova for VMs.

The instructions below assume that you are using a Mac for your development.

Please submit code by end of Jan 30th. In case of questions,
use the email list openstack-open-academy-2014@googlegroups.com.


## Preparation

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

## Manual Verification

First download the settings to use OpenStack command line interface (CLI)
tools. Here is how.

1. Login to the dashboard with username `admin` and password `password`.
2. Click on the 'Project' tab.
3. Create a VM. Then click on the VM. Switch to the Console tab. You should be
   able to login to verify. Note that we're not going to focus on networking
   aspects in this project and hence do not expect to use the VMs for anything
   other than testing OpenStack functionality.
4. Switch Access and Security link. Click on API Access tab. Click on "Download
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

You will notice that the CLI makes HTTP requests to OpenStack APIs. Study the
 sequence of requests, request and response headers and bodies.

## Exercise

Write a python app to query the list of images containing name `ubuntu`, and create a VM of the image.

For this exercise I suggest the following approach:

1. Setup a Python virtual environment in your Mac.
2. Instance python-glanceclient, python-novaclient and python-keystoneclient
in to your virtual enviroment. Use `pip install {package}` to install.







