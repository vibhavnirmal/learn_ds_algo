
# Find Length of Maximal set of mutually disjoint intervals
def maxDisjointIntervals(intervals):
    intervals.sort(key=lambda x:x[1])
    # [[1,2],[4,6],[2,10]]
    # [[2,3],[1,4],[4,6],[8,9]]

    count = len(intervals)
    prev = 0
    
    for i in range(1, len(intervals)):
        if intervals[prev][1] > intervals[i][0]:
            count -= 1
        else:
            prev = i
    
    return count

print(maxDisjointIntervals([[1,2],[2,10],[4,6]]))
print(maxDisjointIntervals([[1,4],[2,3],[4,6],[8,9]]))