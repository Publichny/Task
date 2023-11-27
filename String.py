# str1 = 'James'
# print("Original: ", str1)
# res = str1[0] # записывается первый символ из str1.
# l = len(str1) # вычисляется длина строки str1 (в данном случае, 5).
# mi = int(l / 2) # вычисляется индекс среднего символа. В данном случае, это 2 (индексация начинается с 0).
# res = res + str1[mi] # добавляется средний символ из str1.
# res = res + str1[l - 1] # добавляется последний символ из str1.
# print("New String:", res) # Результат


# # Task - 1
# def get_middle_three_chars(str1):
#     print("Original String is", str1)
#     # сначала получаем средний индекс
#     mi = int(len(str1) / 2)
#     # используем разрезание строк для получения символов результата
#     res = str1[mi - 1:mi + 2]
#     print("Middle three chars are:", res)
# get_middle_three_chars("JhonDipPeta")
# get_middle_three_chars("JaSonAy")


# # Task - 2
# def append_middle(s1, s2):
#     print("Original Strings are", s1, s2)
#     # средний индекс s1
#     mi = int(len(s1) / 2)
#     # получаем символ от 0 до среднего номера индекса от s1
#     x = s1[:mi:]
#     # соединить с ним s2
#     x = x + s2
#     # добавляем оставшийся символ из s1
#     x = x + s1[mi:]
#     print("After appending new string in middle:", x)
# append_middle("Ault", "Kelly")


# # Task - 3
# def mix_string(s1, s2):
#     # получаем первый символ из обеих строк
#     first_char = s1[0] + s2[0]
#     # получаем средний символ из обеих строк
#     middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
#     # получаем последний символ из обеих строк
#     last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
#     # добавить все
#     res = first_char + middle_char + last_char
#     print("Mix String is ", res)
# s1 = "America"
# s2 = "Japan"
# mix_string(s1, s2)


# # Task - 4
# str1 = "PYnAtivE"
# print('Original String:', str1)
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         # добавляем строчные буквы в нижний список
#         lower.append(char)
#     else:
#         # добавляем заглавные буквы в нижний список
#         upper.append(char)
# # Присоединяйтесь к обоим спискам
# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)


# # Task - 5
# def find_digits_chars_symbols(sample_str):
#     char_count = 0
#     digit_count = 0
#     symbol_count = 0
#     for char in sample_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         # если это не буква или цифра, то это специальный символ
#         else:
#             symbol_count += 1
#     print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)
# sample_str = "P@yn2at&#i5ve"
# print("total counts of chars, Digits, and symbols \n")
# find_digits_chars_symbols(sample_str)


# # Task - 6
# s1 = "Abc"
# s2 = "Xyz"
# # получаем длину строки
# s1_length = len(s1)
# s2_length = len(s2)
# # получаем длину большей строки
# length = s1_length if s1_length > s2_length else s2_length
# result = ""
# # обратный s2
# s2 = s2[::-1]
# # повторить строку
# # s1 по возрастанию и s2 по убыванию
# for i in range(length):
#     if i < s1_length:
#         result = result + s1[i]
#     if i < s2_length:
#         result = result + s2[i]
# print(result)


# # Task - 7
# def string_balance_test(s1, s2):
#     flag = True
#     for char in s1:
#         if char in s2:
#             continue
#         else:
#             flag = False
#     return flag
# s1 = "Yn"
# s2 = "PYnative"
# flag = string_balance_test(s1, s2)
# print("s1 and s2 are balanced:", flag)
# s1 = "Ynf"
# s2 = "PYnative"
# flag = string_balance_test(s1, s2)
# print("s1 and s2 are balanced:", flag)


# # Task - 8
# str1 = "Welcome to USA. usa awesome, isn't it?"
# sub_string = "USA"
# # преобразовать строку в нижний регистр
# temp_str = str1.lower()
# # использовать функцию подсчета
# count = temp_str.count(sub_string.lower())
# print("The USA count is:", count)


# # Task - 9
# import re
# input_str = "PYnative29@#8496"
# digit_list = [int(num) for num in re.findall(r'\d', input_str)]
# print('Digits:', digit_list)
# # используйте встроенную функцию sum
# total = sum(digit_list)
# # среднее значение = сумма / количество цифр
# avg = total / len(digit_list)
# print("Sum is:", total, "Average is ", avg)


# # Task - 10
# str1 = "Apple"
# # создайте результирующий словарь
# char_dict = dict()
# for char in str1:
#     count = str1.count(char)
#     # добавить / обновить количество символов
#     char_dict[char] = count
# print('Result:', char_dict)


# # Task - 11
# str1 = "PYnative"
# print("Original String is:", str1)
# str1 = ''.join(reversed(str1))
# print("Reversed String is:", str1)


# # Task - 12
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print("Original String is:", str1)
# index = str1.rfind("Emma")
# print("Last occurrence of Emma starts at index:", index)


# # Task - 13
# str1 = "Emma-is-a-data-scientist"
# print("Original String is:", str1)
# # разделенная строка
# sub_strings = str1.split("-")
# print("Displaying each substring")
# for sub in sub_strings:
#     print(sub)


# # Task - 14
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# # используйте встроенную функцию filter для фильтрации пустого значения
# new_str_list = list(filter(None, str_list))
# print("After removing empty strings")
# print(new_str_list)


# # Task - 15
# import re
# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)
# # заменить специальные символы на "
# res = re.sub(r'[^\w\s]', '', str1)
# print("New string is ", res)


# # Task - 16
# str1 = 'I am 25 years and 10 months old'
# print("Original string is", str1)
# # Сохранять числа в строке
# # Используя понимание списка + join() + isdigit()
# res = "".join([item for item in str1 if item.isdigit()])
# print(res)


# # Task - 17
# str1 = "Emma25 is Data scientist50 and AI Expert"
# print("The original string is : " + str1)
# res = []
# # разбить строку на пробелы
# temp = str1.split()
# # Слова, содержащие как алфавиты, так и цифры
# # isdigit() для цифр + isalpha() для алфавитов
# # используйте any() для проверки каждого символа
# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)
# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)


# # Task - 18
# import string
# str1 = '/*Jon is @developer & musician!!'
# print("The original string is : ", str1)
# # Замените знаки препинания на #
# replace_char = '#'
# # строка.знаки препинания, чтобы получить список всех специальных символов
# for char in string.punctuation:
#     str1 = str1.replace(char, replace_char)
# print("The strings after replacement : ", str1)






# Algodan 165-172
# Cpython 59 - 74, 127,131,132,133,134,483,484,523,524,252,527



def filter_list(my_list, num):
    if num != 0:
        my_list = [x for x in my_list if x % num != 0]
    return my_list




