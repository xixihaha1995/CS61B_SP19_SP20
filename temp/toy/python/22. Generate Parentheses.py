class Solution {
public:
    vector < string > generateParenthesis(int


n) {
    vector < string > ans;
string
cur;
if (n > 0)
dfs(n, n, cur, ans);
return ans;

}
private:
void
dfs(int
l, int
r, string & s, vector < string > & ans){
if (l + r == 0){
ans.push_back(s);
return;
}
if (l > r)
    return;
if (l > 0) {
dfs(l-1, r, s += "(", ans);
s.pop_back();
}
if (r > 0) {
dfs(1, r-1, s += ")", ans);
s.pop_back();
}

}
};