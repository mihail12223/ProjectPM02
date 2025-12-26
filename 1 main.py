def decrypt_caesar_russian(ciphertext):
    # Русский алфавит без 'Ё', как в шифровке
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    n = len(alphabet)
    
    # Функция для расшифровки с заданным сдвигом
    def decrypt_with_shift(text, shift):
        res = ''
        for ch in text:
            if ch in alphabet:
                res += alphabet[(alphabet.index(ch) - shift) % n]
            else:
                res += ch
        return res

    # Проверим все сдвиги и найдём тот, где есть "СЧАСТЬЕ" или "СКАЗАЛ" — ключевые слова
    for shift in range(1, n):
        plain = decrypt_with_shift(ciphertext, shift)
        # Приведём к нижнему регистру для удобства проверки
        plain_lower = plain.lower()
        if 'счастье' in plain_lower or 'сказал' in plain_lower:
            return shift, plain

    # На всякий случай — вернём лучший из найденных (если автоматика не сработает)
    for shift in range(1, n):
        plain = decrypt_with_shift(ciphertext, shift)
        if 'я' in plain.split() or 'на' in plain.lower().split():
            return shift, plain

    # Если ничего — вернём все варианты
    all_variants = [decrypt_with_shift(ciphertext, s) for s in range(1, n)]
    return None, all_variants

# Входной текст
cipher = "ЗЖ АЮДЮЖФВ, АДЗВ Б ЗРЮЖХ ЖЮ ДЧЪБЛ ЙЗЯЭЮКЛЫЗ."

shift, result = decrypt_caesar_russian(cipher)

if isinstance(result, str):
    print(f"✅ Расшифровано! Сдвиг: {shift}")
    print(f"Текст: {result}")
else:
    print("Не удалось автоматически расшифровать. Все варианты:")
    for s in range(1, 33):
        print(f"Сдвиг {s}: {result[s-1]}")