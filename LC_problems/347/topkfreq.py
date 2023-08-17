def topKFrequent(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1

    print(sorted(d.items(), key=lambda x: x[1], reverse=True))

    frequency = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    result = list(frequency.keys())[:k]
    return result

if __name__ == "__main__":
    print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    # print(topKFrequent([-1,-1], 1))