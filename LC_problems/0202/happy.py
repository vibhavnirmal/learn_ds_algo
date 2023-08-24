# Two Pointer approach
# Time: O(logn) and Space: O(1) 
# !!!! Howww beautiful 
# Slow and Fast Pointer
# Floyd's Cycle-Finding Algorithm

def isHappy(n):
    def squared(n):
        result = 0
        while n>0:
            print(n)
            last = n%10
            result += last * last
            n = n//10
        return result

    slow = squared(n)
    fast = squared(squared(n))

    print(slow, fast)

    while slow!=fast and fast!=1:
        slow = squared(slow)
        fast = squared(squared(fast))

    return fast==1

# Space and Time complexity: O(k) => k is iterations required to determine the happy number  
# def isHappy(n):
#     val = str(n)
#     summ = 0
#     d = []
#     while True:
#         for i in range(len(val)):
#             summ += int(val[i])*int(val[i])
#         if summ == 1:
#             return True
        
#         val = str(summ)
#         summ = 0

#         if val not in set(d):
#             d.append(val)
#         else:
#             return False

# print(isHappy(n = 2))
# print(isHappy(n = 8))
print(isHappy(n = 19))
# print(isHappy(n = 3))