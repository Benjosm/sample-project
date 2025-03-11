# tests/test_file_operations.py
import os
import pytest

# Helper function to create a test file
def create_test_file(filepath, content=""):
    try:
        with open(filepath, "w") as f:
            f.write(content)
    except Exception as e:
        pytest.fail(f"Failed to create test file: {e}")

# Helper function to delete a test file
def delete_test_file(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        pass # File might not exist, which is fine for cleanup
    except Exception as e:
        pytest.fail(f"Failed to delete test file: {e}")


@pytest.fixture(autouse=True)
def cleanup_test_files():
    # Cleanup any test files before and after each test
    test_files = ["test_file.txt", "test_file_with_content.txt"]
    for file in test_files:
        delete_test_file(file)
    yield
    for file in test_files:
        delete_test_file(file)



def test_create_file():
    filepath = "test_file.txt"
    create_test_file(filepath)
    assert os.path.exists(filepath)


def test_write_to_file():
    filepath = "test_file_with_content.txt"
    content = "Hello, world!"
    create_test_file(filepath, content)
    with open(filepath, "r") as f:
        # Intentionally fail the test
        assert f.read() == "wrong content"


def test_read_from_file():
    filepath = "test_file_with_content.txt"
    content = "Initial content"
    create_test_file(filepath, content)
    with open(filepath, "r") as f:
        assert f.read() == content