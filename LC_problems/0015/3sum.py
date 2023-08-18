def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i>0 and nums[i-1]==nums[i]:
            continue 
        left = i+1
        right = len(nums)-1
        while left < right: 
            s = nums[i] + nums[left] + nums[right] 
            if s>0: 
                right-=1 
            elif s<0:
                left += 1 
            else:
                result.append([nums[i],nums[left],nums[right]])
                left += 1 
                while nums[left-1]==nums[left] and left<right: 
                    left += 1   
    return result

# BruteForce
# Exceeded time limit
# def threeSum(nums):
#     mylist = []
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             for k in range(j, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j!=k:
#                     if sorted([nums[i], nums[j], nums[k]]) not in mylist:
#                         mylist.append(sorted([nums[i], nums[j], nums[k]]))
#     return mylist

print(threeSum(nums = [-1,0,1,2,-1,-4]))
print(threeSum(nums = [0,1,1]))
print(threeSum(nums = [0,0,0]))
