// 542. 01 Matrix
// Medium

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> updateMatrix(vector<vector<int>> &mat)
{
    queue<pair<int, int>> q;

    int height = mat.size();
    int width = mat[0].size();
    

    vector<vector<int>> ans(height, vector<int>(width, -1));

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (mat[i][j] == 0)
            {
                q.push({i, j});
                ans[i][j] = 0;
            }
        }
    }

    // BFS
    while (!q.empty())
    {
        int i = q.front().first;
        int j = q.front().second;

        if (i+1 >= 0 && i+1 < height && j >= 0 && j < width && ans[i + 1][j] == -1)
        {
            q.push({i + 1, j});
            ans[i + 1][j] = ans[i][j] + 1;
        }
        if (i-1 >= 0 && i-1 < height && j >= 0 && j < width && ans[i - 1][j] == -1)
        {
            q.push({i - 1, j});
            ans[i - 1][j] = ans[i][j] + 1;
        }
        if (i >= 0 && i < height && j+1 >= 0 && j+1 < width && ans[i][j + 1] == -1)
        {
            q.push({i, j + 1});
            ans[i][j + 1] = ans[i][j] + 1;
        }
        if (i >= 0 && i < height && j-1 >= 0 && j-1 < width && ans[i][j - 1] == -1)
        {
            q.push({i, j - 1});
            ans[i][j - 1] = ans[i][j] + 1;
        }
        q.pop();
    }

    return ans;
}

int main()
{
    vector<vector<int>> mat = {{0, 1, 0}, {0, 1, 1}, {1, 1, 1}};
    vector<vector<int>> ans;

    ans = updateMatrix(mat);

    int height = mat.size();
    int width = mat[0].size();

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            cout << ans[i][j];
        }
        cout << endl;
    }
}