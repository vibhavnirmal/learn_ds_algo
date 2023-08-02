# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings


def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d1, d2 = {}, {}

    for i in range(len(s)):
        if s[i] not in d1.keys():
            d1[s[i]] = t[i]
        if s[i] in d1.keys():
            if t[i] != d1[s[i]]:
                return False

    for i in range(len(t)):
        if t[i] not in d2.keys():
            d2[t[i]] = s[i]
        if t[i] in d2.keys():
            if s[i] != d2[t[i]]:
                return False

    if d1 == dict((v, k) for k, v in d2.items()):
        return True

    return False


if __name__ == "__main__":
    # s = "egg"
    # t = "add"

    s = "abbaaab"
    t = "baabbab"

    print(isIsomorphic(s, t))
