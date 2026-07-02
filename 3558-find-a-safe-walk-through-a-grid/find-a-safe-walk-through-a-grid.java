class Solution {
    public boolean findSafeWalk(List<List<Integer>> grid, int health) {
        int m = grid.size();
        int n = grid.get(0).size();

        int[][] best = new int[m][n];
        for (int i = 0; i < m; i++)
            java.util.Arrays.fill(best[i], -1);

        int[] qx = new int[m * n * 100];
        int[] qy = new int[m * n * 100];
        int head = 0, tail = 0;

        int start = health - grid.get(0).get(0);
        if (start <= 0) return false;

        best[0][0] = start;
        qx[tail] = 0;
        qy[tail++] = 0;

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        while (head < tail) {
            int x = qx[head];
            int y = qy[head++];

            int cur = best[x][y];

            if (x == m - 1 && y == n - 1)
                return true;

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx < 0 || ny < 0 || nx >= m || ny >= n)
                    continue;

                int nh = cur - grid.get(nx).get(ny);

                if (nh > 0 && nh > best[nx][ny]) {
                    best[nx][ny] = nh;
                    qx[tail] = nx;
                    qy[tail++] = ny;
                }
            }
        }

        return false;
    }
}