def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    if len(str1) > len(str2):
        return gcdOfStrings(str1[len(str2):], str2)
    elif len(str1) < len(str2):
        return gcdOfStrings(str1, str2[len(str1):])
    else:
        return str1

if __name__ == "__main__":
    # print(gcdOfStrings("ABABAB", "ABABADDSS"))
    print(gcdOfStrings("AA", "AA")) # "A"