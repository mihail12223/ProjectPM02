from itertools import combinations
from collections import Counter

nums = list(map(int, input().split()))
cnt_all = Counter(nums)

for comb in combinations(nums, 4):
    # Создаём мультимножество для текущей комбинации
    cnt_comb = Counter(comb)
    
    # Оставшиеся числа — это те, что не вошли в комбинацию (с учётом кратности)
    cnt_remaining = cnt_all.copy()
    for num in comb:
        cnt_remaining[num] -= 1
        if cnt_remaining[num] == 0:
            del cnt_remaining[num]
    
    # Сортируем комбинацию
    sorted_comb = sorted(comb)
    a, b, c, d = sorted_comb
    
    # Вычисляем произведения
    products = [a * b, b * c, c * d, d * a]
    cnt_products = Counter(products)
    
    # Сравниваем оставшиеся числа с произведениями
    if cnt_remaining == cnt_products:
        print(d)
        break