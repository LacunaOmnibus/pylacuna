from setuptools import setup

setup(
    name='pylacuna',
    version='0.0.1',
    description='Calculates a study path for students.',
    url='https://github.com/miketwo/pylacuna',
    keywords="pylacuna students",
    packages=['pylacuna'],
    scripts=['bin/go.py'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description=open('README.md', 'r').read(),
    )
