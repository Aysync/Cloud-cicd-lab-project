import subprocess
import sys
import unittest


class TestApp(unittest.TestCase):

    def test_app_runs_and_prints(self):
        result = subprocess.run(
            [sys.executable, "app.py"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "Cloud CI Pipeline Running")


if __name__ == "__main__":
    unittest.main()
