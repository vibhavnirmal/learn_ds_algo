# Trick Solution

# Time : O(n)
# Space: O(n)

# https://www.youtube.com/watch?v=2qEmA76Unm4
def repeatedSubstringPattern(s):
    d = (s+s)[1:-1]
    return s in d

# -------------------------------------------

# Time : O(n^2)
# Space: O(n)

# https://www.youtube.com/watch?v=bClIZj66dVE
def repeatedSubstringPattern(s):
    d = ""
    for i in range(int(len(s)/2)):
        d += s[i]
        mul = int(len(s) / len(d))
        if d * mul == s:
            # print(d, s)
            return True
    # print(d, s)
    return False


if __name__ == "__main__":
    s = "abab"
    print(repeatedSubstringPattern(s))
    s = "aba"
    print(repeatedSubstringPattern(s))
    s = "bb"
    print(repeatedSubstringPattern(s))
    s = "ababaababa"
    print(repeatedSubstringPattern(s))