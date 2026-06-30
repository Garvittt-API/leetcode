class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            while (true) {
                int x = nums[i];

                if (x < 1 || x > n) break;

                if (nums[x - 1] == x) break;

                swap(nums[i], nums[x - 1]);
            }
        }

        for (int i = 0; i < n; ++i) {
            if (nums[i] != i + 1)
                return i + 1;
        }

        return n + 1;
    }
};