# cli-project/tests/test_exec_command.py
import pytest
from click.testing import CliRunner
from cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_exec_command(runner):
    result = runner.invoke(cli, ["exec", "echo", "hello"])
    assert result.exit_code == 0
    assert "hello" in result.output


def test_exec_command_with_args(runner):
    result = runner.invoke(cli, ["exec", "echo", "hello world"])
    assert result.exit_code == 0
    assert "hello world" in result.output