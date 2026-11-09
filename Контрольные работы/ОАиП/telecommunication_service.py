import os 
import msvcrt

def get_choice():
	char = msvcrt.getch()
	choice = char.decode('utf-8')
	return choice

def clear_screen():
	os.system('cls')

def menu(menu_num):
	match menu_num:
		case 'main':
			print('Главное меню:\n(1)Мой тариф\n(2)Учет расходов\n(3)Выбор тарифа\n(0)Выход')
		case 'rate':
			print('Выбор тарифа:\n(1)Эконом\n(2)Стандарт\n(3)Безлимит\n(0)Назад')
		case 'expenses':
			print(f'Информация по расходам:\n(1)Израходовано минут: {minutes_used}\n(2)Отправлено Сообщений: {sms_used}\n(3)Счет за услуги\n(0)Назад')
		case 'yes_no':
			print('(1)Да\n(2)Нет')
		case _:
			print('Такого меню не существует')

def press_any_key():
	print('Нажмите любую клавишу..')
	get_choice()

# Тарифы
rate1 = {
	'name': 'Эконом',
	'price': 200,
	'minute': 100,
	'sms': 10,
	'cost_per_minute': 1,
	'cost_of_a_message': 2
}

rate2 = {
	'name': 'Стандарт',
	'price': 350,
	'minute': 300,
	'sms': 20,
	'cost_per_minute': 2,
	'cost_of_a_message': 3
}

rate3 = {
	'name': 'Безлимит',
	'price': 700,
	'minute': 0,
	'sms': 0,
	'cost_per_minute': 0,
	'cost_of_a_message': 0
}

current_rate = {}

minutes_used = 0
sms_used = 0
minutes_comission = 0
sms_comission = 0

while True:
	clear_screen()
	menu('main')
	match get_choice():
		case '1':
			if not current_rate:
				clear_screen()
				print('Вы еще не выбрали тариф')
				press_any_key()
			else:
				clear_screen()
				print(
					f'Ваш тариф: {current_rate['name']}\n'
					f'Стоимость в месяц: {current_rate['price']}\n'
					f'Кол-во бесплатных минут: {current_rate['minute']}\n'
					f'Кол-во бесплатных сообщений: {current_rate['sms']}\n'
					f'Стоимость одной минуты сверх тарифа: {current_rate['cost_per_minute']}руб\n'
					f'Стоимость сообщения сверх тарифа: {current_rate['cost_of_a_message']}руб\n'
					)
				press_any_key()
		case '2':
			while True:
				clear_screen()
				menu('expenses')
				match get_choice():
					case '1':
						clear_screen()
						while True:
							minutes_used = int(input('Введите кол-во потраченных минут за месяц: '))
							if minutes_used < 0:
								print('Вы ввели отрицательное кол-во минут')
								continue
							elif minutes_used > 44640:
								print('В месяце нет столько минут..')
								continue
							print(f'Вы потратили {minutes_used}, верно?')
							menu('yes_no')
							match get_choice():
								case '1':
									break
								case '2':
									continue
								case _:
									clear_screen()
									print('Некорректный выбор')
									press_any_key()

					case '2':
						clear_screen()
						while True:
							sms_used = int(input('Введите кол-во отправленных за месяц сообщений: '))
							if sms_used < 0:
								print('Вы ввели отрицательное кол-во минут')
								continue
							elif sms_used > 200000:
								print('Вы не можете использовать столько сообщений..')
								continue
							print(f'Вы потратили {sms_used}, верно?')
							menu('yes_no')
							match get_choice():
								case '1':
									break
								case '2':
									continue
								case _:
									clear_screen()
									print('Некорректный выбор')
									press_any_key()
					case '3':
						if not current_rate:
							clear_screen()
							print('Вы не выбрали тариф')
							press_any_key()
							continue

						# Расчет комиссии за минуты
						if current_rate['minute'] - minutes_used < 0: 
							minutes_comission = (current_rate['minute'] - minutes_used) * -1 * current_rate['cost_per_minute']
						else: minutes_comission = 0
						# Расчет комиссии за сообщения
						if current_rate['sms'] - sms_used < 0: 
							sms_comission = (current_rate['sms'] - sms_used) * -1 * current_rate['cost_of_a_message']
						else: sms_comission = 0
						# Итоговая сумма
						total_sum = current_rate['price'] + minutes_comission + sms_comission

						clear_screen()
						print(
							f'За этот месяц вы потратили:\n'
							f'На оплату тарифа: {current_rate['price']}\n'
							f'Комиссия за перерасход минут: {minutes_comission}\n'
							f'Комиссия за перерасход сообщений: {sms_comission}\n'
							f'ИТОГО: {total_sum}')
						press_any_key()
					case '0':
						break
					case _:
						clear_screen()
						print('Некорректный выбор')
						press_any_key()	
			continue
		case '3':
			while True:
				clear_screen()
				menu('rate')
				match get_choice():
					case '1':
						current_rate = rate1
						clear_screen()
						print('Выбран тариф Эконом')
						press_any_key()
						break
					case '2':
						current_rate = rate2
						clear_screen()
						print('Выбран тариф Стандарт')
						press_any_key()
						break
					case '3':
						current_rate = rate3
						clear_screen()
						print('Выбран тариф Безлимит')
						press_any_key()
						break
					case '0':
						break
					case _:
						clear_screen()
						print('Некорректный выбор')
						press_any_key()
		case '0':
			clear_screen()
			break
		case _:
			clear_screen()
			print('Некорректный выбор')
			press_any_key()
