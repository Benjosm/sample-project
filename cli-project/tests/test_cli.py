# cli-project/tests/test_cli.py
import pytest
from click.testing import CliRunner
from cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_runs_without_error(runner):
    result = runner.invoke(cli, [])
    assert result.exit_code == 0
    assert "A basic CLI tool." in result.output