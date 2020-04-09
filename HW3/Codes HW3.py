import math

s = int(input('Stock Price: '))
x = int(input('Strike Price: '))
r = float(input('Riskless Interest Rate(%): '))/100
T = int(input('Time Periods: ')) + 1
R = math.exp(r)
R2 = math.exp(-r)
u = 1.5
d = 0.5
p = (R - d)/(u - d) #risk-neutral probability
if p < 0:
    p = 0
if p > 1:
    p = 1
call = [[0]*T for i in range(T)]
for i in range(T):
    for j in range(i+1):
        call[i][j] = s * u**(i-j) * d**j

f = [[0]*T for i in range(T)]
for i in range(T):
    for j in range(T):
        if i == 0:
            f[T-i-1][j] = max(call[T-i-1][j] - x, 0)
        elif j+1 <= T-1:
            f[T-i-1][j] = (p*f[T-i][j] + (1-p)*f[T-i][j+1])*R2

print(f[0][0])