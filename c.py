class Student:
	
	def __init__(self, name):
		self.name = name  #將參數的name存成自己的name
		print('我誕生了名字是', self.name )
		self.do_hw('英文')
		self.study()
		self.sleep()
	def do_hw(self, hw):
		print('我在做作業', hw)
	def study(self):
		print('我在讀書')
	def sleep(self):
		print('i am sleeping')
   

s1 = Student('John')
s2 = Student('Allen')
print(s1.name, s2.name) #不是執行function，而是把name那個屬性給印出來
