# cli-project/tests/test_help_command.py
import pytest
from click.testing import CliRunner
from cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_help_command_general(runner):
    result = runner.invoke(cli, ["help"])
    assert result.exit_code == 0
    assert "Usage: cli" in result.output


def test_help_command_exec(runner):
    result = runner.invoke(cli, ["help", "exec"])
    assert result.exit_code == 0
    assert "Usage: cli exec" in result.output


def test_help_command_file(runner):
    result = runner.invoke(cli, ["help", "file"])
    assert result.exit_code == 0
    assert "Usage: cli file" in result.output


def test_help_command_env(runner):
    result = runner.invoke(cli, ["help", "env"])
    assert result.exit_code == 0
    assert "Usage: cli env" in result.output