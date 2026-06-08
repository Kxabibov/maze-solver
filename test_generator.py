import unittest
from maze_generator import create_maze

class TestGeneratorProperties(unittest.TestCase):
    def test_dimensions(self):
        maze = create_maze(10, 10) # Checks odd formatting normalization
        self.assertEqual(len(maze), 11)
        self.assertEqual(len(maze[0]), 11)
        self.assertEqual(maze[1][0], "S")
        self.assertEqual(maze[9][10], "E")

if __name__ == "__main__":
    unittest.main()