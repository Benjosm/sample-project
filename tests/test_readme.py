# tests/test_readme.py

import os

def test_readme_exists():
    assert os.path.exists("README.md")