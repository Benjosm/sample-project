# test/test_plan_reader.py
import unittest
from src.plan_reader import parse_plan


class TestPlanReader(unittest.TestCase):

    def test_empty_plan(self):
        plan_text = ""
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, [])

    def test_single_task(self):
        plan_text = "Task: Implement feature X"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Implement feature X"])

    def test_multiple_tasks(self):
        plan_text = """
Task: Implement feature X
Task: Write tests
"""
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Implement feature X", "Write tests"])

    def test_step_task(self):
        plan_text = "Step: Refactor code"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Refactor code"])

    def test_numbered_list_task(self):
        plan_text = "1. Deploy to production"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Deploy to production"])

    def test_handles_extra_whitespace(self):
        plan_text = "Task:   Clean up   "
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Clean up"])

if __name__ == '__main__':
    unittest.main()