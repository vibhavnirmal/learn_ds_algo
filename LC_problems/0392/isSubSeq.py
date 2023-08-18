# 392 is subsequence
# Easy

def isSubsequence(s,t):
    ptr1, ptr2 = 0, 0
    while ptr1<len(s) and ptr2<len(t):
        # print(s[ptr1], t[ptr2])
        if s[ptr1] != t[ptr2]:
            ptr2+=1
        elif s[ptr1] == t[ptr2]:
            ptr1+=1
            ptr2+=1
        else:
            break
    # print(ptr1, ptr2)

    if ptr1 == len(s):
        return True
    else:
        return False


if __name__=="__main__":
    s = "abc"
    t = "ahbgdc"

    print(isSubsequence(s,t))