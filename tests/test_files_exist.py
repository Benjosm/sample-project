# tests/test_files_exist.py

import pytest
import os

# Define the files to test
files_to_test = ["index.html", "script.js", "style.css"]


@pytest.mark.parametrize("file_name", files_to_test)
def test_files_exist(file_name):
    """Test that the specified files exist in the project root."""
    assert os.path.exists(file_name), f"{file_name} does not exist."
