# cli-project/cli/cli.py
import click
from cli.commands.exec_command import exec_command

@click.group(name="cli")
def cli():
    """A simple CLI tool."""
    pass

cli.add_command(exec_command)

from cli.commands.file_commands import file
cli.add_command(file)

if __name__ == '__main__':
    cli()
