#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <bitset>
using namespace std;
ifstream fin("in.txt");
deque <int> q;
bitset <50010> vizc;
int D[50010], Viz[50010];
vector< pair< int, int > > L[50010];

int N, M, i, x, y, z, start;

int main() {
    fin >> N >> M >> start;
    for (i = 1; i <= M; i++) {
        fin >> x >> y >> z;
        L[x].push_back(make_pair(y, z));
    }
    q.push_back(start);
    vizc[start] = 1;
    for (i = 0; i < N; i++)
        D[i] = 1000000;
    D[start] = 0;

    while (q.empty() == 0) {
        x = q.front();
        q.pop_front();
        vizc[x] = 0;
        for (i = 0; i < L[x].size(); i++) {
            y = L[x][i].first;
            if (D[y] > D[x] + L[x][i].second) {
                D[y] = D[x] + L[x][i].second;
                if (vizc[y] == 0) {
                    Viz[y]++;
                    if (Viz[y] == N) {
                        cout << "Ciclu negativ!";
                        return 0;
                    }
                    q.push_back(y);
                    vizc[y] = 1;
                }
            }
        }


    }

    for (i = 0; i < N; i++)
        if (D[i] == 1000000)
            cout << "INF ";
        else
            cout << D[i] << " ";

    return 0;
}