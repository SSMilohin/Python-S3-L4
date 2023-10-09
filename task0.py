# Задан список с числами. Напишите программу, которая выводит все
# элементы списка, которые больше предыдущего, в виде отдельного списка.

def find_greater_elements(list):
	result_list = []
	for i in range(1, len(list)):
		if list[i] > list[i-1]:
			result_list.append(list[i])
	return result_list

list_in = [1, 2, 3, 4, 3, 6, 7, 1]
greater_elements = find_greater_elements(list_in)
print(greater_elements)