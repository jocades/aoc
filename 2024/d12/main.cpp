#include <bits/stdc++.h>

using namespace std;

using pos = pair<int, int>;

vector<string> g;
int rows, cols;
set<pos> seen;

pos dirs[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

bool inbounds(int r, int c) {
  return 0 <= r && r < rows && 0 <= c && c < cols;
}

void dfs(int r, int c, int& count, int& sides) {
  seen.insert({r, c});
  count++;
  for (pos dir : dirs) {
    int nr = r + dir.first, nc = c + dir.second;
    if (!inbounds(nr, nc) || g[nr][nc] != g[r][c]) {
      sides++;
    } else if (seen.count({nr, nc}) == 0) {
      dfs(nr, nc, count, sides);
    }
  }
}

void dfs2(int r, int c, int& count, int& sides) {
  seen.insert({r, c});
  count++;

  auto isneighbour = [&](pos dir) -> bool {
    int nr = r + dir.first, nc = c + dir.second;
    return inbounds(nr, nc) && g[nr][nc] == g[r][c];
  };

  for (int d = 0; d < 4; d++) {
    pos dir1 = dirs[d];
    pos dir2 = dirs[(d + 1) % 4];
    if (!isneighbour(dir1) && !isneighbour(dir2)) {
      sides++;
    }
    if (isneighbour(dir1) && isneighbour(dir2) &&
        !isneighbour({dir1.first + dir2.first, dir1.second + dir2.second})) {
      sides++;
    }
  }

  for (pos dir : dirs) {
    int nr = r + dir.first, nc = c + dir.second;
    if (isneighbour(dir) && seen.count({nr, nc}) == 0) {
      dfs2(nr, nc, count, sides);
    }
  }
}

int main() {
  for (string line; getline(cin, line);) g.push_back(line);
  rows = g.size();
  cols = g[0].size();

  long out = 0;
  for (int r = 0; r < rows; r++) {
    for (int c = 0; c < cols; c++) {
      if (seen.count({r, c}) != 0) continue;
      int count = 0, sides = 0;
      dfs2(r, c, count, sides);
      printf("start=(%d,%d) count=%d sides=%d\n", r, c, count, sides);
      out += count * sides;
    }
  }

  cout << out << endl;
}
