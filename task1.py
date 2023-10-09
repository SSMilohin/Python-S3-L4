# Задан список с числами. Напишите программу, которая меняет местами
# наибольший и наименьший элемент и выводит новый список

def min_max_swap(input_list):
    min_index = 0
    max_index = 0
    for i in range(1,len(input_list)):
        if input_list[min_index] > input_list[i]:
            min_index = i
        if input_list[max_index] < input_list[i]:
            max_index = i
    if min_index != max_index:
        input_list[min_index],input_list[max_index] = input_list[max_index], input_list[min_index]

list = [4,2,6,3,9,7,5]
min_max_swap(list)
print(list)