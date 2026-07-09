class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        // Fast I/O optimization
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        vector<int> group(n, 0);
        int component_id = 0;
        
        for (int i = 1; i < n; ++i) {
            if (nums[i] - nums[i - 1] > maxDiff) {
                component_id++;
            }
            group[i] = component_id;
        }
        
        vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            ans.push_back(group[q[0]] == group[q[1]]);
        }
        
        return ans;
    }
};