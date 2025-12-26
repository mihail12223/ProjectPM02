def split(s):
    result = []
    start = 0
    balance_round = 0
    balance_square = 0
    
    for i, ch in enumerate(s):
        if ch == '(':
            balance_round += 1
        elif ch == ')':
            balance_round -= 1
        elif ch == '[':
            balance_square += 1
        elif ch == ']':
            balance_square -= 1
        
        if balance_round == 0 and balance_square == 0:
            result.append(s[start:i+1])
            start = i+1
    
    return result