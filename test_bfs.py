import unittest
from maze_solver_dfs import solve_dfs

class TestDFSSolving(unittest.TestCase):
    def setUp(self):
        self.solvable = [
            ["#", "S", "#"],
            ["#", ".", "#"],
            ["#", ".", "E"]
        ]
        self.unsolvable = [
            ["#", "S", "#"],
            ["#", "#", "#"],
            ["#", ".", "E"]
        ]

    def test_dfs_success(self):
        self.assertTrue(solve_dfs(self.solvable))

    def test_dfs_fail(self):
        self.assertFalse(solve_dfs(self.unsolvable))

if name == "main":
    unittest.main()