// #include <vector>
// #include <iostream>
// #include <algorithm>
#include "headers.h"
class Solution {
public:
  // [[2]                 [[2]
  //  [3, 4]]              [5, 6]
  //  [6, 5, 7]]           [11, 10, 11]
  //  [4, 1, 8, 3]]        [15, 11, 18, 14]]
  
  int minimumTotal(vector<vector<int>>& t) {
    int n = t.size();        
 
    // t[i][j] := minTotalOf(i,j)
    // t[i][j] += min(t[i - 1][j], t[i - 1][j - 1])
 
    for (int i = 0; i < n; ++i)
      for (int j = 0; j <= i; ++j) {
        if (i == 0 && j == 0) continue;
        if (j == 0) t[i][j] += t[i - 1][j];
        else if (j == i) t[i][j] += t[i - 1][j - 1];
        else t[i][j] += min(t[i - 1][j], t[i - 1][j - 1]);
      }
 
    return *std::min_element(begin(t.back()), end(t.back()));
  }

  int main(int argc, char const *argv[])
  {
    /* code */
    Solution s;
    vector<vector<int>> t =     [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
];

    ans = s.minimumTotal();
    cout << ans;

  }
  
};
