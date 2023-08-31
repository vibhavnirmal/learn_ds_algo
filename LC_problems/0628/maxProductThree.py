# 628. Maximum Product of Three Numbers
# Easy

# Sorting
# Time O(nlogn)
# Space O(1)
def maximumProduct(nums):
    nums.sort()
    return max(nums[-3]*nums[-2]*nums[-1], nums[0]*nums[1]*nums[-1])

# Find 2 min and 3 max
# Time O(n)
# Space O(1)
def maximumProduct(nums):
    max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')

    for num in nums:
        if num >= max1:
            max3, max2, max1 = max2, max1, num
        elif num >= max2:
            max3, max2 = max2, num
        elif num >= max3:
            max3 = num

        if num <= min1:
            min2, min1 = min1, num
        elif num <= min2:
            min2 = num

    return max(max1 * max2 * max3, min1 * min2 * max1)

print(maximumProduct(nums = [1,2,3]))
print(maximumProduct(nums = [1,2,3,4]))
print(maximumProduct(nums = [-1,-2,-3]))