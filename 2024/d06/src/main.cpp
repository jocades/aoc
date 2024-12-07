#include "stdc++.h"

void version() {
  if (__cplusplus == 202101L)
    std::cout << "C++23";
  else if (__cplusplus == 202002L)
    std::cout << "C++20";
  else if (__cplusplus == 201703L)
    std::cout << "C++17";
  else if (__cplusplus == 201402L)
    std::cout << "C++14";
  else if (__cplusplus == 201103L)
    std::cout << "C++11";
  else if (__cplusplus == 199711L)
    std::cout << "C++98";
  else
    std::cout << "pre-standard C++." << __cplusplus;
  std::cout << "\n";
}

int main() {
  version();

  vector<string> grid;

  string line;
  while (getline(cin, line)) {
    grid.push_back(line);
  }
  int rows = grid.size();
  int cols = grid[0].size();
  cout << "rows=" << rows << ' ' << "cols=" << cols << '\n';

  pair<int, int> me{-1, -1};
  for (int r = 0; r < rows; r++) {
    for (int c = 0; c < cols; c++) {
      if (grid[r][c] == '^') {
        me = make_pair(r, c);
        cout << "me " << r << ' ' << c << '\n';
        break;
      }
    }
  }

  pair<int, int> dirs[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

  int d = 0;
  set<pair<int, int>> seen;

  while (true) {
    seen.insert(me);

    int nr = me.first + dirs[d].first;
    int nc = me.second + dirs[d].second;
    if (!(0 <= nr && nr < rows && 0 <= nc && nc < cols)) {
      break;
    }
    if (grid[nr][nc] == '#') {
      d = (d + 1) % 4;
    } else {
      me = {nr, nc};
    }
  }

  cout << seen.size() << '\n';
}
