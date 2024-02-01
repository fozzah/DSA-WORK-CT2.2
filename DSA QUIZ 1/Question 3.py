#Must return true if a number appears more than once

nums: list =[1,2,3]

def check_duplicates(nums:list) -> bool:
    #loop through the list
    nums_appeared = []
    for i in nums:
        if i in nums_appeared:
            return True 
            break
        else:
            nums_appeared.append(i)
        return False 

print(check_duplicates(nums))       