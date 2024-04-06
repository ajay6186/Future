# Q. Given a substring check if its palindrame or not ?
# substring ---> continous part of String.
# palindrome is left ot right and right to left is same.

str = 'abmaamcd'

def Ispal(str,s,e):
    result = False

    # 0 1 2 3 4 
    # m a d a m
            
    # 0 1 2 3
    # m a a m
    
    if s>e:
        return True

    if str[s] == str[e] and Ispal(str, s+1, e-1):
        return True
    else:
        return False

print(Ispal(str, 2, 6))