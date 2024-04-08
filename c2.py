class Desk:
	def __init__(self, color):
		self.color = color
		print('我被制造出來了')
	def re_color(self, new_color):
		self.color = new_color

d = Desk('Blue')  #instantiation實體化(創作出物件), 存成d
d.re_color('red')
print(d.color)


