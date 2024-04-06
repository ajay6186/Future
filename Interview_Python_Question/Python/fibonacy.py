# Q. given N, calculate and return nth fibo num.
# index    0 1 2 3 4 5 6 7  8
# output:  0 1 1 2 3 5 8 13 21

num1 = 0
num2 = 0
result = 0
n= 5
for i in range(0, n+1):
    if i == 0:
       num1 = 0
    if i == 1: 
        num2 = 1
    else:
        result = num1 + num2
        num2 = result
        num1 = num2
    print(num2)