#include <bits/stdc++.h>

#include <chrono>
#include <deque>
using namespace std;
using namespace std::chrono;

using pos = pair<int, int>;

vector<vector<int>> g;
int rows, cols;

vector<pos> dirs = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
map<pos, set<pos>> m;

void find_peak(pos me, int t, pos start) {
  for (auto dir : dirs) {
    int r = me.first + dir.first;
    int c = me.second + dir.second;

    if (!(0 <= r && r < rows && 0 <= c && c < cols)) continue;
    if (g[r][c] != t) continue;

    if (t == 9) {
      m[start].insert({r, c});
    } else {
      if (t == 1 && m.count(me) == 0) m[start] = {};
      find_peak({r, c}, t + 1, start);
    }
  }
}

int score(pos me) {
  deque<pos> q = {me};
  int summits = 0;
  set<pos> seen;
  while (q.size() > 0) {
    me = q.front();
    q.pop_front();

    for (pos dir : dirs) {
      int r = me.first + dir.first;
      int c = me.second + dir.second;

      if (!(0 <= r && r < rows && 0 <= c && c < cols)) continue;
      if (g[r][c] != g[me.first][me.second] + 1) continue;

      if (seen.count({r, c}) > 0) continue;
      seen.insert({r, c});

      if (g[r][c] == 9) {
        summits++;
      } else {
        q.push_back({r, c});
      }
    }
  }
  return summits;
}

int dfs(pos me, set<pos>& seen) {
  // if (seen.count(me) > 0) return 0;
  // seen.insert(me);
  if (g[me.first][me.second] == 9) return 1;

  int count = 0;
  for (pos dir : dirs) {
    int r = me.first + dir.first;
    int c = me.second + dir.second;
    if (!(0 <= r && r < rows && 0 <= c && c < cols)) continue;
    if (g[r][c] != g[me.first][me.second] + 1) continue;
    count += dfs({r, c}, seen);
  }
  return count;
}

int main() {
  for (string line; getline(cin, line);) {
    vector<int> row;
    for (char n : line) row.push_back(n - '0');
    g.push_back(row);
  };

  rows = sz(g);
  cols = sz(g[0]);

  int out = 0;
  auto start = high_resolution_clock::now();
  for (int r = 0; r < rows; r++) {
    for (int c = 0; c < cols; c++) {
      if (g[r][c] != 0) continue;
      pos me = {r, c};
      set<pos> seen;
      // find_peak(me, 1, me);
      // out += score(me);
      out += dfs(me, seen);
    }
  }

  // for (auto const& [from, to] : m) out += sz(to);

  auto end = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(end - start);

  cout << out << endl;
  cout << "took " << duration.count() << "μs" << endl;
}
