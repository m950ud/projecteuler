def f(a):
    if a % 5 == 0 or a % 3 == 0 :
        return a

sum1 = 0       
for i in range (1,1000):
    if f(i):
        sum1 += i
print (sum1)

