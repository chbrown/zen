from setuptools import setup

setup(
    name='sanity',
    version='0.0.1',
    # description='Pretty python evangelization',
    # author='Christopher Brown',
    # author_email='io@henrian.com',
    # url='https://github.com/chbrown/zen',
    packages=['styling'],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'run-sanity-example = styling:main',
        ],
    }
)
