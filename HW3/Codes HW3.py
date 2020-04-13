import math

s = int(input('股票價格: '))
x = int(input('履約價: '))
r = float(input('無風險利率(%): '))/100
T = int(input('距離履約期數: ')) + 1
u = float(input('股票上漲幅度: '))
d = float(input('股票下跌幅度: '))
R = math.exp(r)
R2 = math.exp(-r)

p = (R - d)/(u - d) #risk-neutral probability
if p < 0:
    p = 0
if p > 1:
    p = 1
price = [[0]*T for i in range(T)]
for i in range(T):
    for j in range(i+1):
        price[i][j] = s * u**(i-j) * d**j

call = [[0]*T for i in range(T)]
for i in range(T):
    for j in range(T):
        if i == 0:
            call[T-i-1][j] = max(price[T-i-1][j] - x, 0)
        elif j+1 <= T-1:
            call[T-i-1][j] = (p*call[T-i][j] + (1-p)*call[T-i][j+1])*R2
put= [[0]*T for i in range(T)]
for i in range(T):
    for j in range(T):
        if i == 0:
            put[T-i-1][j] = max(x - price[T-i-1][j], 0)
        elif j+1 <= T-1:
            put[T-i-1][j] = (p*put[T-i][j] + (1-p)*put[T-i][j+1])*R2

print('買權價格: ', call[0][0])
print('賣權價格: ', put[0][0])





