# cli-project/tests/test_file_commands.py
import pytest
from click.testing import CliRunner
from cli.cli import cli  # Import the main CLI object


runner = CliRunner()

def test_read_file_not_found():
    result = runner.invoke(cli, ['file', 'read', 'nonexistent_file.txt'])
    assert result.exit_code == 1
    assert 'File not found' in result.output
