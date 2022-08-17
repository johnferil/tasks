# -*- coding: utf-8 -*-
"""
Задание 5.2
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10        1         1         0
00001010  00000001  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)
Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
network = input("Ввод IP-сети в формате: 10.1.1.0/24: ")
net_mask = network.split('/')
print("Network:")
octets = net_mask[0].split(".")
output = """
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""
print(output.format(int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3])))

print("Mask:")
print("/{}".format(int(net_mask[1])))
mask_bin = "1" * int(net_mask[1]) + "0" * (32 - int(net_mask[1]))
output = """{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""
print(output.format(int(mask_bin[0:8],2), int(mask_bin[8:16],2), int(mask_bin[16:24],2), int(mask_bin[24:33],2)))
