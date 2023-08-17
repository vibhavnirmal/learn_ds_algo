# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Medium


# def maxSubArray(nums) -> int:
#     init = True
#     start = 0
#     end = 0
#     while end < len(nums):
#         if init:
#             maxVal = nums[start]
#             sums = nums[start]
#             end += 1
#             init = False
        
#         print(sums,nums[start], nums[end])

#         if sums + nums[end] > maxVal:
#             sums += nums[end]
#             print(sums ,nums[start], nums[end])
#             if nums[end] > maxVal:
#                 sums = nums[end]
#                 maxVal = nums[end]
#             else:
#                 maxVal = sums
#             end +=1 
#         else:
#             start+=1
#             print(sums,nums[start], nums[end])

#         if start == end:
#             print("start", start, "and end", end)
#             end += 1
#         print("--------------")
#     return maxVal

# maxVal= maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

# print(maxVal)