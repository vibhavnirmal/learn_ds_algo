# https://leetcode.com/problems/contains-duplicate/
# 217. Contains Duplicate


def containsDuplicate(nums) -> bool:
    dictd = {}
    for i in nums:
        if i in dictd:
            return True
        dictd[i] = 1
    return False
            
print(containsDuplicate([3,4,5,6,7]))