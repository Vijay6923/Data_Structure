#include <iostream>
#include <vector>
#include <algorithm>
#include <climits> // For INT_MIN

using namespace std;

class heap {
public:
    vector<int> a;
    int sz;

    heap() : sz(0) {}

    int parent(int x) {
        return (x - 1) / 2;
    }

    int leftChild(int x) {
        return 2 * x + 1;
    }

    int rightChild(int x) {
        return 2 * x + 2;
    }

    void push(int val) {
        int ind = sz;
        a.push_back(val);
        sz++;
        while (ind != 0) {
            if (a[ind] > a[parent(ind)]) {
                swap(a[ind], a[parent(ind)]);
                ind = parent(ind);
            } else {
                break;
            }
        }
    }

    int top() {
        if (isEmpty()) {
            return INT_MIN;
        }
        return a[0];
    }

    void pop() {
        if (sz == 0) {
            return;
        }
        a[0] = a[sz - 1];
        a.pop_back();
        sz--;
        int ind = 0;
        while (true) {
            int lc = leftChild(ind) < sz ? a[leftChild(ind)] : INT_MIN;
            int rc = rightChild(ind) < sz ? a[rightChild(ind)] : INT_MIN;

            int maximum = max(a[ind], max(lc, rc));
            if (maximum == a[ind]) break;

            if (maximum == lc) {
                swap(a[ind], a[leftChild(ind)]);
                ind = leftChild(ind);
            } else {
                swap(a[ind], a[rightChild(ind)]);
                ind = rightChild(ind);
            }
        }
    }

    bool isEmpty() {
        return size() == 0;
    }

    int size() {
        return sz;
    }
};

signed main() {
    heap h;
    h.push(10);
    h.push(20);
    h.push(5);
    
    cout << "Top element: " << h.top() << endl;
    h.pop();
    cout << "Top element after pop: " << h.top() << endl;

    return 0;
}