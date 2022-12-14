# -*- coding: utf-8 -*-
"""
Задание 9.4
Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.
Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint
ignore = ["duplex", "alias", "configuration"]
def ignore_command(command, ignore):
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    config_dict = {}
    with open(config_filename) as cfg:
        for line in cfg:
            if line.startswith("!"): continue
            elif line[0].isalnum():
                key_string = line.strip()
                config_dict[key_string] = []
            elif not line[0].isalnum() and len(line) > 1 and not(ignore_command(line, ignore)):
                argument_string = line.strip()
                config_dict[key_string].append(argument_string)
        result_config_dict = {}
        for key, values in config_dict.items():
            if not(ignore_command(key, ignore)):
                result_config_dict[key] = values

        return result_config_dict


pprint(convert_config_to_dict("config_sw1.txt"))