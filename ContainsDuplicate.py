def ContainsDuplicate(nums):
    a = set()
    for i in nums:
        if i in a:
            return True
        a.add(i)
    return False
nums = [1, 2, 3, 2]
print(ContainsDuplicate(nums))
