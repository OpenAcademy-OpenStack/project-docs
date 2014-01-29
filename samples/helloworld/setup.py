from setuptools import setup, find_packages
from helloworld.openstack.common import setup as common_setup

install_requires = common_setup.parse_requirements(['tools/pip-requires'])
tests_require = common_setup.parse_requirements(['tools/test-requires'])
setup_require = common_setup.parse_requirements(['tools/setup-requires'])
dependency_links = common_setup.parse_dependency_links([
    'tools/pip-requires',
    'tools/test-requires',
    'tools/setup-requires'
])

setup(
    name='helloworld',
    version='0.0.1',
    description='I just call to say .... helloworld',
    author='OpenAcademy',
    url='https://github.com/OpenAcademy-OpenStack/project-docs/samples/helloworld',
    packages=find_packages(exclude=['bin']),
    include_package_data=True,
    test_suite='nose.collector',
    setup_requires=setup_require,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    dependency_links=dependency_links,
    scripts=[
        'bin/helloworld',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: System :: Systems Administration',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: OpenStack',
    ],
)
