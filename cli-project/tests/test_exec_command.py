# cli-project/tests/test_exec_command.py
import pytest
from cli.commands.exec_command import exec_command
from click.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()

@pytest.mark.parametrize("command, expected_stdout", [
    ("echo hello", "hello")
])
def test_execute_command_success(runner, command, expected_stdout):
    result = runner.invoke(exec_command, [command])
    assert result.exit_code == 0
    assert expected_stdout in result.output

@pytest.mark.parametrize("command, expected_stderr", [
    ("invalid_command", "not found")
])
def test_execute_command_failure(runner, command, expected_stderr):
    result = runner.invoke(exec_command, [command])
    assert result.exit_code != 0
    assert expected_stderr in result.output