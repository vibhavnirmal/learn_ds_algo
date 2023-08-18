def isValid(s):
    myList = []
    for b in s:
        print(myList)
        if b in ["{", "(", "["]:
            myList.append(b)
        else:
            if len(myList) == 0:
                return False
            last = myList.pop()
            if last == "(" and b != ")":
                return False
            if last == "[" and b != "]":
                return False
            if last == "{" and b != "}":
                return False
    return len(myList) == 0       


# print(isValid(s = "()"))
# print(isValid(s = "()[]{}{"))
# print(isValid(s = "(]"))
print(isValid(s = "(()[])"))