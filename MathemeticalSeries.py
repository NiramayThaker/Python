# Mathemetical series if 2 then 2+22 output = 24 

num = int(input('Integer value of n :- ')) 
k = num

temp = str(num)

a = []
for i in range(1, k+1):
    a.append(temp*i)

sum = 0

for i in a:
    sum = sum + int(i)

print(sum)
