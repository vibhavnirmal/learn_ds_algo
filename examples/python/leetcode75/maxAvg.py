# 643. Maximum Average Subarray I
# Easy

def findMaxAverage(nums, k):
    newSum = sum(nums[:k])
    maxSum = newSum
    for i in range(k, len(nums)):
        newSum += nums[i] - nums[i-k]
        maxSum = max(maxSum, newSum)
    return maxSum/k

if __name__ == "__main__":
    print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
    print(findMaxAverage(nums = [5], k = 1))