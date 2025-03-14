# cli-project/cli/commands/exec_command.py
import click
import subprocess
import json

@click.command()
@click.argument('command', type=str)
def exec_command(command):
    """Executes a shell command."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        output = {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }
        click.echo(json.dumps(output))
    except subprocess.CalledProcessError as e:
        output = {
            "stdout": e.stdout.strip() if e.stdout else "",
            "stderr": e.stderr.strip() if e.stderr else e.output.strip(),
            "returncode": e.returncode
        }
        click.echo(json.dumps(output))
        raise click.exceptions.Exit(e.returncode)
    except FileNotFoundError as e:
        output = {
            "stdout": "",
            "stderr": str(e),
            "returncode": 127
        }
        click.echo(json.dumps(output))
        raise click.exceptions.Exit(127)
    except Exception as e:
        output = {
            "stdout": "",
            "stderr": str(e),
            "returncode": 1
        }
        click.echo(json.dumps(output))
        raise click.exceptions.Exit(1)
