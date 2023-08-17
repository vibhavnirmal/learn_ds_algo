# 1768. Merge Strings Alternately
# Easy

# This code takes in two strings and concatenates them alternately. If one string is longer than the other, the remaining letters of the longer string are added to the end of the new string. If both strings are equal in length, the new string will be the two input strings concatenated alternately.

def mergeAlternately(word1, word2):
    newWord = ""
    w1l = len(word1)
    w2l = len(word2)
    if len(word1) > 0 and len(word2) > 0:
        if w1l > w2l:
            for i in range(w2l):
                newWord = newWord + str(word1[i]) + str(word2[i])
            newWord = newWord + word1[w2l::]
            return newWord
        elif w2l > w1l:
            for i in range(w1l):
                newWord = newWord + str(word1[i]) + str(word2[i])
            newWord = newWord + word2[w1l::]
            return newWord
        else:
            for i in range(w1l):
                newWord = newWord + str(word1[i]) + str(word2[i])
            return newWord
    elif len(word2) == 0:
        return word1
    elif len(word1) == 0:
        return word2
    else:
        return ""

if __name__ == "__main__":
    print(mergeAlternately("abc", "pqr"))
    print(mergeAlternately("ab", "pqrs"))
    print(mergeAlternately("abcd", "pq"))
    print(mergeAlternately("abcde", "pqr"))
    print(mergeAlternately("abcd", "pqrs"))