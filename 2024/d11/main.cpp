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

/*

Since we only need to know the **number of stones** produced after X steps
for N number we can cache how many stones will be produced from (N, X).

Let's say number `1` for `3` steps.

1        (1, 3): 4
2024     (2024, 2): 4
20 24    (20, 1): 2, (24, 2): 2
2 0 2 4

Basically caching the arguments to the function and the result that these
arguments produced when the function was called.

*/

map<pair<long, int>, long> cache;
long count(long n, int steps) {
  cout << "stone=" << n << ' ' << "steps=" << steps << '\n';
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
    cout << "cache=" << k.first << ' ' << k.second << " : " << result << '\n';
    cache[k] = result;
  }
  return cache[k];
}

int main() {
  vector<long> stones;
  for (long n; cin >> n;) stones.push_back(n);

  // long out = 0;
  // for (auto n : stones) out += count(n, 75);
  long out = count(2024, 3);
  for (auto const& [k, v] : cache)
    cout << k.first << ' ' << k.second << " : " << v << '\n';
  cout << out << endl;
}
