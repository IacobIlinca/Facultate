#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("t.in");
ofstream fout("t.out");
#define inf (1<<30)

int n, t[100005], fii[100005], t2[100005], k, fr[100005];

void codare_prufer() {
	int i, j;
	for (i = 1; i <= n - 1; i++) {
		for (j = 0; j < n; j++) {
			if (fii[j] == 0) {
				break;
			}
		}
		t2[k++] = t[j];
		fii[j]--;
		fii[t[j]]--;
	}
}

void decodare_prufer() {
	int i, j;
	for (i = 0; i < n - 1; i++) {
		for (j = 0; j < n && fr[j] != 0; j++);
		t[j] = t2[i];
		fr[j]++;
		fr[t2[i]]--;
	}
}

int main(int argc, char* argv[]) {
	int i;
	fin >> n;
	for (i = 0; i < n; i++) {
		fin >> t[i];
		fii[t[i]]++;
	}
	codare_prufer();
	fout << n - 1 << '\n';
	for (i = 0; i < n - 1; i++) {
		fout << t2[i] << ' ';
		fr[t2[i]]++;
		t[i] = -1;
	}
	t[n - 1] = -1;
	
	decodare_prufer();
	fout << '\n' << n << '\n';
	for (i = 0; i < n; i++) {
		fout << t[i] << ' ';
	}
	
	return 0;
}


