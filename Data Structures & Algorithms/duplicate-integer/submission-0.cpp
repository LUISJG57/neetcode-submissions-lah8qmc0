class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> d;
        for (int num : nums) {
            if (d.count(num)) {
                return true;
            }
            d.insert(num);
        }
        return false;
    }
};
