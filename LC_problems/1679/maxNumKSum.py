# 1679. Max Number of K-Sum Pairs
# Medium


def maxOperations(nums, k):
    left = 0
    right = len(nums) - 1
    count = 0

    (nums).sort()

    while left < right:
        # print(left, ":",nums[left], "AND ",right,":", nums[right])
        if nums[left]+nums[right] == k:
            left+=1
            right-=1
            count += 1

        elif nums[left] + nums[right] < k:
            left+=1
        else:
            right-=1
        

    return count

if __name__ == "__main__":
    print(maxOperations(nums = [1,2,3,4], k = 5))
    print(maxOperations(nums = [3,1,3,4,3], k = 6))
    print(maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))
    print(maxOperations([2,2,2,3,1,1,4,1], 4))