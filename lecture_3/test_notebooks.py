"""Offline preflight checks for Lecture 3 notebooks (no LLM server required).

Run from repository root:
    python -m unittest discover -s lecture_3 -p 'test_*.py' -v
"""
import ast
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


def notebook(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def sources(name):
    return [
        "".join(cell.get("source", []))
        for cell in notebook(name)["cells"]
        if cell["cell_type"] == "code"
    ]


def combined_source(name):
    return "\n\n".join(sources(name))


class Lecture3NotebookTests(unittest.TestCase):
    def test_all_code_cells_parse(self):
        for filename in ("seminar_3.ipynb", "hw_2.ipynb"):
            for i, source in enumerate(sources(filename)):
                with self.subTest(filename=filename, code_cell=i):
                    ast.parse(source, filename=f"{filename}:cell_{i}")

    def test_cat_reply_unknown_is_handled(self):
        tree = ast.parse(combined_source("seminar_3.ipynb"))
        fn = next(
            node for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name == "cat_reply"
        )
        namespace = {}
        exec(compile(ast.Module(body=[fn], type_ignores=[]), "<cat_reply>", "exec"), namespace)
        for need in ("unknown", "hungry", "play"):
            with self.subTest(need=need):
                result = namespace["cat_reply"](
                    {"need": need, "food": "salmon", "messages": ["hi"]}
                )
                self.assertGreater(len(result["messages"]), 1)
                self.assertIsInstance(result["messages"][-1], str)
        self.assertEqual(
            namespace["cat_reply"](
                {"need": "unknown", "messages": ["hi"]}
            )["need"], "unknown"
        )

    def test_seminar_tool_message_history(self):
        code = combined_source("seminar_3.ipynb")
        self.assertIn('HumanMessage("Мяу. Хочу есть"), ai_message', code)
        self.assertIn("ToolMessage(", code)

    def test_homework_tool_decorates_inner_function(self):
        tree = ast.parse(combined_source("hw_2.ipynb"))
        factory = next(
            node for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name == "make_solve_math_problem_tool"
        )
        self.assertEqual(factory.decorator_list, [])
        inner = next(
            node for node in factory.body
            if isinstance(node, ast.FunctionDef)
            and node.name == "solve_math_problem"
        )
        self.assertTrue(inner.decorator_list)

    def test_homework_retry_wraps_a_chain(self):
        code = combined_source("hw_2.ipynb")
        self.assertIn("timeout_until_attempt(k=2, chain=chain)", code)
        self.assertIn("retry_if_exception_type=(TimeoutError,)", code)
        self.assertNotIn("RunnableLambda(timeout_until_attempt(3))", code)


if __name__ == "__main__":
    unittest.main()
