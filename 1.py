sum1 = 0
for i in range(3,1000):
    if i % 3 == 0:
        sum1 = sum1 + i
print (sum1)

sum2 = 0
for i in range(5,1000):
    if i % 5 == 0:
        sum2 = sum2 + i
print (sum2)


sum3 = 0
for i in range(15,1000):
    if i % 15 == 0:
        sum3 = sum3 + i
print (sum3)


print("")
print(sum1+sum2)
print(sum1+sum2-sum3)
