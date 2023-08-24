# 68. Text Justification
# https://leetcode.com/problems/text-justification/

def fullJustify(words, maxWidth):
    currentLineWidth = 0
    row = []
    paragraph = []
    for word in words:
        if currentLineWidth + len(word) + len(row) <= maxWidth:
            row.append(word)
            currentLineWidth += len(word)
        else:
            spaces = maxWidth - currentLineWidth
            extra_spaces = len(row) - 1

            if extra_spaces == 0:
                r = row[0] + " " * spaces
            else:
                equal_space = spaces // extra_spaces
                extra_space = spaces % extra_spaces
                r = ""
                for i in range(extra_spaces):
                    r += row[i] + " " * (equal_space)
                    if extra_space > 0:
                        r += " "
                        extra_space -= 1
                r += row[-1]
                
            paragraph.append(r)
            row = [word]
            currentLineWidth = len(word)

    last_line = " ".join(row)
    last_line += " " * (maxWidth - len(last_line))
    paragraph.append(last_line)

    return paragraph

# print(fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
# print(fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
print(fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))