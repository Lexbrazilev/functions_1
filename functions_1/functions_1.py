def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return factorial(n-1) * n
        
a = int(input("Введите число "))

a1 = factorial(a) 

num = []

for i in range(a1, 0, -1):
    num.append(factorial(i))

print(num)
        
