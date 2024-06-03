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
const int N = 2e5 + 5;
int n,a[N],dp[N],pre[N];
vector <pii> ans;
int main(){
    //freopen("testdata.txt","r",stdin);
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    rep(i,0,n - 1) cin >> a[i];
    ans.pb({a[0],0}),dp[0] = 1;
    rep(i,0,n - 1)pre[i] = -1;
    rep(i,1,n - 1){
        if(a[i] > ans.back().fi){
            dp[i] = ans.size(),pre[i] = ans.back().se;
            ans.pb({a[i],i});
            continue;
        }
        int j = lower_bound(ALL(ans),make_pair(a[i],0)) - ans.begin();
        ans[j] = {a[i],i};
        dp[i] = j + 1;
        if(j > 0)pre[i] = ans[j - 1].se;
    }
    //cout << ans.size() << endl;
    vi vec;
    int i = ans.back().se;
    while(pre[i] >= 0){
        vec.pb(i);
        i = pre[i];
    }
    vec.pb(i);
    reverse(ALL(vec));
    rep(i,0,vec.size() - 1){
        cout << vec[i] << ' ';
        if(i > 0)assert(a[vec[i]] > a[vec[i - 1]]);
    }
    cout<<"\n";
    return 0;
}
