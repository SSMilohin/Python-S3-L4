# Напишите программу, которая принимает 2 списка чисел и определяет
# количество общих чисел из первого и второго списка

def number_of_the_same_elements(list1,list2):
    list_of_repeats = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j] and list1[i] not in list_of_repeats:
                list_of_repeats.append(list1[i])

    return len(list_of_repeats)

def string_to_int_list(string):
    int_list = string.split()
    for i in range(len(int_list)):
        int_list[i] = int(int_list[i])
    return int_list

list_1 = string_to_int_list(input("Введите первый список чисел (Например: 1 2 3 4 5 6 7 8 9): "))
list_2 = string_to_int_list(input("Введите второй список чисел (Например: 3 3 3 4 5 5 7 9 9): "))

print(number_of_the_same_elements(list_1,list_2))