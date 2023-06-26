"""

"""

def spiral(n: int, m: int) -> list:
    arr = [[0] * m for _ in range(n)]
    row, row_delta, col, col_delta = 0, 0, 0, 1

    for num in range(1, n * m + 1):
        arr[row][col] = num

        if arr[(row + row_delta) % n][(col + col_delta) % m]:
            row_delta, col_delta = col_delta, -row_delta

        row += row_delta
        col += col_delta

    return arr

if __name__ == '__main__':
    pass