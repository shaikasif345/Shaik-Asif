def TwoSum(nums,target):
    num_indices = {}
    for i,num in enumerate(nums):
        complement = target-num
        if complement in num_indices:
            return[num_indices[complement],i]
        num_indices[num] = i
    return None
nums = [2,7,11,15]
target = int(input("Enter the target"))
print(TwoSum(nums,target))