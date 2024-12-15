#include <bits/stdc++.h>

using namespace std;

vector<string> g;
int rows, cols;

int main() {
  for (string line; getline(cin, line);) g.push_back(line);
  rows = sz(g);
  cols = sz(g[0]);
}
