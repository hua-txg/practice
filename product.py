#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		# s = line.strip().split(',')
		# name = s[0]
		# price = s[1]
		name, price = line.strip().split(',')
		products.append([name, price])
	print(products)




# products = []
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

for p in products:
	print(p)
	print(p[0], '的價格是', p[1])

#輸入結果寫入檔案
# with open('products.txt', 'w') as f:
# 	for p in products:
# 		f.write(p[0]+','+str(p[1])+'\n')

#寫入欄位名稱
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+','+str(p[1])+'\n')


