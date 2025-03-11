# tests/test_script.py

import pytest

# Assuming script.js should have some comments


def test_script_has_comments():
    with open("script.js", "r") as f:
        content = f.read()
        assert "//" in content or "/*" in content, "script.js should contain comments (// or /* */)"
