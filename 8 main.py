```python
binary_str = "011010001100"
mapping = {
    "00": "а",
    "01": "б",
    "10": "в",
    "11": "г",
    "000": "д",
    "001": "е",
    "010": "ж",
    "011": "з",
    "100": "и",
    "101": "к",
    "110": "л",
    "111": "м"
}

i = 0
result = ""
while i < len(binary_str):
    if binary_str[i] == '0':
        # Попробуем 2-битный код
        if i + 2 <= len(binary_str):
            chunk = binary_str[i:i+2]
            if chunk in mapping:
                result += mapping[chunk]
                i += 2
                continue
    # Если не 2 бита или не подошло — пробуем 3 бита
    if i + 3 <= len(binary_str):
        chunk = binary_str[i:i+3]
        if chunk in mapping:
            result += mapping[chunk]
            i += 3
            continue
    # Если ничего не подошло — ошибка (но по условию всегда должно быть решение)
    i += 1

print(result)