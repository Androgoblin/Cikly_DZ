# ЗАДАЧА 10

# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


# n = int(input())
# k = 0
# for i in range(n):
#     v = int(input())
#     if v == 1:
#         k += 1
# print(k if k<n/2 else n-k)

#Задача 12

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3


# sum = int(input('Введите сумму чисел: '))
# pro = int(input('Введите произведение чисел: '))
# X = int(-(-sum) - ((-sum)**2 - 4*pro)**0.5) // 2
# Y = sum - X
# if X<=1000 and Y<=1000:
#    print('Петя обманул')
# print(f'числа задуманные Петей -> {X,Y}')

# Задача 14

# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8
# степень 0 1 2 3 результат не больше 10

# N = int(input('Введите целое число больше 1: '))
# p=1
# while p<=N:
#     print(p,end=' ')
#     p=p*2
