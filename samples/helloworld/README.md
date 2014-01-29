## Sample OpenStack Project
### Introduction
This project serves as an example of a typical OpenStack project. It demonstrates the following:

1. Reading configurations from a file.
2. Logging to a file.
3. Starting and stopping a service.
4. Using Nova Python client to get a list of flavors.
5. Leveraging "setup" to bring in dependencies.

### Setup
1. Create a virtual environment.
2. Clone the code.
3. Copy **etc/helloworld.conf.sample** to **etc/helloworld.conf** and update it with the correct credentials.
3. In **samples/helloworld** folder, run:

        python setup.py develop
    
4. Finally start the service with:

        helloworld
    
### Create Your Own Project
1. Copy everything except helloworld/openstack directory.
2. Rename "helloworld" to something more relevant to your project.
3. See [Oslo](https://wiki.openstack.org/wiki/Oslo#Syncing_Code_from_Incubator) for instructions to copy certain modules from the Oslo project. **openstack-common.conf** file dictates which modules to copy. Update it as necessary.
4. Chances are you'll make use of other Python modules in your project. Make sure to update **tools/pip-requires** with packages required by your project.



