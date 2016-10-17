# python setup.py install
# or
# python setup.py develop
# You may need to be root

from setuptools import setup, find_packages
setup(
    name = "pyReactor",
    version = "0.1",
    packages = find_packages(),
    #scripts = ['main.py'],
    install_requires = ['numpy>=1.7.0', 'scipy>=0.12.0', 'matplotlib>=1.2.1', 'pyserial'],
    package_data = { '': ['*.txt'] },
    author = 'William Gurecky',
    license = "MIT",
    author_email = "william.gurecky@gmail.com",

    # set primary console script up
    entry_points = {
        'console_scripts': [
            'pyReactor = legoReactor:main'
        ]
    }
)

