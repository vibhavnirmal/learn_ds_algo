# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/description/
def validPalindrome(s):
    left = 0
    right = len(s) - 1
    flag = True

    def checkPal(s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True    

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif checkPal(s, left+1, right) or checkPal(s, left, right-1):
            return True
        else:
            return False
    return True
            
# def validPalindrome(s):
#     p = int(len(s)/2)
#     pp = s[:p]
#     ppp = s[p:]

#     print(pp)
#     print(ppp[::-1])


print(validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))