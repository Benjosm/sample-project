# tests/test_index_html.py

import pytest
import os

# Assuming index.html contains the title "Worm Game"

def test_index_html_has_title():
    """Test that index.html contains the title "Worm Game""""
    with open("index.html", "r") as f:
        content = f.read()
        assert "<title>Worm Game</title>" in content, "index.html does not contain the title 'Worm Game'"
