
# Complexity

# Time complexity : O(nlogn)
# Space complexity: O(1)

# Greedy approach
def eraseOverlapIntervals(intervals):
    # we have to find all the intervals that end early this way we can find the maximum number of intervals
    # Sorting array with the last value of each interval
    # Taking example of intervals = [[1,2],[2,3],[3,4],[1,3]]
    
    intervals.sort(key = lambda x:x[1])
    # [[1, 2], [2, 3], [1, 3], [3, 4]]

    # Lets define the count to keep track of all the overlapping regions
    count = 0

    # defining a pointer to previous interval
    # Initially it is the first pointer
    prev = 0

    # Looping through all the intervals
    for i in range(1, len(intervals)):
        
        # If the previous interval's end range is bigger than the current intervals starting range
        # Increase count because we have to remove that interval to have have all non overlapping intervals

        # We do not have to keep track of the intervals so we are not modifying and array
        print(intervals[prev][1], intervals[i][0])
        # 2 2
        # 3 1
        # 3 3
        if intervals[prev][1] > intervals[i][0]:
            count += 1
        else:
            prev = i
            # if the ranges are in order, update the previous interval to the current one
        
    return count






# print(eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
# print(eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
# print(eraseOverlapIntervals(intervals = [[1,2],[2,3]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
