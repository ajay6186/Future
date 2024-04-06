# index:  0 1 2 3 4 5 6 7 8 
# series: 0 1 1 2 3 5 8 13 21 ....
# fib(10)
# fib(10)

def fibself(n):
    num1 = 0
    num2 = 0
    result = 0
    final_result = []
    for i in range(0, n):
        if i == 0:
           num1 = i
           final_result.append(i)

        elif i == 1:
           num2 = i
           final_result.append(i)

        else:
            result = num1 + num2
            num1 = num2
            num2 = result
            final_result.append(result)
    
    return final_result

print(fibself(10))

# global num1
# global num2
# num1 = 0
# num2 = 0
# result = 0
# final_result = []
# index = 0
# store = 0
# def fibself(n):
#         print(n)
#         global num1
#         global num2
#         global index
#         global store

#         if index == 0:
#            num1 = index
#            final_result.append(index)
#            store = n
        
#         elif index == 1:
#            num2 = index
#            final_result.append(index)
        
#         elif store == index:
#              return
           
#         else:
#             result = num1 + num2
#             num1 = num2
#             num2 = result
#             final_result.append(result)
#         index = index + 1
#         return fibself(n-1)

# fibself(10)
# print(final_result)