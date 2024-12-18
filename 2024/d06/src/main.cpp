#include <bits/stdc++.h>
using namespace std;

// Contains. `c in a..b`
#define cts(a, b, c) (a <= c && c < b)

int main() {
  vector<string> grid;
  string line;
  while (cin >> line) grid.push_back(line);
  int rows = grid.size();
  int cols = grid[0].size();

  pair<int, int> me{-1, -1};
  iter(r, 0, rows) {
    iter(c, 0, cols) {
      if (grid[r][c] == '^') {
        me = {r, c};
        cout << "me " << r << ' ' << c << endl;
        break;
      }
    }
  }

  pair<int, int> dirs[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
  auto is_loop = [&](pair<int, int> me) {
    int d = 0;
    vector<bool> seen(rows * cols * 4);
    loop {
      int k = (me.first * cols + me.second) * 4 + d;
      if (seen[k]) return true;
      seen[k] = true;

      int nr = me.first + dirs[d].first;
      int nc = me.second + dirs[d].second;
      if (!(cts(0, rows, nr) && cts(0, cols, nc))) {
        return false;
      }
      if (grid[nr][nc] == '#') {
        d = (d + 1) % 4;
      } else {
        me = {nr, nc};
      }
    }
  };

  int count = 0;
  iter(r, 0, rows) {
    iter(c, 0, cols) {
      if (grid[r][c] == '.') {
        grid[r][c] = '#';
        if (is_loop(me)) count++;
        grid[r][c] = '.';
      }
    }
  }

  cout << count << endl;
}
