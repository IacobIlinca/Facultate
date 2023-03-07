#include<iostream>
#include<fstream>
using namespace std;
ifstream f("noduri.in");
ofstream g("rezultate.out");

int main()
{	
	int n,i,matrice[100][100],j,varfuri[100],st,dr, matr_inc[100][100]={};
	f >> n;
	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
			matrice[i][j] = 0;

	int nr = 0;

	for (i = 1; i <= n; i++)
		varfuri[i] = i;

	while (f >> st && f >> dr)
	{	
		matrice[st][dr] = 1;
		matrice[dr][st] = 1;
		//matrice de incidenta din lista de muchii
		nr++;
		matr_inc[st][nr] = 1;
		matr_inc[dr][nr] = 1;

	}


	
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= n; j++)
			g << matrice[i][j] << " ";
		g << endl;
	}



	g << endl;
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= nr; j++)
			g << matr_inc[i][j] << " ";
		g << endl;
	}

	g << endl;
	g << "Varfurile izolate sunt:";

	for (i = 1; i <= n; i++)
	{
		int ok = 0;
		for (j = 1; j <= n; j++)
			if (matrice[i][j] == 1)
				ok = 1;
		if (ok == 0)
			g << i;
	}

	int suma = 0;
	for (i = 1; i <= n; i++)
		suma += matrice[1][i];

	int reg = 1;
	for (i = 1; i <= n; i++)
	{
		int s = 0;
		for (j = 1; j <= n; j++)
			s += matrice[i][j];
		if (s != suma)
			reg = 0;

	}
	g << endl;

	if (reg == 0)
		g << "Graful este neregular!";
	else
		g << "Graful este regular!";

	g.close();
	return 0;

}

