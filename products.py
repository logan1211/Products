products = []
while True:
	name = input('請輸入名稱： ')
	if name == 'q':
		break
	price = input ('請輸入價格： ')
	p =[name, price]
	products.append(p)
print (products)
	
