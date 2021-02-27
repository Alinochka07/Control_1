import random
from itertools import zip_longest

# Task 1

lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

dic = {index: value for index, value in enumerate(lst)}
print(dic)

# Task 2
n = (random.randrange(1, 21))

max_attempts = 4
attempt = 0

while attempt <= max_attempts:
    user_guess = int(input("Угадайте рандомное число от 1 до 20: "))
    attempt += 1
    if user_guess == n:
        print("Класс! Вы угадали!")
        break 
    elif user_guess > n:
        print("Слишком много")
    elif user_guess < n:
        print("Слишком мало")
else:
    print("Все! Вы не выиграли, игра завершилась...")

# Task 3
some_string = str(input("Введите любое слово: "))

print(some_string[int(len(some_string)/2) - 1:int(len(some_string)/2) + 2])

# Task 4
a = str(input("Введите любую строку или имя: "))
b = str(input("Введите еще одну строку или имя: "))

# if the length of strings does not matter
print(''.join(''.join(i) for i in zip_longest(a, b, fillvalue='')))

# option 2
# if the length of strings are same
# a_len = len(a)
# b_len = len(b)

# output = ""
# for i in range(len(a)):
#     output += a[i]
#     output += b[i]

# print(output)

