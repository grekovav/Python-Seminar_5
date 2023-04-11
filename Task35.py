# 35. Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5   Output: yes

# n = int(input('Введите число: '))


# def simple(a):
#     for i in range(2, a):
#         if a % i == 0:
#             return 'Введенное число НЕ является простым'
#         else:
#             return 'Введенное число является простым'


# print(simple(n))


def prime_number(num):
    flag_prime = True
    if num == 1 or num == 2:
        print('Введенное число является простым')
    else:
        i = 2
        while flag_prime and i < num//2+1:
            if num % i == 0:
                flag_prime = False
            i += 1
        if flag_prime:
            print('Введенное число является простым')
        else:
            print('Введенное число НЕ является простым')
    return


number = int(input('Введите целое число: '))
prime_number(number)
