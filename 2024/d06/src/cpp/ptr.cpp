#include <iostream>
using namespace std;

int main() {
  string name;
  cin >> name;

  auto fn = [&]() -> bool {
    cout << "Hello " << name << endl;
    return true;
  };
  fn();

  return 0;
}
