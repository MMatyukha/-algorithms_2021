"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import uuid
import hashlib

salt = uuid.uuid4().hex

password = input()
pass_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

print(pass_hash)

with open('file.pass', 'w') as f:
    f.write(pass_hash)

password2 = input()
pass2_hash = hashlib.sha256(salt.encode() + password2.encode()).hexdigest()


with open('file.pass', 'r') as f:
    pass_hash = f.readline()
    print(pass_hash == pass2_hash)