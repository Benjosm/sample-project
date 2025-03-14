# cli-project/cli/cli.py
import click
from cli.commands.exec_command import exec_command

@click.group()
def cli():
    """A simple CLI tool."""
    pass

cli.add_command(exec_command)

if __name__ == '__main__':
    cli()
