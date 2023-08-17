def isPalindrome(s):
    left = 0
    v = "abcdefghijklmnopqrstuvwxyz0123456789"
    v1 = []

    for i in range(len(s)):
        if s[i].lower() in v:
            v1.append(s[i].lower())

    right = len(v1)-1

    while left < right:
        if v1[left] == v1[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
s = "race a car"
print(isPalindrome(s))
s = " "
print(isPalindrome(s))
s = "0P"
print(isPalindrome(s))