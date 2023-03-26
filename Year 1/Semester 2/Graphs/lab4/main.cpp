#include <iostream>
#include <vector>

using namespace std;

vector<int> nodes, code;

void initNodes(int size)
{
    for (int i = 0; i < size; i++) {
        nodes.push_back(i);
    }
}

int getMin()
{
    for (int node : nodes) {
        bool ok = true;
        for (int elem : code) {
            if (node == elem) {
                ok = false;
                break;
            }
        }
        if (ok) {
            return node;
        }
    }

    return -1;
}

vector<int> decodare_prufer()
{
    vector<int> rez(nodes.size());

    for (int i = 0; i < rez.size(); i++) {
        rez[i] = -1;
    }

    while (!code.empty()) {
        int v = getMin();

        rez[v] = code[0];

        code.erase(code.begin());   
        nodes.erase(remove(nodes.begin(), nodes.end(), v), nodes.end());
    }
    if (nodes.size() == 2) {
        rez[nodes[1]] = rez[nodes[0]];
    }

    return rez;
}

int main()
{
    int k;
    cin >> k;
    initNodes(k+1);
    for (int i = 0; i < k; i++) {
        int x; 
        cin >> x;
        code.push_back(x);
    }

    cout << k + 1 << endl;
    for (auto elem : decodare_prufer()) {
        cout << elem << " ";
    }
}