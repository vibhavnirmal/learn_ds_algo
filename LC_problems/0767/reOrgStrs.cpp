#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>

using namespace std;

struct Compare{
    bool operator()(pair<char, int> a, pair<char, int> b){
        return a.second < b.second;
    }
};

string reorganizeString(string s)
{

    unordered_map<char, int> mp;
    for (int i = 0; i < s.size(); i++)
        mp[s[i]]++;

    priority_queue<pair<char, int>, vector<pair<char, int>>, Compare> pq;

    for (auto it : mp)
        pq.push({it.first, it.second});

    string ans;
    char prev = '\0';

    while (!pq.empty()){

        pair<char, int> top = pq.top();
        pq.pop();

        if (top.first != prev){
            prev = top.first;
            ans += top.first;
            top.second--;

            if (top.second > 0)
                pq.push(top);

        }
        else if (!pq.empty())
        {
            pair<char, int> top2 = pq.top();
            pq.pop();
            
            prev = top2.first;
            ans += top2.first;
            top2.second--;

            if (top2.second > 0)
                pq.push(top2);

            pq.push(top);
        }
        else
            return "";
    }
    return ans;
}

int main(){
    cout<<reorganizeString("aab")<<endl;
    cout<<reorganizeString("ab")<<endl;
    cout<<reorganizeString("a")<<endl;
    cout<<reorganizeString("aaabcbcbcaa")<<endl;
    cout<<reorganizeString("aaabcbcbcaaaaaa")<<endl;
    
    return 0;
}