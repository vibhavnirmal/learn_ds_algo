# https://www.youtube.com/watch?v=uvB-Ns_TVis

# https://en.wikipedia.org/wiki/Dutch_national_flag_problem 
# DNF Problem



# Two Pass
def sortColors(nums):
    # Bucket sort- Count values and then replace in the array
    d = {}
    for i in nums:
        if i not in d.keys():
            d[i] = 0
        d[i] += 1
    
    nums.clear()
    # print(d)
    for key, value in sorted(d.items()):
        nums.extend([key] * value)

    print(nums)


    


# One Pass
def sortColors(nums):
    left = 0
    mid = 0
    right = len(nums) - 1

    def swapVals(val1, val2):
        nums[val1], nums[val2] = nums[val2], nums[val1]

    while mid <= right:
        if nums[mid] < 1:
            swapVals(left, mid)
            left += 1
            mid += 1
        elif nums[mid] > 1:
            swapVals(mid, right)
            right -= 1
        else:
            mid += 1
    print(nums)

sortColors(nums = [2,0,2,1,1,0])
# sortColors(nums = [2,0,1])
# sortColors(nums = [0,1,2])
# sortColors(nums = [1,0,2])
# sortColors(nums = [1,0,1])
# sortColors(nums = [0,0,0])
# sortColors(nums = [2,2,1,1,0,0])
# sortColors(nums = [0,1,1,0,2,1,1,0])