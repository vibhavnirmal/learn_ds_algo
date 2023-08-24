#include <vector>
#include <string>
using namespace std;

vector<string> fullJustify(vector<string> &words, int maxWidth) {
    vector<string> paragraph;
    int currentLineWidth = 0;
    vector<string> row;
    for (int i = 0; i < words.size(); ++i) {
        string word = words[i];
        if (currentLineWidth + word.size() + row.size() <= maxWidth) {
            row.push_back(word);
            currentLineWidth += word.size();
        } else {
            int spaces = maxWidth - currentLineWidth;
            int extra_spaces = row.size() - 1;

            string r;
            if (extra_spaces == 0) {
                r = row[0] + string(spaces, ' ');
            } else {
                int equal_space = spaces / extra_spaces;
                int extra_space = spaces % extra_spaces;
                for (int i = 0; i < extra_spaces; ++i) {
                    r += row[i] + string(equal_space, ' ');
                    if (extra_space > 0) {
                        r += " ";
                        extra_space -= 1;
                    }
                }
                r += row[row.size() - 1];
            }

            paragraph.push_back(r);
            row.clear();
            row.push_back(word);
            currentLineWidth = word.size();
        }
    }

    string last_line = "";
    for (int i = 0; i < row.size(); ++i) {
        last_line += row[i];
        if (i < row.size() - 1) {
            last_line += " ";
        }
    }
    last_line += string(maxWidth - last_line.size(), ' ');
    paragraph.push_back(last_line);

    return paragraph;
}

int main(){
    vector<string> words = {"ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"};
    int maxWidth = 16;
    vector<string> paragraph = fullJustify(words, maxWidth);

    for (int i = 0; i < paragraph.size(); ++i) {
        printf("%s\n", paragraph[i].c_str());
    }

    return 0;
}