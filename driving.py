country = input('請問你是那國人：')
age = input('你輸入年齡：')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')