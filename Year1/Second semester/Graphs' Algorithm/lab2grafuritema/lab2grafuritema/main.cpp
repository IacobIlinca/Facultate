#include <iostream>
#include <fstream>
using namespace std;
ifstream f("in.txt");
ofstream g("out.txt");
int fr[100];
int c[100], t[100], dist[100];
int a, b;
int x, y;
int d[101][101], n, m[101][101];
void drum(int nod) {
	if (nod) {
		drum(t[nod]);
		cout << nod << " ";
	}
}

void bfs(int start, int final) {
	fr[start] = 1;
	c[1] = start;
	int p = 1, u = 1;
	while (p <= u) {
		for (int i = 1; i <= n; i++)
			if (m[c[p]][i]) {
				if (fr[i] == 0) {
					c[++u] = i;
					fr[i] = 1;
					t[i] = c[p];
					if (i == final) {
						drum(i);
						return;
					}
				}
			}
		p++;
	}
}

void bfs_nou(int start) {
	fr[start] = 1;
	c[1] = start;
	int p = 1, u = 1;
	while (p <= u) {
		cout << c[p] << " " << dist[c[p]] << "\n";
		for (int i = 1; i <= n; i++)
			if (m[c[p]][i]) {
				if (fr[i] == 0) {
					c[++u] = i;
					fr[i] = 1;
					dist[i] = dist[c[p]] + 1;  //distanta 

				}
			}
		p++;
	}
}


void dfs(int nod) {
	fr[nod] = 1;
	cout << nod << " ";
	for (int i = 1; i <= n; i++)
		if (m[nod][i]) {
			int vecin = i;
			if (!fr[vecin]) {
				dfs(vecin);
			}
		}
}


int main()
{
	f >> n;

	while (f >> x >> y)
	{
		d[x][y] = 1;
		m[x][y] = 1;
	}


	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (d[i][j] == 0 && d[i][k] && d[k][j])
					d[i][j] = 1;


	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			cout << d[i][j] << " ";
		cout << endl;
	}
	cout << "\n";
	cout << "Drumul dintre urmatoarele 2 noduri: ";
	cin >> a >> b;
	bfs(a, b);


	for (int i = 0; i < 100; i++)
	{
		fr[i] = 0;
		t[i] = 0;
	}


	cout << "\n Introduceti nodul sursa:";
	cin >> a;
	bfs_nou(a);

	for (int i = 0; i < 100; i++)
	{
		fr[i] = 0;
	}

	cout << "\n Introduceti nodul sursa:";
	cin >> a;
	dfs(a);

	return 0;
}