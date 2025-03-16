# cli-project/cli/cli.py
import click
from .commands import env_commands, exec_command, file_commands

@click.group()
def cli():
    pass

cli.add_command(env_commands.env)
cli.add_command(file_commands.file)
cli.add_command(exec_command.exec_command)

if __name__ == '__main__':
    cli()