# Date: 08/05/2023

# Approach 1 : Sort both strings and compare
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    if sorted(s) == sorted(t):
        return True
    return False

# Approach 2 : Hashmap, count frequency
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    d = {}
    for i in s:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1

    for j in t:
        if j not in d.keys():
            return False
        else:
            d[j] -= 1
    
    for i in d.values():
        if i != 0:
            return False

    return True
    


print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))