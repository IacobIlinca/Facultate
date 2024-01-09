#include <iostream>
#include <math.h>
#include <map>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <list>

using namespace std;

string p1(string prop) {
    string t;
    stringstream x(prop);
    string rez = "a";
    while (getline(x, t, ' ')) {
        if (t > rez) {
            rez = t;
        }
    }
    return rez;
}

double p2(int x1, int x2, int y1, int y2) {
    //Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
    // De ex. distanța între (1,5) și (4,1) este 5.0
    return sqrt((x1 + x2) * (x1 + x2) + (y1 + y2) * (y1 + y2));
}

//p3: produs pe coloana si le aduni
int p3(int n, int sir1[], int sir2[]) {
    int prod = 0;
    while (n >= 0) {
        prod += sir1[n] * sir2[n];
        n--;
    }
    return prod;
}

void p4(string prop) {
    string t;
    stringstream x(prop);
    std::map<string, int> dictionar;
    while (getline(x, t, ' ')) {
        dictionar[t]++;
    }
    map<string, int>::iterator it;
    for (it = dictionar.begin(); it != dictionar.end(); it++) {
        if (it->second == 1) {
            cout << it->first << endl;
        }
    }
}

int p5(int n, int sir[]) {
    //Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1}
    // astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
    // De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.
    std::map<int, int> dictionar;
    for (int i = 0; i < n; i++) {
        dictionar[sir[i]]++;
    }

    map<int, int>::iterator it;
    for (it = dictionar.begin(); it != dictionar.end(); it++) {
        if (it->second == 2) {
            return it->first;
        }
    }

//    for (int j = 0; j < dictionar.size(); j++) {
//        if (dictionar[j] == 2) {
//            return j;
//        }
//    }
    return 0;
}

int p6(int n, int sir[]) {
    //Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar (care apare de mai mult de n / 2 ori).
    //De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].
    std::map<int, int> dictionar;
    for (int i = 0; i < n; i++) {
        dictionar[sir[i]]++;
    }

    int max = dictionar[0];
    for (int i = 1; i < dictionar.size(); i++) {
        if (dictionar[i] > n / 2 && dictionar[i] > max) {
            max = i;
        }
    }
    return max;
}


int partition(int arr[], int start, int end) {

    int pivot = arr[start];

    int count = 0;
    for (int i = start + 1; i <= end; i++) {
        if (arr[i] <= pivot)
            count++;
    }

    int pivotIndex = start + count;
    std::swap(arr[pivotIndex], arr[start]);

    int i = start, j = end;

    while (i < pivotIndex && j > pivotIndex) {

        while (arr[i] <= pivot) {
            i++;
        }

        while (arr[j] > pivot) {
            j--;
        }

        if (i < pivotIndex && j > pivotIndex) {
            swap(arr[i++], arr[j--]);
        }
    }

    return pivotIndex;
}

void quickSort(int arr[], int start, int end) {

    if (start >= end)
        return;

    int p = partition(arr, start, end);

    quickSort(arr, start, p - 1);

    quickSort(arr, p + 1, end);
}


int p7(int n, int sir[], int k) {

    quickSort(sir, 0, n - 1);
    return sir[n - k];
}

void p8(int n) {
    for (int i = 1; i <= n; i++) {
        string binar = std::bitset<32>(i).to_string();
        binar = binar.substr(binar.find('1'));
        cout << binar << endl;
    }
}

void p9(int n, int m, int matr[1000][1000], list<pair<pair<int,int>, pair<int,int>>> casute){
    list<pair<pair<int,int>, pair<int,int>>>::iterator it;
    for(it = casute.begin();it!=casute.end();++it){
        pair<int,int> st = it->first;
        pair<int,int> dr = it->second;
        int mini,maxi,maxj, minj;
        if(st.first < dr.first){
            mini = st.first;
            maxi = dr.first;
        } else {mini = dr.first; maxi = st.first;}
        if(st.second < dr.second){
            minj = st.second;
            maxj = dr.second;
        } else {minj = dr.second; maxj = st.second;}

        int suma = 0;
        for(int i=mini; i <= maxi && i<= m;i++){
            for(int j=minj;j<=maxj && j<=n;j++){
                suma+=matr[i][j];
            }
        }
        cout<<suma;
    }
}

