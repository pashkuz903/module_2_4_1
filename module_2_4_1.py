# Ввод исходных данных
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Создаем пустые списки
primes = []
not_primes = []
# Создаем цикл
for i in numbers:
    if i == 1:
        continue # Условие для пропуска числа 1. Т.К. оно не простое и не сложное
    is_primes = True # Просто число - правда
    for j in range(2,i): # Внутренний цикл для подбора делителя
        if i % j == 0: # Условие: делимое должно делится на делитель без остатка
            is_primes = False # Если нет остатка, то это ложь
            break # Если делитель найден, то остановка внутреннего цикла
    if is_primes: # Ели правда, то в список "primes"
        primes.append(i)
    else: # Если ложь - "not_primes"
        not_primes.append(i)

print('Primes:', primes)
print('Not primes:', not_primes)


