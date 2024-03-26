products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
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
with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0]+','+p[1]+'\n')

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0]+','+p[1]+'\n')


