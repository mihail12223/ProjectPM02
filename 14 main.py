def sum_arith(first, last, step):
    if first > last:
        return 0
    n = (last - first) // step + 1
    return n * (first + last) // 2

A = int(input())
B = int(input())

# Чётные
even_start = A if A % 2 == 0 else A + 1
even_end = B if B % 2 == 0 else B - 1
sum_even = sum_arith(even_start, even_end, 2)

# Нечётные
odd_start = A if A % 2 == 1 else A + 1
odd_end = B if B % 2 == 1 else B - 1
sum_odd = sum_arith(odd_start, odd_end, 2)

print(sum_even - sum_odd)