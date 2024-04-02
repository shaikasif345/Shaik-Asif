def RunningSum(nums):
    running_sum = []
    current_sum = 0
    for a in nums:
        current_sum += a
        running_sum.append(current_sum)
    return running_sum
nums = [1, 2, 3, 4]
print(RunningSum(nums))
