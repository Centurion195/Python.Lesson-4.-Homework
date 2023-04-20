# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.

list_1 = [int(input()) for _ in range(int(input("Количество элементов множества #1: ")))]
list_2 = [int(input()) for _ in range(int(input("Количество элементов множества #2: ")))]

set_list = set(list_1).intersection(set(list_2))

print(sorted(list(set_list)))