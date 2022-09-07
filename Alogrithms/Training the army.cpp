#include <bits/stdc++.h>

using namespace std;

// Self Template Code BGEIN

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define repf(i,a,b) for (int i = (a); i <= (b); ++i)
#define repd(i,a,b) for (int i = (a); i >= (b); --i)
#define repcase int t, Case = 1; for (scanf ("%d", &t); t; --t)
#define repeach(i,x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)

typedef long long int64;
typedef pair<int, int> pii;

int sgn(double x) { return (x > 1e-8) - (x < -1e-8); }
int count_bit(int x) { return x == 0? 0 : count_bit(x >> 1) + (x & 1); }

template<class T> inline void ckmin(T &a, const T b) { if (b < a) a = b; }
template<class T> inline void ckmax(T &a, const T b) { if (b > a) a = b; }

// Self Template Code END

struct graph {
    static const int maxn = 50 * 30 * 2 + 200 * 30 + 10;
    static const int inf = (-1u) >> 1;

    struct Adj {
        int v, c, b;
        Adj(int _v, int _c, int _b): v(_v), c(_c), b(_b) {}
        Adj() {};
    };
    int i, n, S, T, h[maxn], cnt[maxn];
    vector <Adj> adj[maxn];
    void clear() {
        for (i = 0; i < n; ++i)
            adj[i].clear();
        n = 0;
    }
    void insert(int u, int v, int c, int d = 0) {
        // printf ("insert %d %d %d\n", u, v, c);
        n = max(n, max(u, v) + 1);
        adj[u].push_back(Adj(v, c, adj[v].size()));
        adj[v].push_back(Adj(u, c * d, adj[u].size() - 1));
    }
    int maxflow(int _S, int _T) {
        S = _S, T = _T;
        fill(h, h + n, 0);
        fill(cnt, cnt + n, 0);
        int flow = 0;
        while (h[S] < n)
            flow += dfs(S, inf);
        return flow;
    }
    int dfs(int u, int flow) {
        if (u == T)
            return flow;
        int minh = n - 1, ct = 0;
        for (vector<Adj>::iterator it = adj[u].begin(); flow && it != adj[u].end(); ++it) {
            if (it -> c) {
                if (h[it -> v] + 1 == h[u]) {
                    int k = dfs(it -> v, min(it -> c, flow));
                    if (k) {
                        it -> c -= k;
                        adj[it -> v][it -> b].c += k;
                        flow -= k;
                        ct += k;
                    }
                    if (h[S] >= n)
                        return ct;
                }
                minh = min(minh, h[it -> v]);
            }
        }
        if (ct)
            return ct;
        if (--cnt[h[u]] == 0)
            h[S] = n;
        h[u] = minh + 1;
        ++cnt[h[u]];
        return 0;
    }
};

struct wizard {
    int NA, NB;
    vector<int> A, B;

    void input() {
        scanf ("%d", &NA);
        A.clear();
        rep (i, NA) {
            int bar;
            scanf ("%d", &bar);
            A.push_back(--bar);
        }
        scanf ("%d", &NB);
        B.clear();
        rep (i, NB) {
            int bar;
            scanf ("%d", &bar);
            B.push_back(--bar);
        }
    }
};

const int MAXN = 200 + 2;
const int MAXW = 50 + 2;

wizard wizards[MAXW];
graph g;
int num[MAXN];
int n, w;

int get_level_id(int x, int y) {
    return y * n + x + 2;
}

int solve() {
    // build graph

    // 0 : clear
    g.clear();
    int S = 0, T = 1;

    // 1 : build level
    rep (i, n) {
        rep (j, w) {
            g.insert (get_level_id(i, j), get_level_id(i, j + 1), graph::inf);
        }
    }
    rep (i, n) {
        if (num[i]) g.insert (S, get_level_id(i, 0), num[i]);
        g.insert (get_level_id(i, w), T, 1);
    }

    // 2 : build transform edge
    int vertex_cnt = get_level_id(n - 1, w) + 1;
    map<int, int> in_vertex_id, out_vertex_id;
    rep (i, w) {
        rep (j, wizards[i].NA) {
            g.insert (get_level_id(wizards[i].A[j], i), vertex_cnt, 1);
            in_vertex_id[wizards[i].A[j]] = vertex_cnt++;
        }
        rep (j, wizards[i].NB) {
            g.insert (vertex_cnt, get_level_id(wizards[i].B[j], i + 1), 1);
            out_vertex_id[wizards[i].B[j]] = vertex_cnt++;
        }
        rep (j, wizards[i].NA) {
            rep (k, wizards[i].NB) {
                g.insert (in_vertex_id[wizards[i].A[j]], out_vertex_id[wizards[i].B[k]], 1);
            }
        }
    }

    return g.maxflow(S, T);
}

int main() {
    while (scanf ("%d%d", &n, &w) != EOF) {
        rep (i, n) {
            scanf ("%d", &num[i]);
        }
        rep (i, w) {
            wizards[i].input();
        }

        printf ("%d\n", solve());
    }
    return 0;
}