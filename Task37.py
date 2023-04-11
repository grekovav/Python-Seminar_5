# 37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы
# и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4    Output: 4 3

# n = int(input('Введите число: '))


# def somefunc(a):
#     result = str(a)
#     if a == 1:
#         return result
#     return result + somefunc(a-1)


# print(somefunc(n))

def rec_input(num):
    if num == 1:
        return input()
    temp = input()
    list_str = rec_input(num-1) + ' ' + temp
    return list_str


n = int(input('Введите натуральное число N: '))
print(rec_input(n))
