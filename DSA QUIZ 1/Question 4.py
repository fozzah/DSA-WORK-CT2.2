def check_for_non_duplicates(nums:list) -> int:
    for i in nums:
        times_appeared=nums.count(i)
        if times_appeared == 1:
            return i
        
nums:list= [65,34,23,65,34,23,56]
result = check_for_non_duplicates(nums)
print(f"The unique numbers are: {result}")        