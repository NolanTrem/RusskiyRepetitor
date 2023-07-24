from setuptools import setup

setup(
    name='russkiyrepetitor',
    version='0.1',
    packages=['russkiyrepetitor'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        russkiyrepetitor=russkiyrepetitor.cli.__main__:cli
    ''',
)
