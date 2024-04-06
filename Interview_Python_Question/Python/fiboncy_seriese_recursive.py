# Q. given N, calculate and return nth fibo num.
# index    0 1 2 3 4 5 6 7  8
# output:  0 1 1 2 3 5 8 13 21
import matplotlib.pyplot as plt
def fib_recr(n,depth = 0):
    print( ''.join(["*"]*depth), n)
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib_recr(n-1, depth+1) + fib_recr(n-2, depth+1)

def main():
    print(fib_recr(6))

main()