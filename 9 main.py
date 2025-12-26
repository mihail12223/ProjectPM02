min_total = float('inf')

# Генерируем все перестановки чисел 1-9
from itertools import permutations

for perm in permutations(range(1, 10)):
    # Заполняем таблицу 3x3
    grid = [list(perm[i:i+3]) for i in range(0, 9, 3)]
    
    # Суммы четырех 2x2 квадратов
    sums = [
        grid[0][0] + grid[0][1] + grid[1][0] + grid[1][1],  # верхний левый
        grid[0][1] + grid[0][2] + grid[1][1] + grid[1][2],  # верхний правый
        grid[1][0] + grid[1][1] + grid[2][0] + grid[2][1],  # нижний левый
        grid[1][1] + grid[1][2] + grid[2][1] + grid[2][2]   # нижний правый
    ]
    
    total = sum(sums)
    if total < min_total:
        min_total = total

print(min_total)