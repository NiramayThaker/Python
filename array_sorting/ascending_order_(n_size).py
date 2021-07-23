num = []    
array_size = int(input("Enter size of array: "))

for i in range(0, array_size):
    digit = int(input(f"Enter digit-{i+1}: "))
    num.append(digit)

print(f"\nBefor sorting:\n{num}\n")
for i in range(0, array_size):
    for j in range(0, array_size):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]
            print(num)

print(f"\nFinal sorted array in Acending Order:\n{num}\n")
