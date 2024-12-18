#include <bits/stdc++.h>

using namespace std;

int main() {
  string text;
  cin >> text;

  pair<int, int> me = {0, 0};
  set<pair<int, int>> seen;
  for (char c : text) {
    switch (c) {
      case '^': me.first--; break;
      case '>': me.second++; break;
      case 'v': me.first++; break;
      case '<': me.second--; break;
    }
    seen.insert(me);
  }

  cout << seen.size() + 1 << endl;
}
