class Student:
	def __init__(self):
		print('我誕生了')
		self.do_hw('英文')
		self.study()
		self.sleep()
	def do_hw(self, hw):
		print('我在做作業', hw)
	def study(self):
		print('我在讀書')
	def sleep(self):
		print('i am sleeping')
   

s = Student()

