# test_magic_square.py
import unittest
from magic_square import solve

class TestMagicSquare(unittest.TestCase):
    def test_solution(self):
        grid, s = solve()
        # magic sum should be 18
        self.assertEqual(s, 18)

        # check rows
        for row in grid:
            self.assertEqual(sum(row), 18)

        # check columns
        for c in range(3):
            self.assertEqual(sum(grid[r][c] for r in range(3)), 18)

        # check diagonals
        self.assertEqual(grid[0][0] + grid[1][1] + grid[2][2], 18)
        self.assertEqual(grid[0][2] + grid[1][1] + grid[2][0], 18)

if __name__ == "__main__":
    unittest.main()
