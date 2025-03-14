# cli-project/tests/test_env_commands.py
import os
import json
import pytest
from click.testing import CliRunner
from cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_env_get_success(runner, monkeypatch):
    monkeypatch.setenv("TEST_VAR", "test_value")
    result = runner.invoke(cli, ["env", "get", "TEST_VAR"])
    assert result.exit_code == 0
    assert "test_value" in result.output


def test_env_get_not_found(runner):
    result = runner.invoke(cli, ["env", "get", "NON_EXISTENT_VAR"])
    assert result.exit_code == 1
    assert "Environment variable 'NON_EXISTENT_VAR' not found." in result.output


def test_env_list_text(runner, monkeypatch):
    monkeypatch.setenv("TEST_VAR1", "test_value1")
    monkeypatch.setenv("TEST_VAR2", "test_value2")
    result = runner.invoke(cli, ["env", "list"])
    assert result.exit_code == 0
    assert "TEST_VAR1=test_value1" in result.output
    assert "TEST_VAR2=test_value2" in result.output


def test_env_list_json(runner, monkeypatch):
    monkeypatch.setenv("TEST_VAR1", "test_value1")
    monkeypatch.setenv("TEST_VAR2", "test_value2")
    result = runner.invoke(cli, ["env", "list", "--format", "json"])
    assert result.exit_code == 0
    output = json.loads(result.output)
    assert "TEST_VAR1" in output
    assert output["TEST_VAR1"] == "test_value1"
    assert "TEST_VAR2" in output
    assert output["TEST_VAR2"] == "test_value2"
