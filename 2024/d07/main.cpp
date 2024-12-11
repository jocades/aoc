#include <iostream>
using namespace std;

int main() {
  int line = 0;
  for (string x; cin >> x;) {
    line++;
    cout << line << ": " << x << endl;
  }
}
