# cli-project/tests/test_cli.py
import pytest
from click.testing import CliRunner
from cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_help(runner):
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage: cli" in result.output