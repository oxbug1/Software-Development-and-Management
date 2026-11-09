lab_done = False
points = int(input())
if points >= 60:
	lab_done = True
else:
	lab_done = False
if lab_done:
	print('Сдал')
else:
	print('Не сдал')