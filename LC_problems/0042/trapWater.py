def trap(height):
    if len(height) < 1: return 0
    
    left, right = 0, len(height) - 1
    maxLeft, maxRight = height[left], height[right]
    result = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            maxLeft = max(maxLeft, height[left])
            result += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            result += maxRight - height[right]

    return result


print(trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap(height = [4,2,0,3,2,5]))
print(trap(height = [4,2]))
print(trap(height = []))