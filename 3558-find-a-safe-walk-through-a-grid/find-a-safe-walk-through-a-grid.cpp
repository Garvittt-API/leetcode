class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size(), n = grid[0].size();

        const int INF = 1e9;
        vector<vector<int>> dist(m, vector<int>(n, INF));

        deque<pair<int,int>> dq;

        dist[0][0] = grid[0][0];
        dq.push_front({0, 0});

        int dirs[5] = {-1, 0, 1, 0, -1};

        while (!dq.empty()) {
            auto [x, y] = dq.front();
            dq.pop_front();

            for (int k = 0; k < 4; k++) {
                int nx = x + dirs[k];
                int ny = y + dirs[k + 1];

                if (nx < 0 || ny < 0 || nx >= m || ny >= n)
                    continue;

                int w = grid[nx][ny];

                if (dist[x][y] + w < dist[nx][ny]) {
                    dist[nx][ny] = dist[x][y] + w;

                    if (w == 0)
                        dq.push_front({nx, ny});
                    else
                        dq.push_back({nx, ny});
                }
            }
        }

        return dist[m - 1][n - 1] < health;
    }
};