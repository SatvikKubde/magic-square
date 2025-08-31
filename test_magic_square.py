import unittest
from magic_square import solve

class TestMagicSquare(unittest.TestCase):
    def test_solution_sum(self):
        grid, s = solve()
        # check magic sum
        self.assertEqual(s, 18)

    def test_rows(self):
        grid, s = solve()
        for row in grid:
            self.assertEqual(sum(row), 18)

    def test_columns(self):
        grid, s = solve()
        for c in range(3):
            self.assertEqual(sum(grid[r][c] for r in range(3)), 18)

    def test_diagonals(self):
        grid, s = solve()
        self.assertEqual(grid[0][0] + grid[1][1] + grid[2][2], 18)
        self.assertEqual(grid[0][2] + grid[1][1] + grid[2][0], 18)

if __name__ == "__main__":
    unittest.main()
