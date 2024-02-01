#First Question:
#Remove duplicates from array

numbers:list =[1,2,3,5,8,6,54,197,3,81,3,91,6,6,3,98,2,9,2,6]

for i in numbers:
    repeated = 0
    for idx,x in enumerate(numbers):
        if x == i and repeated<1:
            repeated +=1

    print(f"Repeated {i}, {repeated} times")
print(numbers)