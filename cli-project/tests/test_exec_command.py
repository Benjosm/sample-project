import pytest
from cli.cli import cli
from cli.commands import exec_command


@pytest.fixture
def mocker():
    from unittest.mock import Mock
    return Mock()


def test_exec_command(mocker):
    assert exec_command.exec_command is not None