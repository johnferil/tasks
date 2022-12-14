# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ignore = ["duplex", "alias", "configuration"]

source_file = argv[1]
dest_file = argv[2]

with open(source_file, "r") as f:
    with open (dest_file, "w") as f_dest:
        for line in f:
            if not line.lstrip().startswith('!'):
                a = 0
                for ign in ignore:
                    if not (line.find(ign)+1):
                        a +=1
                    if a == len(ignore):
                        f_dest.write(line)

