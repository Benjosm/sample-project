import pytest
from click.testing import CliRunner
from cli.cli import cli  # Corrected import


@pytest.fixture
def runner():
    return CliRunner()


def test_env_commands(runner):
    # Add your test cases here
    pass