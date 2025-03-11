# tests/test_script.py
import pytest

# Assuming script.js exists and is linked in index.html

def test_script_exists():
    with open("script.js", "r") as f:
        assert f.read() is not None


def test_javascript_animation_present():
    # Placeholder for animation testing.  Inspect script.js content.
    try:
        with open("script.js", "r") as f:
            js_content = f.read()
        assert "animation" in js_content or "transition" in js_content
    except FileNotFoundError:
        pytest.fail("script.js not found")
