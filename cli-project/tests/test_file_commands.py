# cli-project/tests/test_file_commands.py
import pytest
from click.testing import CliRunner
from cli.cli import cli
import os

@pytest.fixture
def runner():
    return CliRunner()


def test_file_command_read(runner, tmp_path):
    # Create a temporary file
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("file content")

    # Read the file using the command
    result = runner.invoke(cli, ["file", "read", str(file_path)])
    assert result.exit_code == 0
    assert "file content" in result.output


def test_file_command_write(runner, tmp_path):
    # Write to a temporary file
    file_path = tmp_path / "test_write.txt"
    result = runner.invoke(cli, ["file", "write", str(file_path), "new content"])
    assert result.exit_code == 0
    assert "Successfully wrote" in result.output
    assert file_path.read_text() == "new content"


def test_file_command_delete(runner, tmp_path):
    # Create a temporary file
    file_path = tmp_path / "test_delete.txt"
    file_path.write_text("delete content")

    # Delete the file using the command
    result = runner.invoke(cli, ["file", "delete", str(file_path)])
    assert result.exit_code == 0
    assert "Successfully deleted" in result.output
    assert not file_path.exists()


def test_file_command_list(runner, tmp_path):
    # Create some temporary files
    file1_path = tmp_path / "file1.txt"
    file1_path.write_text("content1")
    file2_path = tmp_path / "file2.txt"
    file2_path.write_text("content2")

    # List files in the directory using the command
    result = runner.invoke(cli, ["file", "list", str(tmp_path)])
    assert result.exit_code == 0
    assert "file1.txt" in result.output
    assert "file2.txt" in result.output