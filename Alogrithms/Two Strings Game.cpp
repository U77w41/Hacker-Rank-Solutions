#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;
 
#define maxn 300000
#define limit 1000000000000000000LL
 
long long k;
 
int n, m, i, j, cur, bad_value, kk;
char a[maxn], b[maxn];
bool was[30];
pair<int, int> srt[maxn * 2 + 3];
 
struct sfa {
 
    long long dp[maxn * 2 + 3], grundy_sum[30], ways[maxn * 2 + 3];
 
    int next[maxn * 2 + 3][26], len[maxn * 2 + 3], lnk[maxn * 2 + 3], grundy[maxn * 2 + 3];
    int nodes, last, j;
 
    void init () {
        nodes = last = 1;
        len[1] = lnk[1] = 0;
    }
 
    void push (int c) {
        int cur = ++nodes, p;
        len[cur] = len[last] + 1;
        for(p = last; p && !next[p][c]; p = lnk[p]) next[p][c] = cur;
        if (!p) lnk[cur] = 1; else {
            int q = next[p][c];
            if (len[p] + 1 == len[q]) lnk[cur] = q; else {
                int clone = ++nodes;
                len[clone] = len[p] + 1;
                for(int j = 0; j < 26; j++) next[clone][j] = next[q][j];
                lnk[clone] = lnk[q];
                for(; p && next[p][c] == q; p = lnk[p]) next[p][c] = clone;
                lnk[q] = lnk[cur] = clone;
            }
        }
        last = cur;
    }
 
    void grundy_precalc () {
        for(i = 1; i <= nodes; i++) srt[i] = make_pair(len[i], i);
        sort(srt + 1, srt + nodes + 1);
        for(i = 1; i <= nodes; i++) {
            int k = srt[nodes - i + 1].second;
            dp[k] = 1;
            for(j = 0; j < 30; j++) was[j] = 0;
            for(j = 0; j < 26; j++) if (next[k][j]) was[grundy[next[k][j]]] = true;
            for(j = 0; j < 30; j++) if (!was[j]) {
                grundy[k] = j;
                break;
            }
        }        
    }    
 
    void substr_precalc () {
        for(i = 1; i <= nodes; i++) srt[i] = make_pair(len[i], i);
        sort(srt + 1, srt + nodes + 1);
        for(i = 1; i <= nodes; i++) {
            int k = srt[nodes - i + 1].second;
            dp[k] = 1;
            for(j = 0; j < 26; j++) if (next[k][j]) dp[k] += dp[next[k][j]];
        }
        ways[1] = 1;
        for(i = 1; i <= nodes; i++) for(j = 0; j < 26; j++) if (next[srt[i].second][j]) ways[next[srt[i].second][j]] += ways[srt[i].second];
        for(i = 1; i <= nodes; i++) grundy_sum[grundy[i]] += ways[i];
    }
 
    void dp_recalc (int bad_value) {
        for(i = 1; i <= nodes; i++) srt[i] = make_pair(len[i], i);
        sort(srt + 1, srt + nodes + 1);
        for(i = 1; i <= nodes; i++) {
            int k = srt[nodes - i + 1].second;
            dp[k] = grundy[k] != bad_value;
            for(j = 0; j < 26; j++) if (next[k][j]) dp[k] += dp[next[k][j]];
        }
    }
 
} sfa1, sfa2;
 
int main (int argc, char * const argv[]) {
//    freopen("input.txt", "r", stdin);
    scanf("%d %d %lld\n", &n, &m, &k);
 
    sfa1.init();
    sfa2.init();
 
    for(i = 0; i < n; i++) {
        a[i] = getchar();
        while (a[i] < 'a' || a[i] > 'z') a[i] = getchar();
        sfa1.push(a[i] - 'a');
    }
    for(i = 0; i < m; i++) {
        b[i] = getchar();
        while (b[i] < 'a' || b[i] > 'z') b[i] = getchar();
        sfa2.push(b[i] - 'a');
    }
 
    sfa1.grundy_precalc();
    for(i = 1; i <= sfa2.nodes; i++) was[i] = false;
    sfa2.grundy_precalc();
 
    sfa2.substr_precalc();    
 
    for(i = 1; i <= sfa1.nodes; i++) srt[i] = make_pair(sfa1.len[i], i);
    sort(srt + 1, srt + sfa1.nodes + 1);
    for(i = 1; i <= sfa1.nodes; i++) {
        kk = srt[sfa1.nodes - i + 1].second;
        sfa1.dp[kk] = sfa2.dp[1] - sfa2.grundy_sum[sfa1.grundy[kk]];
        for(j = 0; j < 26; j++) if (sfa1.next[kk][j]) {
            sfa1.dp[kk] += sfa1.dp[sfa1.next[kk][j]];
            if (sfa1.dp[kk] > limit) sfa1.dp[kk] = limit;
        }
    }        
 
    if (k > sfa1.dp[1]) {
        puts("no solution");
        return 0;
    }
 
    cur = 1;
    while (k > 0) {
        if (k <= sfa2.dp[1] - sfa2.grundy_sum[sfa1.grundy[cur]]) break; else k -= sfa2.dp[1] - sfa2.grundy_sum[sfa1.grundy[cur]];
        for(j = 0; j < 26; j++) if (k > sfa1.dp[sfa1.next[cur][j]]) k -= sfa1.dp[sfa1.next[cur][j]]; else {
            putchar('a' + j);
            cur = sfa1.next[cur][j];
            break;
        }
    }
    puts("");    
 
    sfa2.dp_recalc(bad_value = sfa1.grundy[cur]);
    cur = 1;
    while (k > 0) {
        if (sfa2.grundy[cur] != bad_value) {
            --k;
            if (k == 0) break;
        }
        for(j = 0; j < 26; j++) if (k > sfa2.dp[sfa2.next[cur][j]]) k -= sfa2.dp[sfa2.next[cur][j]]; else {
            putchar('a' + j);
            cur = sfa2.next[cur][j];
            break;
        }
    }
    puts("");
    return 0;
}