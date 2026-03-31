// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        vector<vector<Pair>> res;
        for(int i=0; i<pairs.size(); i++){
            int l=i-1;
            while(l >= 0 && pairs[l+1].key < pairs[l].key){
                Pair tmp = pairs[l+1];
                pairs[l+1] = pairs[l];
                pairs[l] = tmp;
                l--;
                
            }
            res.push_back(pairs);
            
        }
        return res;
    }
};
