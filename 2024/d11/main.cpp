#include <bits/stdc++.h>

using namespace std;

int main() {
  vector<long> line;
  for (string x; cin >> x;) {
    cout << x << ' ';
    long n = stol(x);
    long len = x.length();
    if (n == 0) {
      line.push_back(1);
    } else if (len > 1 && len % 2 == 0) {
      line.push_back(stol(x.substr(0, len / 2)));
      line.push_back(stol(x.substr(len / 2)));
    } else {
      line.push_back(n * 2024);
    }
  }
  cout << '\n';

  for (int i = 0; i < 24; i++) {
    vector<long> nl;
    for (long n : line) {
      if (n == 0) {
        nl.push_back(1);
        continue;
      }
      string s = to_string(n);
      if (s.length() % 2 == 0) {
        nl.push_back(stol(s.substr(0, s.length() / 2)));
        nl.push_back(stol(s.substr(s.length() / 2)));
      } else {
        nl.push_back(n * 2024);
      }
    }
    line = nl;
  }

  cout << line.size() << endl;
}
