def MajorityElement(nums):
    count = {}
    for a in nums:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    for a, repeted in count.items():
        if repeted > len(nums) // 2:
            return a
nums = [3, 2, 3,]
print(MajorityElement(nums))
