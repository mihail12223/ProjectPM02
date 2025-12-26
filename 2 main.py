def crack_pincode(pincode):
    # Соседи для каждой цифры на клавиатуре (горизонтально/вертикально)
    neighbors = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['0', '5', '7', '8', '9'],
        '9': ['6', '8', '9']
    }
    
    # Начинаем с пустой строки
    results = ['']
    
    # Для каждой цифры в переданном пин-коде
    for digit in pincode:
        # Генерируем новые комбинации
        new_results = []
        for combo in results:
            for neighbor in neighbors[digit]:
                new_results.append(combo + neighbor)
        results = new_results
    
    return results