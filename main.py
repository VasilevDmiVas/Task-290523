# result = 0
# count = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number >= 0:
#         result += number
#         count += 1
#     if number < 0:
#         break
#     print('Сумма чисел = ', result)
# print('Результат =', result / count)

# result = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number == 0:                      #and number % 2 == 1 or number < 0 and number % 2 == 1: 0 четный
#         break
#     if number % 2 == 0:
#         continue
#     result += number
# print('Сумма нечетных чисел = ', result)

# 6.4 операторы использовать
# 6.6 б + разность между ними
# 6.42 а

# 6.4
# result = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number > 0:
#         break
#     result += 1
# print('Количество введенных отрицательных чисел =',result)

# 6.6 б
# while True:


# # 6.42 а
# number = int(input('Введите число\n'))
# maxNumber1 = 0
# maxNumber2 = 0
# index = 0
#
# indexMaxNumber1 = 0
# indexMaxNumber2 = 0
# number1 = number
# while number1 > 0:
#     x = number1 % 10 # переход в конец введенного числа
#     if x > maxNumber1:
#         maxNumber1 = x
#         indexMaxNumber1 = index
#     index += 1
#     number1 //= 10
# print(maxNumber1)
# print(indexMaxNumber1)
#
# number1 = number
# index = 0
# while number1 > 0:
#     x = number1 % 10
#     if x > maxNumber2 and x != maxNumber1:
#         maxNumber2 = x
#         indexMaxNumber2 = index
#     if x > maxNumber2:
#         maxNumber2 = x
#         indexMaxNumber2 = index
#     index +=1
#     number1 //= 10
# print(maxNumber2)
# print(indexMaxNumber2)

# number1 = 5
# number2 = 10
# summa = number1 + number2
# print(number1, '+', number2, '=', number1+number2)
# print(f'{number1} + {number2} = {summa}')

# Гоша Дударь itproger.com ютуб

# 9.14 9.15 9.16 9.24 9.38а 9.41 9,59 9,76 б
# дана строка вывести ее наоборот

# 9.14
# text = input('Введите слово\n')
# print(text[-1])

# 9.15
# text = input('Введите слово\n')
# number = int(input('Введите номер символа который нужно вывести\n'))
# print(text[number])

# 9.16
# text = input('Введите слово\n')
# if text[2] == text[4]:
#     print('Символы одинаковы')
# else:
#     print('Символы разные')

# 9.24
# text = 'Яблоко'
# print(text[1:5])
# print(text[3:6])

# 9.38а
# text = input('Введите слово из 12 букв\n')
# if len(text) <= 12:
#     print(text[8:12], text[4:8], text[0:4])
#     print(f'{text[8:12]}{text[4:8]}{text[0:4]}')
# else:
#     print('Ошибка ввели > 12 символов')

# 9.41
# print('Л\nо\nк\nо\nм\nо\nт\nи\nв')
# text = input('Введите текст \n')
# text1 = len(text)
# while text1 < 10:
#     if text1 > 1:
#         print(text[0],'\n',text[1],'\n',text[2],'\n')


# 9.59
text = input('Введите текст \n')
# text1 = len(text)
# print(list(text))
print(text[::-1])