int p10(int n, int m, int matr[3][5]){
    int max = 0,poz;
    for(int i=0;i<m;i++){
        int j = n-1, count = 0;
       // cout<<matr[i][j]<<endl;
        while(j>=0 && matr[i][j]==1){
            count++;
            j--;
        }

        if(count >max ) {poz = i; max = count;}
    }
    return poz;
}

int main() {

    while (true) {
        int opt;
        std::cout << "Problema: ";
        std::cin >> opt;

        if (opt == 1) {
            string prop = "Ana are mere rosii si galbene";
            string prop2 = "yellow x zeama";
            std::cout << p1(prop2) << endl;

        } else if (opt == 2) {

            //pt 2
            int x1, y1, x2, y2;
            std::cout << "Coordonatele primei locatii: ";
            std::cout << "x:";
            std::cin >> x1;
            std::cout << "y:";
            std::cin >> y1;

            std::cout << "Coordonatele celei de a doua locatii: ";
            std::cout << "x:";
            std::cin >> x2;
            std::cout << "y:";
            std::cin >> y2;
            std::cout << p2(x1, x2, y1, y2) << std::endl;
            //break;
        } else if (opt == 3) {
            int n = 5;
            int sir1[] = {1, 0, 2, 0, 3}, sir2[] = {1, 2, 0, 3, 1};
            cout << p3(n, sir1, sir2) << endl;
        } else if (opt == 4) {
            string prop = "ana are ana are mere rosii ana";
            p4(prop);

        } else if (opt == 5) {
            //pt 5
            int n = 0, sir[1000];
            std::cout << "Numarul de elemente din sir: ";
            std::cin >> n;
            std::cout << "Elementele sirului: ";
            for (int i = 0; i < n; i++) {
                std::cin >> sir[i];
            }

            std::cout << p5(n, sir) << std::endl;
        } else if (opt == 6) {
            int n, sir[10000];
            std::cout << "Numarul elementelor: ";
            std::cin >> n;
            std::cout << "Elementele sirului: ";
            for (int i = 0; i < n; i++) {
                std::cin >> sir[i];
            }
            std::cout << p6(n, sir) << std::endl;
        } else if (opt == 7) {
            int n, sir[10000], k;
            std::cout << "Numarul elementelor: ";
            std::cin >> n;
            std::cout << "Elementele sirului: ";
            for (int i = 0; i < n; i++) {
                std::cin >> sir[i];
            }
            std::cout << "k: ";
            std::cin >> k;
            std::cout << p7(n, sir, k) << endl;
        } else if (opt == 8) {
            int n = 4;
            p8(n);
//        } else if (opt == 9) {
//            int m = 5, n = 5;
//            int matr[1000][1000] = {
//                    {0,2,5,4,1},
//                    {4,8,2,3,7},
//                    {6,3,4,6,2},
//                    {7,3,1,8,3},
//                    {1,5,7,9,4}
//            };
//            std::list<pair<pair<int,int>, pair<int,int>>> casute;
//            //REVINO!!!
//            p9(n,m,matr,casute);
        }else if(opt == 10){
            int n = 5;
            int m = 3;
            int matr[3][5] = {
                    {0,0,0,1,1},
                    {0,1,1,1,1},
                    {0,0,1,1,1}
            };
            vector<vector<int>> matrice;
//            for(int i=0;i<m;i++){
//                for(int j = 0;j<n;j++){
//                    cout<<matr[i][j]<<" ";
//
//                }
//                cout<<endl;
//            }
            std::cout<<p10(n,m,matr)<<endl;
        }
        else break;
    }
}
