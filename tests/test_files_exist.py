# tests/test_files_exist.py
import os
import unittest

class TestFilesExist(unittest.TestCase):

    def test_index_html_exists(self):
        self.assertTrue(os.path.exists("index.html"))

    def test_style_css_exists(self):
        self.assertTrue(os.path.exists("style.css"))

    def test_script_js_exists(self):
        self.assertTrue(os.path.exists("script.js"))
