# test/test_plan_reader.py
import unittest
from src.plan_reader import parse_plan

class TestPlanReader(unittest.TestCase):

    def test_parse_plan_single_task(self):
        plan_text = "- Task 1"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Task 1"])

    def test_parse_plan_multiple_tasks(self):
        plan_text = "- Task 1\n- Task 2\n- Task 3"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Task 1", "Task 2", "Task 3"])

    def test_parse_plan_with_leading_spaces(self):
        plan_text = "  - Task 1"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Task 1"])

    def test_parse_plan_with_numbered_list(self):
        plan_text = "1. Task 1"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Task 1"])

    def test_parse_plan_empty_plan(self):
        plan_text = ""
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, [])

    def test_parse_plan_with_empty_lines(self):
        plan_text = "- Task 1\n\n- Task 2"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Task 1", "Task 2"])

    def test_parse_plan_different_formats(self):
        plan_text = "- Task 1\n- Task 2\n  - Task 3\n1. Task 4"
        tasks = parse_plan(plan_text)
        self.assertEqual(tasks, ["Task 1", "Task 2", "Task 3", "Task 4"])
