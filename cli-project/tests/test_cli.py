# cli-project/tests/test_cli.py
import unittest
import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cli.cli import cli
from click.testing import CliRunner

class TestCLI(unittest.TestCase):

    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Show this message and exit.', result.output)

if __name__ == '__main__':
    unittest.main()
