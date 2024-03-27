import os

#讀取檔案  
def read_file():
	products = []
	if os.path.isfile('products.csv'):
		print('yeah! 找到檔案了!')
		
		with open('products.csv', 'r', encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue #繼續
				# s = line.strip().split(',')
				# name = s[0]
				# price = s[1]
				name, price = line.strip().split(',')
				products.append([name, price])
			print(products)
	else:
		print('找不到檔案')



#讓使用者輸入
# products = []
def user_input():
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		price = int(price)
		p = []
		p.append(name)
		p.append(price)
		products.append(p)
	print(products)

#簡寫 products.append([name, price])

#印出所有購買釲錄
def print_products():
	for p in products:
		print(p)
		print(p[0], '的價格是', p[1])

#輸入結果寫入檔案
# with open('products.txt', 'w') as f:
# 	for p in products:
# 		f.write(p[0]+','+str(p[1])+'\n')

#寫入檔案
#寫入欄位名稱
def write_file():
	with open('products.csv', 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0]+','+str(p[1])+'\n')





read_file()
user_input()
print_products()
write_file()
