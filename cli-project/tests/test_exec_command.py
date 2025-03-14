# cli-project/tests/test_exec_command.py
import json
import pytest
from click.testing import CliRunner
from cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_exec_command_success(runner):
    result = runner.invoke(cli, ['exec', 'echo hello'])
    assert result.exit_code == 0
    assert "hello" in result.output


def test_exec_command_failure(runner):
    result = runner.invoke(cli, ['exec', 'invalid_command'])
    assert result.exit_code != 0
    assert "No such file or directory" in result.output
