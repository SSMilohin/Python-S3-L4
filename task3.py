# Напишите программу, которая принимает список строк и выводит
# количество повторений данных строк в списке.
# Необходимо реализовать решение с использованием словарей.

slovar = {}
string_input = input("Введите строку (например - abc bcd abc abd abd dcd abc): ").split()
for i in range(len(string_input)):
    if string_input[i] in slovar:
        slovar[string_input[i]] += 1
    else:
        slovar[string_input[i]] = 1

print(slovar)

result_string = ""
for key in slovar:
    result_string += str(slovar.get(key)) + " "
print(result_string)