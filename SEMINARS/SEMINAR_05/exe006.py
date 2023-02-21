def degree(a, b):
    if b==0:
        return 1
    else:
    # res = (a*degree(a, b-1))
        return (a * degree(a, b-1))

res = 0
a = int(input('введите число А: '))
b = int(input('введите число B: '))
# res = degree(a, b)
# res = degree(a, b)
print(degree(a, b))

#
# def power(base, exp):
#     if (exp == 1):
#         return (base)
#     elif (exp == 0):
#         return 1
#     else:
#     # if (exp != 1):
#         return (base * power(base, exp - 1))
#
# base = int(input("Введите число: "))
# exp = int(input("Введите его степень: "))
# print("Результат возведения в степень равен:", power(base, exp))
