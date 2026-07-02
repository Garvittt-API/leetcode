class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size(), n = grid[0].size();

        static int best[50][50];
        memset(best, -1, sizeof(best));

        queue<pair<int,int>> q;

        int start = health - grid[0][0];
        if (start <= 0) return false;

        best[0][0] = start;
        q.push({0,0});

        int dx[4]={1,-1,0,0};
        int dy[4]={0,0,1,-1};

        while(!q.empty()){
            auto [x,y]=q.front();
            q.pop();

            int cur=best[x][y];

            if(x==m-1 && y==n-1) return true;

            for(int k=0;k<4;k++){
                int nx=x+dx[k];
                int ny=y+dy[k];

                if(nx<0||ny<0||nx>=m||ny>=n) continue;

                int nh=cur-grid[nx][ny];

                if(nh<=0) continue;

                if(nh>best[nx][ny]){
                    best[nx][ny]=nh;
                    q.push({nx,ny});
                }
            }
        }

        return false;
    }
};