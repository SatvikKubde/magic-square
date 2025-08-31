# magic_square.py

def solve():
    # Derived solution for given partially-filled 3x3
    # Grid:
    # 5 _ _
    # _ 6 2
    # 3 8 _
    #
    # Unique integer solution exists.
    d = 10
    a = d - 6
    b = d - 1
    c = d - 3
    grid = [
        [5, a, b],
        [d, 6, 2],
        [3, 8, c],
    ]
    return grid, 5 + a + b

if __name__ == "__main__":
    grid, s = solve()
    print("Magic Square Solution (Sum =", s, ")")
    for row in grid:
        print(row)

