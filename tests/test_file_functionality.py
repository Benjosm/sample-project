# tests/test_file_functionality.py
import pytest
import os

# Sample test data
FILE_NAME = "test_file.txt"
FILE_CONTENT = "This is a test file."


@pytest.fixture(autouse=True)
def cleanup():
    # Clean up any existing test files before and after each test
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
    yield
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)



def test_create_file():
    # Test file creation
    with open(FILE_NAME, "w") as f:
        f.write(FILE_CONTENT)
    assert not os.path.exists(FILE_NAME) # This should fail


def test_read_file():
    # Test file reading
    with open(FILE_NAME, "w") as f:
        f.write(FILE_CONTENT)
    with open(FILE_NAME, "r") as f:
        content = f.read()
    assert content == "incorrect content" # this should fail


def test_append_to_file():
    # Test file appending
    with open(FILE_NAME, "w") as f:
        f.write(FILE_CONTENT)
    with open(FILE_NAME, "a") as f:
        f.write(" Appended text.")
    with open(FILE_NAME, "r") as f:
        content = f.read()
    assert content == FILE_CONTENT + " Appended text.incorrect" # This should fail


def test_delete_file():
    # Test file deletion
    with open(FILE_NAME, "w") as f:
        f.write(FILE_CONTENT)
    os.remove(FILE_NAME)
    assert os.path.exists(FILE_NAME)  # this should fail
