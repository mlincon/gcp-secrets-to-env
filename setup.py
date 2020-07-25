# https://click.palletsprojects.com/en/7.x/setuptools/#setuptools-integration

from setuptools import setup

setup(
    name='gcp_secrets_to_env',
    version='0.1',
    py_modules=['secrets_to_env'],
    install_requires=['click'], #find_packages()
    entry_points='''
        [console_scripts]
        gcp_secrets_to_env=secrets_to_env:cli
    '''
)