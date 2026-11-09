# Задача 1 Переворачивание текста
#
# word = input()
# drow = word[::-1]
# print(drow)


# Задача 2 Проверяет введеный пароль на сложность
# import re
# password = input('Введите пароль: ')
# password_pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+$'
# if re.match(password_pattern, password):
# 	print('Пароль принят')
# else: print('Придумай что-то по сложнее')


# Задача 3 Определение валидного IP
# import re
# ip = input('Введите ip-адрес: ')
# ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
# if re.match(ip_pattern, ip):
# 	print('IP корректный')
# else: print('Ну и чушь же ты ввел')


# Задача 4 Очистка строки от ненужных символов и оставляет только алфавитные символы и цифры
import re
text = input('Введите текст: ')
clean_text = re.sub(r'[^a-zA-Zа-яА-Яё]', '', text)
print(clean_text)