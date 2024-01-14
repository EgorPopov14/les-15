orders=[]
with open('ordiers.txt','r') as f:
    for order in f:
        orders.append(order.replace('\n'),''))
while True:
    print('1.добавить покупку')
    print('2.история покупок')
    print('3.выход')
    choice=input('введите номер: ')
    if choice =='1':
        name=input('введите название')
        orders.append(name)
    elif choice=='2':
        for orfer in orders:
            print(order)
    elif choice=='3':
        with open('ordiers.txt','w') as f:
            for order in orders:
                f.write(f'{order}\n')

