import os
import re
import sys
import json
import click

@click.option('-j', '--json_file', required=True, help='Secrets JSON file', type=str)
@click.option('-p', '--prefix', required=False, help='Add a prefix to every env variable', type=str)
@click.option('-f', '--save_file', required=True, help='The shell initialization file', type=str)
@click.option('-c', '--export_cmd', required=False, help='Whether any cmd should be used, default is "export"', type=str)

@click.command()
def cli(json_file: str, prefix: str, save_file: str, export_cmd: str) -> None:
    re_file = re.sub(r'^(\.\.\/)+', '', json_file)
    click.echo(f'reading secrets from {re_file}')

    os = sys.platform
    if os == 'linux':
        click.echo(f'dectected OS: {os}')
        create_env_linux(json_file, prefix, save_file, export_cmd)
    
    if os.startswith('win'):
        create_env_windows()


def create_env_linux(json_file: str, prefix: str, save_file: str, export_cmd: str=None) -> None:
    
    click.echo(f'writing to {save_file}')

    env_file = open(os.path.join(os.environ.get('HOME'), save_file), 'a')

    env_file.write('\n\n')
    with open(json_file) as client_secrets_json:
        secrets = json.load(client_secrets_json)
        for k, v in secrets['web'].items():
            
            # https://unix.stackexchange.com/a/117470
            set_keyword = export_cmd if export_cmd is not None else 'export'
            entry = f'{set_keyword} {prefix}_{k.upper()}="{v}"'.strip() + '\n'

            env_file.write(entry)

            try:
                env_name = entry.split()[1].split('=')[0]
            except:
                env_name = entry.split('=')[0]
            click.echo(f'created env {env_name} for parameter {k}')
    
    env_file.close()


def create_env_windows():
    click.echo('Not yet implemented')