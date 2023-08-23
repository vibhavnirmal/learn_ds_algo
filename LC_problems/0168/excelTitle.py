# 168. Excel Sheet Column Title

def convertToTitle(columnNumber):
    thecol = ""
    while columnNumber:
        columnNumber -= 1
        remainder = columnNumber % 26
        thecol += chr(ord("A") + remainder )
        columnNumber = columnNumber // 26

    return thecol[::-1]



print(convertToTitle(columnNumber = 1))
print(convertToTitle(columnNumber = 26))
print(convertToTitle(columnNumber = 28))
print(convertToTitle(columnNumber = 701))
print(convertToTitle(columnNumber = 2147483647)) #FXSHRXW