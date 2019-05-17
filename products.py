products = []
while True:
	name = input('請輸入名稱： ')
	if name == 'q':
		break
	price = input ('請輸入價格： ')
	p =[name, price]
	products.append(p)
print (products)


with open ('products.csv', 'w', encoding= 'utf-8') as f:
	f.write('商品,價格,\n')
	for i in products:
		f.write(i[0]+',' + i[1] + ','+ '\n' )

