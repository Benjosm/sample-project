import pytest
from click.testing import CliRunner
from cli.cli import cli  # Corrected import


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_help(runner):
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'A simple CLI tool' in result.output