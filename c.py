class Student:
	
	def __init__(self, name, score):
		self.name = name  #將參數的name存成自己的name
		self.score = score
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
   

s1 = Student('John', 100)
s2 = Student('Allen', 95)
print(s1.name, s1.score)  #屬性給印出來
print(s2.name, s2.score)