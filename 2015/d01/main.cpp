#include <bits/stdc++.h>

using namespace std;

int main() {
  string input;
  cin >> input;

  int floor = 0;
  int count = 0;
  for (char x : input) {
    if (floor == -1) break;
    if (x == ')') {
      floor--;
    } else {
      floor++;
    }
    count++;
  }

  cout << count << endl;
}
