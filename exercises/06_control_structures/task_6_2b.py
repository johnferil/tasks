# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_addr_incorrect = True

while ip_addr_incorrect:
    ip_addr = input("Введите IP-адрес в формате 10.0.1.1: ")
    ip_list = ip_addr.split(".")
    digest_count = 0
    digest_normal_range = 0
    for octet in ip_list:
        if octet.isdigit:
            digest_count += 1
        try:
            if int(octet) >=0 and int(octet) <=255:
                digest_normal_range += 1
        except ValueError:
            continue

    if ip_addr.count(".") != 3:
        print("Неправильный IP-адрес")
        continue
    if digest_count != 4:
       print("Неправильный IP-адрес")
       continue
    if digest_normal_range != 4:
       print("Неправильный IP-адрес")
       continue
    ip_addr_incorrect = False



if int(ip_list[0]) >= 1 and int(ip_list[0]) <= 223:
    print("unicast")
elif int(ip_list[0]) >= 224 and int(ip_list[0]) <= 239:
    print("multicast")
elif ip_addr == "255.255.255.255":
    print("local broadcast")
elif ip_addr == "0.0.0.0":
    print("unassigned")
else:
    print("unused")