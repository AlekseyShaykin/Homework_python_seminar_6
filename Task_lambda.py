# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.


data = [i for i in range(1, int(input(" : ")))]
lst = list(map(lambda n:(1+1/n)**n, data))
print(sum(lst))