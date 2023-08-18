# Date: ?
# def containsDuplicate(nums) -> bool:
#     dictd = {}
#     for i in nums:
#         if i in dictd:
#             return True
#         dictd[i] = 1
#     return False
            
# print(containsDuplicate([3,4,5,6,7]))

# Date: 08/05/2023
def containsDuplicate(nums):
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1
    for value in d.values():
        if value > 1:
            return True
    return False

print(containsDuplicate([3,4,5,6,7]))