def lengthOfLongestSubstring(s):
    result = set()
    left = 0
    val = 0
    
    for right in range(len(s)):
        
        while s[right] in result:
            result.remove(s[left])
            left+=1

        result.add(s[right])
        val = max(val, len(result))

    return val
            
# def lengthOfLongestSubstring(s):
#     dic = [-1] * 256
#     max_len = 0
#     start = -1

#     for i in range(len(s)):
#         print(dic)
#         if dic[ord(s[i])] > start:
#             start = dic[ord(s[i])]
#         dic[ord(s[i])] = i
#         max_len = max(max_len, i - start)

#     return max_len

# Aug 31, 2022
# def lengthOfLongestSubstring(s):
#     start, mx= 0,0    # 0: start, mx: maximum length
#     chars = {}        # chars: dictionary of characters

#     for i in range(len(s)):
#         if s[i] in chars and start <= chars[s[i]]:
#             start = chars[s[i]]+1
#         else:
#             mx = max(mx, i-start+1)

#         chars[s[i]] = i
#         print(chars)

#     return mx
        

print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring(s = "bbbbb"))
# print(lengthOfLongestSubstring(s = "pwwkew"))
# print(lengthOfLongestSubstring("dvdf"))