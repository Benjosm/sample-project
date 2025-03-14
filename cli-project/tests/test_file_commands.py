import os
import shutil
import pytest
from click.testing import CliRunner
from cli import cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def test_file_path(tmp_path):
    return tmp_path / "test_file.txt"


@pytest.fixture
def test_dir_path(tmp_path):
    return tmp_path / "test_dir"


def create_test_file(file_path, content="test content"):
    with open(file_path, "w") as f:
        f.write(content)


def create_test_dir(dir_path):
    os.makedirs(dir_path)


@pytest.fixture(autouse=True)
def cleanup(tmp_path):
    yield
    # Clean up the temporary directory after each test
    shutil.rmtree(tmp_path)



def test_file_read_success(runner, test_file_path):
    create_test_file(test_file_path)
    result = runner.invoke(cli, ["file", "read", str(test_file_path)])
    assert result.exit_code == 0, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert result.output.strip() == "test content"


def test_file_read_file_not_found(runner, test_file_path):
    result = runner.invoke(cli, ["file", "read", str(test_file_path)])
    assert result.exit_code == 1, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert "File not found" in result.stderr


def test_file_write_success(runner, test_file_path):
    result = runner.invoke(cli, ["file", "write", str(test_file_path), "new content"])
    assert result.exit_code == 0, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert "Successfully wrote" in result.output
    with open(test_file_path, "r") as f:
        assert f.read() == "new content"


def test_file_delete_success(runner, test_file_path):
    create_test_file(test_file_path)
    result = runner.invoke(cli, ["file", "delete", str(test_file_path)])
    assert result.exit_code == 0, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert "Successfully deleted" in result.output
    assert not os.path.exists(test_file_path)


def test_file_delete_file_not_found(runner, test_file_path):
    result = runner.invoke(cli, ["file", "delete", str(test_file_path)])
    assert result.exit_code == 1, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert "File not found" in result.stderr


def test_file_list_success_text(runner, test_dir_path):
    create_test_dir(test_dir_path)
    create_test_file(os.path.join(test_dir_path, "file1.txt"))
    create_test_file(os.path.join(test_dir_path, "file2.txt"))
    result = runner.invoke(cli, ["file", "list", str(test_dir_path)])
    assert result.exit_code == 0, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert "file1.txt" in result.output
    assert "file2.txt" in result.output


def test_file_list_success_json(runner, test_dir_path):
    create_test_dir(test_dir_path)
    create_test_file(os.path.join(test_dir_path, "file1.txt"))
    create_test_file(os.path.join(test_dir_path, "file2.txt"))
    result = runner.invoke(cli, ["file", "list", str(test_dir_path), "--json"])
    assert result.exit_code == 0, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert '["file1.txt", "file2.txt"]' in result.output.strip()


def test_file_list_dir_not_found(runner, test_dir_path):
    result = runner.invoke(cli, ["file", "list", str(test_dir_path)])
    assert result.exit_code == 1, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert "Directory not found" in result.stderr



def test_file_write_no_content(runner, test_file_path):
    result = runner.invoke(cli, ["file", "write", str(test_file_path)])
    assert result.exit_code == 2, f"Exit code: {result.exit_code}\nStderr: {result.stderr}"
    assert "Error: Missing argument 'content'" in result.stderr