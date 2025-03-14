# cli-project/tests/test_exec_command.py
import pytest
import subprocess
import json
from cli_project.cli.commands.exec_command import run_command


@pytest.fixture
def mock_subprocess_run(mocker):
    return mocker.patch("subprocess.run")



def test_exec_command_basic(mock_subprocess_run):
    run_command("ls")
    mock_subprocess_run.assert_called_once()
    assert mock_subprocess_run.call_args[0][0][0] == "ls"


def test_exec_command_with_args(mock_subprocess_run):
    run_command("ls", "-l", "-a")
    mock_subprocess_run.assert_called_once()
    assert mock_subprocess_run.call_args[0][0] == ["ls", "-l", "-a"]


def test_exec_command_file_not_found(mock_subprocess_run):
    mock_subprocess_run.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError):
        run_command("nonexistent_command")


def test_exec_command_called_process_error(mock_subprocess_run):
    mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, "cmd", output=b'error output')
    with pytest.raises(subprocess.CalledProcessError):
        run_command("some_command")


def test_exec_command_success_json_output(mock_subprocess_run, mocker):
    mock_subprocess_run.return_value.stdout = b'{"result": "success"}'
    mocker.patch('json.loads', return_value={'result': 'success'})
    result = run_command("ls", json_output=True)
    assert result == {'result': 'success'}


def test_exec_command_error_json_output(mock_subprocess_run, mocker):
    mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, "cmd", output=b'error output')
    mocker.patch('json.loads', side_effect=json.JSONDecodeError("", "", 0))
    with pytest.raises(subprocess.CalledProcessError):
        run_command("ls", json_output=True)
