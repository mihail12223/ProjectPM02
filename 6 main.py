results = []
for a in range(1, 10):      
    for b in range(0, 10):  
        num = 10 * a + b
        digit_sum = a + b
        digit_product = a * b
        if digit_sum + digit_product == num:
            results.append(num)

for num in results:
    print(num)