# cli-project/cli/commands/file_commands.py
import click
import os
import json

@click.group()
def file():
    """Manages files within the container."""
    pass

@file.command()
@click.argument('file_path', type=click.Path(exists=True))
def read(file_path):
    """Reads the content of a file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        click.echo(content)
        return 0
    except FileNotFoundError:
        click.echo('File not found', err=True)
        return 1
    except Exception as e:
        click.echo(f'An error occurred: {e}', err=True)
        return 1

@file.command()
@click.argument('file_path', type=click.Path())
@click.argument('content', required=True)
def write(file_path, content):
    """Writes content to a file."""
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        click.echo('Successfully wrote to {}'.format(file_path))
        return 0
    except Exception as e:
        click.echo(f'An error occurred: {e}', err=True)
        return 1

@file.command()
@click.argument('file_path', type=click.Path(exists=True))
def delete(file_path):
    """Deletes a file."""
    try:
        os.remove(file_path)
        click.echo('Successfully deleted {}'.format(file_path))
        return 0
    except FileNotFoundError:
        click.echo('File not found', err=True)
        return 1
    except Exception as e:
        click.echo(f'An error occurred: {e}', err=True)
        return 1

@file.command()
@click.argument('dir_path', type=click.Path(exists=True, file_okay=False))
@click.option('--json', is_flag=True, help='Output in JSON format.')
def list(dir_path, json):
    """Lists files in a directory."""
    try:
        files = os.listdir(dir_path)
        if json:
            click.echo(json.dumps(files))
        else:
            for file in files:
                click.echo(file)
        return 0
    except FileNotFoundError:
        click.echo('Directory not found', err=True)
        return 1
    except Exception as e:
        click.echo(f'An error occurred: {e}', err=True)
        return 1
