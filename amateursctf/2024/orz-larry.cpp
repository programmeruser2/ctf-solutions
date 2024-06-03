#include <bits/stdc++.h>
#define rep(i,a,b) for(int i=(a);i<=(b);++i)
#define per(i,a,b) for(int i=(a);i>=(b);--i)
#define pii pair<int,int>
#define vi vector<int>
#define fi first
#define se second
#define pb push_back
#define ALL(x) x.begin(),x.end()
#define sz(x) int(x.size())
#define ll long long
using namespace std;
const int N = 2e5+5, P=1e9+9;
string S;
ll sum;
map <char,ll> dp;
int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin >> S;
    sum = dp[S[0]] = 1;
    rep(i,1,size(S) - 1){
        ll tmp = sum;
        //new sum
        sum = (sum - dp[S[i]] + (sum + 1)) % P;
        //new # of subsequence end at c
        dp[S[i]] = (tmp + 1) % P;

    }
    cout << sum << endl;
    return 0;
}
