import random
def summation(array):
    sum = 0
    for num in array:
        sum += num
    return sum

def maximum(array):
    max = array[0]
    for num in array:
        if num > max:
            max = num
    return max

n = int(input("Enter the length of the array: "))
array = []

for i in range(n):
    num = random.randint(0,n)
    array.append(num)
print(array)

sum = summation(array)
print("The sum of the integers in the array is:", sum)  

max = maximum(array)
print("The largest integer in the array is:", max)