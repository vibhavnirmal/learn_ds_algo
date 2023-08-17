def canPlaceFlowers(flowerbed , n):
    flowerbed = [0] + flowerbed + [0]

    for i in range(1,len(flowerbed)-1):
        if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
            flowerbed[i] = 1
            n -=1

    if n<=0:
        return True
    else:
        return False
    
if __name__=="__main__":
    print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
    print(canPlaceFlowers(flowerbed = [1,0,0,1], n = 1))
    print(canPlaceFlowers(flowerbed = [1,0,1], n = 1))
    print(canPlaceFlowers(flowerbed = [0,0,0], n = 2))
    print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))