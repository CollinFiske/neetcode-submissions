#include <map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> stuff;

        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];
            if (stuff.contains(num))
                return true;
            else
                stuff[num] = num;
        }
        return false;
    }
};