# 33. Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4   Output: 1 3 3 3 1
# Ввод оценок пока != 0

# def input_rating():
#     list_rating = []
#     i = 0
#     flag_stop_input = False
#     while not flag_stop_input:
#         temp = int(input('Введите оценку: '))
#         if temp == 0:
#             flag_stop_input = True
#         else:
#             list_rating.append(temp)
#             i += 1
#     return list_rating


# def change_rating(list_rating_input):
#     for i in range(len(list_rating_input)):
#         if list_rating_input[i] == max(list_rating_input):
#             list_rating_input[i] = min(list_rating_input)
#     return list_rating_input


# rating_list_new = input_rating()
# print(f'Оценки до изменения: {rating_list_new}')
# print(f'Оценки после изменения: {change_rating(rating_list_new)}')

def rec_input(list1):
    temp = int(input('Введите оценку: '))
    if temp == 0:
        return list1
    list1.append(temp)
    list1 = rec_input(list1)
    return list1
list_new = []
print(rec_input(list_new))
