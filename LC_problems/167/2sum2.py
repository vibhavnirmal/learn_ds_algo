def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1
    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] < target:
            left += 1

print(twoSum(numbers = [2,7,11,15], target = 9))
print(twoSum(numbers = [2,3,4], target = 6))
print(twoSum(numbers = [-1,0], target = -1))