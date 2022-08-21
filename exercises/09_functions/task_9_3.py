# -*- coding: utf-8 -*-
"""
Задание 9.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}
* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}
У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint
def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        config = f.read()
        access_dict = {}
        trunk_dict = {}
        config_sections = config.split("!")
        for section in config_sections:
            section = section.strip()
            if section.find("access") > 0:
                section_lines = section.split("\n")
                for line in section_lines:
                    if line.startswith("interface"):
                        intf = line.split()[-1]
                    if line.find("vlan") > 0:
                        access_dict[intf] = int(line.split()[-1])

            if section.find("trunk") > 0:
                #pprint(section)
                section_lines = section.split("\n")
                for line in section_lines:
                    if line.startswith("interface"):
                        intf = line.split()[-1]
                    if line.find("vlan") > 0:
                        vlan_list_str = line.split()[-1].split(",")
                        vlan_list_int = []
                        for vlan in vlan_list_str:
                            vlan_list_int.append(int(vlan))
                        trunk_dict[intf] = vlan_list_int

        print(access_dict)
        print(trunk_dict)
        return access_dict, trunk_dict







get_int_vlan_map("config_sw1.txt")