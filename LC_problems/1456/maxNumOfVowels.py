def maxVowels(s, k):
    vowels = "aeiou"
    maxCount, count = 0, 0

    for i in range(len(s)):
        if i >= k and s[i-k] in vowels: 
            count-=1
        if s[i] in vowels:
            count +=1
        maxCount = max(maxCount, count)

    return maxCount

if __name__ == "__main__":
    print(maxVowels(s = "abciiidef", k = 3))
    print(maxVowels(s = "aeiou", k = 2))
    print(maxVowels(s = "leetcode", k = 3))
    print(maxVowels("weallloveyou", 7))