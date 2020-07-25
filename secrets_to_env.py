import os
import re
import sys
import json
import click

@click.option('-j', '--json_file', required=True, help='Secrets JSON file', type=str)
@click.option('-p', '--prefix', required=False, help='Add a prefix to every env variable', type=str)

@click.command()
def cli(json_file: str, prefix: str) -> None:
    re_file = re.sub(r'^(\.\.\/)+', '', json_file)
    click.echo(f'reading secrets from {re_file}')

    os = sys.platform
    if os == 'linux':
        click.echo(f'dectected OS: {os}')
        create_env_linux(json_file, prefix)
    
    if os.startswith('win'):
        create_env_windows()


def create_env_linux(json_file: str, prefix: str) -> None:
    
    click.echo('writing to bashrc')

    bashrc = open(os.path.join(os.environ.get('HOME'), '.bashrc'), 'a')

    bashrc.write('\n\n')
    with open(json_file) as client_secrets_json:
        secrets = json.load(client_secrets_json)
        for k, v in secrets['web'].items():
    
            # write to .bashrc
            if prefix:
                entry = f'{prefix}_{k.upper()}="{v}"\n'
            else:
                entry = f'{k.upper()}="{v}"\n'

            bashrc.write(entry)

            env_name = entry.split('=')[0]
            click.echo(f'created env {env_name} for parameter {k}')
    
    bashrc.close()


def create_env_windows():
    click.echo('Not yet implemented')