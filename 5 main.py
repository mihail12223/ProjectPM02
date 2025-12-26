def next_palindrome(s):
    n = len(s)
    if all(ch == '9' for ch in s):
        return '1' + '0' * (n - 1) + '1'
    
    mid = n // 2
    if n % 2 == 0:
        left = s[:mid]
        candidate = left + left[::-1]
        if candidate > s:
            return candidate
        new_left = str(int(left) + 1)
        return new_left + new_left[::-1]
    else:
        left = s[:mid + 1]
        candidate = left + left[-2::-1]
        if candidate > s:
            return candidate
        new_left = str(int(left) + 1)
        return new_left + new_left[-2::-1]

print(next_palindrome(input().strip()))
