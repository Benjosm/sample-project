# cli-project/cli/commands/env_commands.py
import os
import json
import click


@click.group()
def env():
    """Manages environment variables."""
    pass


@env.command()
@click.argument('key')
def get(key):
    """Gets the value of an environment variable."""
    value = os.environ.get(key)
    if value is not None:
        click.echo(value)
        exit(0)
    else:
        click.echo(f"Environment variable '{key}' not found.")
        exit(1)


@env.command()
@click.option('--format', type=click.Choice(['text', 'json']), default='text', help='Output format.')
def list(format):
    """Lists all environment variables."""
    if format == 'text':
        for key, value in os.environ.items():
            click.echo(f'{key}={value}')
    elif format == 'json':
        click.echo(json.dumps(dict(os.environ), indent=4))
    exit(0)
