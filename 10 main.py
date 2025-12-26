grid = [
    [1, 4, 3, 2],
    [4, 2, 1, 3],
    [2, 3, 4, 1],
    [3, 1, 2, 4]
]

# Проверка (опционально)
def is_valid_latin_square(grid):
    n = len(grid)
    for i in range(n):
        if set(grid[i]) != set(range(1, n+1)):
            return False
        if set(grid[j][i] for j in range(n)) != set(range(1, n+1)):
            return False
    return True

# Выводим решение в формате, как в задании (по строкам, через пробелы)
for row in grid:
    print(' '.join(map(str, row)))