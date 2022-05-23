total_money	= 100
price =	7
def cal (x, y, count=0):
    print('totally',x,'money')
    while x - y > 0:
        x = x - y
        count += 1
    print('buy', count, 'chocolate bars, remain', x, 'money')

cal(total_money,price)

total_money = int(input('now, wirte your own total money:'))
price = int(input('write the price:'))
cal(total_money,price)