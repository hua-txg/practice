import os

#讀取檔案  
#檔名'products.csv'寫成參數,每次可讀不同檔案, 
#products = [] 讀到的資料存到 products 清單，故要回吐用return，加在最後一行
def read_file(filename):
	products = []
	if os.path.isfile(filename):
		print('yeah! 找到檔案了!')
		
		with open(filename, 'r', encoding='utf-8') as f:
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
	return products



#讓使用者輸入
# products = []
def user_input(products):
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
	return products

#簡寫 products.append([name, price])

#印出所有購買釲錄
def print_products(products):
	for p in products:
		print(p)
		print(p[0], '的價格是', p[1])

#輸入結果寫入檔案
# with open('products.txt', 'w') as f:
# 	for p in products:
# 		f.write(p[0]+','+str(p[1])+'\n')

#寫入檔案
#寫入欄位名稱
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0]+','+str(p[1])+'\n')





products = read_file('products.csv')  #read_file()有return 故用products來存
products = user_input(products)       #把read_file()的products再讓使用者key in後，return在存回products
print_products(products)              #只是印出不用回傳
write_file('products.csv', products)
