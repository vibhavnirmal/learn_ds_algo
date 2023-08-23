# https://leetcode.com/problems/zigzag-conversion/
# 6. Zigzag Conversion


def convert(s,numRows):
    listS = []
    for i in range(len(s)):
        if(numRows>=2):
            for j in range(numRows):
                continue
        if(numRows==1):
            listS.append(s)
    
    stringS = "".join(listS)
    return stringS


if __name__=="__main__":

    ConvStr = convert("A",1)
    print(convert("PAYPALISHIRING",3))           #PAHNAPLSIIGYIR
    print(convert("PAYPALISHIRING",4))           #PINALSIGYAHRPI