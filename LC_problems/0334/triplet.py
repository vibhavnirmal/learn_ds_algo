def increasingTriplet(nums):
    first = second = float('inf')
    print("-----------")
    for num in nums:
        print(first, second, num)
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False



# BF time limit exceeds
# def increasingTriplet(nums):
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             for k in range(j, len(nums)):
#                 if nums[i] < nums[j] < nums[k] and i!= j and j!=k and i!= k:
#                     print(nums[i], nums[j], nums[k])
#                     return True
#     return False

if __name__ == "__main__":
    print(increasingTriplet(nums = [1,2]))
    print(increasingTriplet(nums = [1,2,3,4,5]))
    print(increasingTriplet(nums = [5,4,3,2,1]))
    print(increasingTriplet(nums = [2,1,5,0,4,6]))
    print(increasingTriplet(nums = [2,4,-2,-3]))
    print(increasingTriplet(nums = [20,100,10,12,5,13]))