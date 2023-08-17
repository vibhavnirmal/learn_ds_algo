# With Prefix and postfix multiplications

def productExceptSelf(nums):
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result
    

# 08/07/2023
# Did it in first try: A bit proud moment.. took almost 20 minutes | But using Div Operation

# Runtime: Beats 88.22%of users with Python3
# Memory: Beats 99.85%of users with Python3

# def productExceptSelf(nums):
#     location = -1
#     total = 1
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] == 0 and count < 2:
#             location = i
#             count += 1
#         if count > 1:
#             return [0 for _ in range(len(nums))]    
#         if nums[i] != 0: 
#             total *= nums[i]
#         else:
#             pass
    
#     if count == 1:
#         nums = [0 for _ in range(len(nums))]
#         nums[location] = total
#     else:
#         for i in range(len(nums)):
#             nums[i] = int(total/nums[i])

#     return nums

print(productExceptSelf(nums = [1,2,3,4]))
# print(productExceptSelf(nums = [-1,1,0,-3,3]))
# print(productExceptSelf(nums = [-1,1,0,-3,3,0]))