def kidsWithCandies(candies, extraCandies):
    isMax = []
    for i in range(len(candies)):
        if candies[i]+extraCandies >= max(candies):
            isMax.append(True)
        else:
            isMax.append(False)

    return isMax

if __name__ == "__main__":
    print(kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
    print(kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
    print(kidsWithCandies(candies = [12,1,12], extraCandies = 10))