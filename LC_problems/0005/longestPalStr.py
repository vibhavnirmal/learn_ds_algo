# https://www.youtube.com/watch?v=y2BD4MJqV20
def longestPalindrome(s):
    p = ''
        
    def get_palindrome_from_middle(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    for i in range(len(s)):
        p2 = get_palindrome_from_middle(s, i, i) # for odd
        p1 = get_palindrome_from_middle(s, i, i+1) # for even
                
            
        p = max([p, p1, p2], key=len)
    return p


print(longestPalindrome("babad"))
print(longestPalindrome(s = "cbbd"))
                
