# deque (doubly linked list) is used to store the index of the elements in the sliding window
# O(n) time complexity
from collections import deque

def maxSlidingWindow(nums, k):
    pass

# Time limit exceeded 

# O(nk) time complexity
# n is the length of nums, k is the size of the sliding window
def maxSlidingWindow(nums, k):
    if k == 1: return nums
    currMax = max(nums[:k])
    result = [currMax]
    for i in range(1, len(nums)-k+1):
        if nums[i+k-1] > currMax:
            currMax = nums[i+k-1]
        elif currMax == nums[i-1]:
            currMax = max(nums[i:i+k])
        result.append(currMax)

    return result

print(maxSlidingWindow([7,2,4], 2))
print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(maxSlidingWindow(nums = [1], k = 1))
print(maxSlidingWindow(nums = [1,-1], k=1))