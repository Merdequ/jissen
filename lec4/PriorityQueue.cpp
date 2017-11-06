#include <queue>
#include <string>
#include <iostream>
using namespace std;

int main() {
  int num;
  string cmd; // whileの外側で定義して一つの変数を再利用する
  priority_queue<int> Q;
  while (cin >> cmd && cmd != "end") {
    if (cmd == "insert") {
      cin >> num;
      Q.push(num);
    }
    else if (cmd == "extract") {
      cout << Q.top() << endl;
      Q.pop();
    }
  }
  return 0;
}

