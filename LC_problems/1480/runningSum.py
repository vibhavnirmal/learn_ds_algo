# 1480. Running Sum of 1d Array

def runningSum(nums):
    run = 0
    mylist = []
    for i in nums:
        run+=i
        mylist.append(run)
    return mylist
        
print(runningSum([1,2,3,4]))