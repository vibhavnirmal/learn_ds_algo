# 767. Reorganize String
# https://leetcode.com/problems/reorganize-string/

# Daily Challenge 08/23/2023

"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

# hint:

# Data Structure: Priority queue / MaxHeap

# if maxOccChar > len(s) + 1: return "" 


from collections import Counter

def reorganizeString(s):
    # Count values
    myHash = Counter(s)

    if max(myHash.values()) > (len(s) + 1)//2:
        return ""

    res = []

    
    
    return res

print(reorganizeString(s = "aab"))
print(reorganizeString(s = "abcddcbaaa"))
print(reorganizeString(s = "aaab"))
print(reorganizeString(s = "aabb"))
print(reorganizeString(s = "a"))
print(reorganizeString(s = "ab"))
print(reorganizeString(s = "aa"))
print(reorganizeString(s = "aabbbb"))
        


