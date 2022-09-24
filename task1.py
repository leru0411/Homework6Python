#Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
# n = int(input('Введите число: '))
# for i in range(1, n + 1):
#     print(f'{i}: {(1 + 1/i)**i}')

n = int(input('Введите число: '))
list_1 = [i for i in range(1, n+1)]
list_2 = [round((1 + 1/i)**i, 2) for i in range(1, n+1)]
print(*list(zip(list_1, list_2)))