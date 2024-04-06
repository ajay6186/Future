# Q.5 Given N, print all numbers from 1 to N in increasing order.

# def increa(n):
#     if n == 1:
#         print(1)
#         return 
#     increa(n-1)
#     print(n)
# increa(5)

# result_list = []

# def increa_recur(n):
#     if n == 1:
#         result_list.append(1)
#         return
#     increa_recur(n-1)
#     result_list.append(n)

# increa_recur(5)
# print(result_list)

# Q. Given N print all numbers from N to 1 in desc order .?

def descrea(n):
    print(n)
    if n == 1:
        return 
    descrea(n-1)
    
descrea(5)