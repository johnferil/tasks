# -*- coding: utf-8 -*-
"""
Задание 7.3b
Сделать копию скрипта задания 7.3a.
Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.
Пример работы скрипта:
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
vlan_number = input("Ввведите номер VLAN: ")
output = "{:10} {:20} {}"
sort_list = []
with open("CAM_table.txt", "r") as f:
    for line in f:
        if "DYNAMIC" in line:
            str_list = line.split()
            sort_list.append(str_list)
for line in sort_list:
    line[0] = int(line[0])
sort_list = sorted(sort_list   )
for line in sort_list:
    if int(vlan_number) == line[0]:
        print("{:<10} {:20} {}".format(line[0], line[1], line[3]))