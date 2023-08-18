from collections import defaultdict

def groupAnagrams(strs):
    d = defaultdict(list)
    for word in strs:
        count = [0] * 26 
        for char in word:
            count[ord(char)-ord("a")] +=1 
        print(count)
        
        d[tuple(count)].append(word)
        

    return list(d.values())

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))