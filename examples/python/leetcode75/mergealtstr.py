# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately


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


def main():
    print(mergeAlternately("abc", "pqr"))
    print(mergeAlternately("ab", "pqrs"))
    print(mergeAlternately("abcd", "pq"))
    print(mergeAlternately("abcde", "pqr"))
    print(mergeAlternately("abcd", "pqrs"))

if __name__ == "__main__":
    main()