import pytest
from click.testing import CliRunner
from cli_project.cli import cli  # Corrected import


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_help(runner):
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'CLI tool for managing files' in result.output