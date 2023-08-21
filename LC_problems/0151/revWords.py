# 151. Reverse Words in a String
# LC 75

def reverseWords(s):
    myList = []
    word = ""
    for i in range(len(s)):
        if s[i] != " ":
            word += s[i]
            if i+1 < len(s):
                if s[i+1] == " ":
                    myList.append(word)
                    word = ""
            else:
                if i == len(s)-1:
                    myList.append(word)  
    return " ".join(myList[::-1])
            

# def reverseWords(s):
#     l = s.split(" ")
#     newL = []
#     for i in l:
#         if i == "":
#             continue
#         else:
#             newL.append(i)
#     return " ".join(newL[::-1])


# def reverseWords(s):
#     return " ".join(s.split()[::-1])

if __name__ == "__main__":
    print(reverseWords("the sky is blue"))
    print(reverseWords("a good   example"))
    print(reverseWords("  hello world  "))
