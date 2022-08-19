# -*- coding: utf-8 -*-
"""
Задание 7.1
Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:
O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0
O        10.0.28.0/24 [110/31] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.37.0/24 [110/11] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.41.0/24 [110/51] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.78.0/24 [110/21] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.79.0/24 [110/20] via 10.0.19.9, 4d02h, FastEthernet0/2

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



with open("ospf.txt") as f:
    for  line in f:
        output = "\n{:25} {}" * 5

        line = line.replace(",", " ").replace("[", "").replace("]", "")
        line = line.split()
        #print(line)
        ip = line[1]
        print(output.format("Prefix", line[1],
        "AD/Metric", line[2],
        "Next-Hop", line[4],
        "Last update", line[5],
        "Outbound Interface", line[6]))

        #, "AD/Metric", line[2], "Next-Hop", line[4], "Last update", line[5], "Outbound Interface", line[6])