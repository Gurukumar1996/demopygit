print("Hello")

#Factorial Numbers


def fact(n):
    f = 1
    for i in range(1,n+1):         # 1*2*3*4*5
        f = f*i
    
    return f

x = 5
result = fact(x)
print(result)
