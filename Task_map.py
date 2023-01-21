# 14.	Подсчитать сумму цифр в вещественном числе.

string = str(input("Input вещественное число: "))
lst1 = list(map(int, [i for i in string if i.isdigit()]))

sum=0
for i in lst1:
    sum+=i
print(f'Сумма чисел в вещественном числе {string} = {sum}')
