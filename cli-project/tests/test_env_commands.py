# cli-project/tests/test_env_commands.py
import pytest
from click.testing import CliRunner
from cli.cli import cli
import os


@pytest.fixture
def runner():
    return CliRunner()


def test_env_command_get(runner, monkeypatch):
    monkeypatch.setenv("MY_VAR", "my_value")
    result = runner.invoke(cli, ["env", "get", "MY_VAR"])
    assert result.exit_code == 0
    assert "my_value" in result.output


def test_env_command_set(runner, tmp_path, monkeypatch):
    # Test setting an environment variable
    result = runner.invoke(cli, ["env", "set", "NEW_VAR", "new_value"])
    assert result.exit_code == 0
    assert "Successfully set" in result.output
    assert os.environ.get("NEW_VAR") == "new_value"


def test_env_command_unset(runner, monkeypatch):
    monkeypatch.setenv("TEMP_VAR", "temp_value")
    result = runner.invoke(cli, ["env", "unset", "TEMP_VAR"])
    assert result.exit_code == 0
    assert "Successfully unset" in result.output
    assert os.environ.get("TEMP_VAR") is None