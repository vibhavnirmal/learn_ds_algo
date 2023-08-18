def longestConsecutive(nums):
    numsSet = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in numsSet:
            currSeq = 0
            while num + currSeq in numsSet:
                currSeq += 1
            longest = max(longest, currSeq)

    return longest


print(longestConsecutive(nums = [100,4,200,1,3,2]))
print("----")
print(longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print("----")
print(longestConsecutive(nums= [0,0,-1]))
print("----")
print(longestConsecutive(nums= [9,1,4,7,3,-1,0,5,8,-1,6]))
print("----")