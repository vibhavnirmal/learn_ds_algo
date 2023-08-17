# https://leetcode.com/problems/zigzag-conversion/
# 6. Zigzag Conversion


class Solution:
    def convert(self, s: str, numRows: int) -> str:
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
    s = Solution()
    # ConvStr = s.convert("A",1)
    ConvStr = s.convert("PAYPALISHIRING",3)           #PAHNAPLSIIGYIR
    # ConvStr = s.convert("PAYPALISHIRING",4)             #PINALSIGYAHRPI
    print(ConvStr)