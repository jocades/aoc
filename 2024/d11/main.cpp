#include <bits/stdc++.h>

using namespace std;

void part1(vector<long>& stones) {
  for (int i = 0; i < 25; i++) {
    vector<long> output;
    for (auto n : stones) {
      if (n == 0) {
        output.push_back(1);
        continue;
      }

      string s = to_string(n);
      long len = s.length();
      if (len % 2 == 0) {
        output.push_back(stol(s.substr(0, len / 2)));
        output.push_back(stol(s.substr(len / 2)));
      } else {
        output.push_back(n * 2024);
      }
    }

    stones = output;
    cout << i << ' ' << stones.size() << '\n';
  }
}

map<pair<long, int>, long> cache;
long count(long n, int steps) {
  if (steps == 0) return 1;
  pair<long, int> k = {n, steps};
  if (cache.count(k) == 0) {
    long result;
    if (n == 0) {
      result = count(1, steps - 1);
    } else {
      string s = to_string(n);
      long len = s.length();
      if (len % 2 == 0) {
        result = count(stol(s.substr(0, len / 2)), steps - 1) +
                 count(stol(s.substr(len / 2)), steps - 1);
      } else {
        result = count(n * 2024, steps - 1);
      }
    }
    cache[k] = result;
  }
  return cache[k];
}

int main() {
  vector<long> stones;
  for (long n; cin >> n;) {
    stones.push_back(n);
  }

  long out = 0;
  for (auto n : stones) out += count(n, 75);
  cout << out << endl;
}
