# cli-project/cli/cli.py
import click

@click.group()
def cli():
    """A basic CLI tool."""
    pass

if __name__ == '__main__':
    cli()