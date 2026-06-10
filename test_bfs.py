import unittest
from maze_solver_bfs import solve_bfs

class TestBFSSolving(unittest.TestCase):
    def setUp(self):
        self.solvable = [
            ["#", "S", "."],
            ["#", "#", "."],
            ["#", "#", "E"]
        ]
        self.unsolvable = [
            ["#", "S", "."],
            ["#", "#", "#"],
            ["#", "#", "E"]
        ]

    def test_bfs_success(self):
        self.assertTrue(solve_bfs(self.solvable))

    def test_bfs_fail(self):
        self.assertFalse(solve_bfs(self.unsolvable))

if __name__ == "__main__":
    unittest.main()