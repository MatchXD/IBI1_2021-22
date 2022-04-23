total_money	= 100
price =	7
def cal (x, y, count=0):
    print('totally',x,'money')
    while x > 0:
        x = x - y
        if x > 0:
            count += 1
            print('buy',count,'chocolate bars, remain',x,'money')
    print('can totally buy',count,'chocolate bars')
cal(total_money,price)