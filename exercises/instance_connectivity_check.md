# Connectivity Check

## Problem Statement
From time to time network errors occur during the launch of an instance, and render it inaccessible, even when it shows up in Nova as active. One way to confirm that a newly launched instance is functional is to check that connection can be established to and from it.

## Requirements
Write a Python application that performs the following task:

1. Launch an instance.
2. Wait for it to come up.
3. Ping a well known IP (www.ebay.com, for example) from the instance.
4. Update the instance status to "failed" if the ping test isn't successful. 

Please submit code by end of Jan 30th.

## Setup

See [Getting Started Guide](https://github.com/OpenAcademy-OpenStack/project-docs) for instructions to set up your development environment.

## Discussions
- You'll need to make use of Python clients for Glance (to fetch images), and Nova (to launch instances).
- Boot with "ubuntu" image created as part of the [setup](https://github.com/OpenAcademy-OpenStack/project-docs)
- When launching an instance you can get a custom script (a.k.a user data) executed. This gives you the ability to perform additional configurations during boot time. You'll need to leverage this feature to perform the ping test. More information is available [here](http://docs.openstack.org/user-guide/content/user-data.html). 
- The result of the ping test can be extract from the [console log](http://docs.openstack.org/user-guide/content/novaclient_commands.html#novaclient_subcommand_console-log).

## Key Learning
- [Cloud Init](https://help.ubuntu.com/community/CloudInit)
- [User Data](http://docs.openstack.org/user-guide/content/user-data.html)

## Help
Use the email list openstack-open-academy-2014@googlegroups.com.




