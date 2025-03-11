# tests/test_script.py
import pytest
from script import get_worm_container


def test_worm_container_exists():
    # Assuming a function get_worm_container() is defined in script.js
    # and returns the element.  This function does not yet exist, so
    # the test should fail.
    try:
        worm_container = get_worm_container()
        assert worm_container is not None
    except NameError:
        pytest.fail("get_worm_container function not defined.")
