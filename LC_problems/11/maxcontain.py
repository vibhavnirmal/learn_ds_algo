# 11. Container With Most Water
# Medium

def maxArea(height):
    left, right = 0, len(height)-1
    maxArea = 0

    while left<right:
        maxArea = max(maxArea, (right-left) * min(height[left], height[right]))
        if height[left] < height[right]: left += 1
        else: right-=1
            

    return maxArea


if __name__ == "__main__":
    print(maxArea(height = [1,2,7,8]))
    # print(maxArea(height = [1,1]))