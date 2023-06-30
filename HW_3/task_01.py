# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


my_list = [1, 1, 4, 5, 7, 7, 8, 0]
new_list = []

for num in my_list:
    if my_list.count(num) > 1 and num not in new_list:
        new_list.append(num)
        
print(my_list, new_list, sep='\n')
