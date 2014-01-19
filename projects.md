
This is work in progress.

1. Multi-factor authentication for Keystone
  - Define an API extension to Keystone
  - Inject an API extension into Keystone
  - Create a default implementation
  - Write unit tests
  - Extend the CLI
  - Add an extension to Horizon
2. Access keys for Keystone including the user experience
  - Define an API extension to Keystone
  - Inject an API extension into Keystone
  - Create a default implementation
  - Write unit tests
  - Extend the CLI
  - Add an extension to Horizon
3. Instance cleanup from nova
  - Set multi-node node devstack
  - Create orphan data in nova database
  - Create a bot to clean orphans
4. Instance cleanup from hypervisors
  - Set a multi-node node devstack
  - Delete VM from database
  - Now clean up VMs
5. Nova Scheduler is O(n). How can you improve it?
  - Analyze nova scheduler performance
  - Use a multi-node devstack setup
  - Propos one or more solutions to improve performance.
  - Implement at least one solution.
6. Keystone split RO/RW access
  - Refactor such that Keystone can be used used in read-only mode against a read-only slave database
  - Implement unit tests.

