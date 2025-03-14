import pytest
from click.testing import CliRunner
from cli_project.cli import cli  # Corrected import


@pytest.fixture
def runner():
    return CliRunner()


def test_exec_command(runner):
    # Add your test cases here
    pass