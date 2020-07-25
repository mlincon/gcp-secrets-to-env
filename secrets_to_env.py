import os
import re
import sys
import json
import click

@click.option('-f', '--file', required=True, help='Secrets JSON file', type=str)
@click.option('-p', '--prefix', required=False, help='Add a prefix to every environment variable', type=str)

@click.command()
def cli(file: str, prefix: str):
    re_file = re.sub(r'^(\.\.\/)+', '', file)
    click.echo(f'reading secrets from {re_file}')

    if sys.platform == 'linux':
        click.echo(f'Dectected OS: {sys.platform}')
        write_in_bashrc(file, prefix)

def write_in_bashrc(file: str, prefix: str):
    
    click.echo('Writing to bashrc')

    bashrc = open(os.path.join(os.environ.get('HOME'), '.bashrc'), 'a')

    with open(file) as client_secrets_json:
        secrets = json.load(client_secrets_json)
        for k, v in secrets['web'].items():
            click.echo(f'Creating env for: {k.upper()}')
    
            # write to .bashrc
            if prefix:
                entry = f'export {prefix}_{k.upper()}={v}\n'
            else:
                entry = f'export {k.upper()}={v}\n'

            bashrc.write(entry)
    
    bashrc.close()



# if __name__ == '__main__':
#     createEnvVariables(file)