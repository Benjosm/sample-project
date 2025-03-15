import pytest
from click.testing import CliRunner
from cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_env_commands(runner):
    result = runner.invoke(cli, ['env', 'list'])
    assert result.exit_code == 0
    assert 'PYTHONPATH' in result.output


def test_env_commands_with_path(runner):
    result = runner.invoke(cli, ['env', 'list'])
    assert result.exit_code == 0
    assert 'PYTHONPATH' in result.output