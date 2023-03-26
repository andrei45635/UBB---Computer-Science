#include <iostream>
#include <fstream>
std::ifstream f("in.txt");
int n = 0, m, viz[22], A[22][22];

void DFS(int x)
{
	int i;
	viz[x] = 1;
	for (i = 1; i <= n; i++)
	{
		if (A[i][x] == 1 && viz[i] == 0)
			DFS(i);
	}
}

int Conex()
{
	int i;
	DFS(1);
	for (i = 1; i <= n; i++)
	{
		if (viz[i] == 0)
			return 0;
	}
	return 1;
}

int main()
{
	int i, j, k, L[22][22], K[22][22], D[22][22];
	const auto INF = 9999;
	//A este matricea de adiacenta
	//L este lista de adiacenta
	//K este matricea de incidenta
	//n este numarul de muchii
	f >> m; //nr varfuri
	for (i = 1; i <= m; i++)
		for (j = 1; j <= m; j++)
		{
			A[i][j] = 0;
			K[i][j] = 0;
		}
	n = 0;
	while (f >> i >> j)
	{
		A[0][i]++;
		A[0][j]++;
		A[i][j] = 1;
		A[j][i] = 1;
		n++; //n este numarul de muchii
		K[i][n] = 1;
		K[j][n] = 1;
	}
	int vf = 0;
	for (i = 1; i <= m; i++)
	{
		for (j = 1; j <= m; j++)
		{
			if (A[0][i] == 0 && A[0][j] == 0)
				vf++;
		}
	}
	std::cout << vf << " varf(uri) izolate" << std::endl;
	int s1 = 0;
	bool ok = true; //pp ca graful e regular
	for (i = 1; i <= m; i++)
	{
		for (j = 1; j <= m; j++)
			if (A[0][i] != A[0][i + 1])
				ok = false;
	}
	if (ok)
	{
		std::cout << "Graf regular" << std::endl;
	}
	else {
		std::cout << "Graful nu este regular" << std::endl;
	}
	//construim matricea drumurilor
	for (i = 1; i <= m; i++)
		for (j = 1; j <= m; j++)
		{
			if (i != j && A[i][j] == 0)
				D[i][j] = INF;
			else if (i == j)
			{
				D[i][j] = 0;
			}
			else
			{
				D[i][j] = A[i][j];
			}
		}
	//roy-floyd
	for (k = 1; k <= n; k++)
	{
		for (i = 1; i <= n; i++)
		{
			for (j = 1; j <= n; j++)
			{
				if (D[i][k] != INF && D[k][j] != INF && i!=j)
				{
					if (D[i][j] > D[i][k] + D[k][j])
					{
						D[i][j] = D[i][k] + D[k][j];
					}
				}
			}
		}
	}
	//conexitate
	if (Conex() == 1)
	{
		std::cout << "Graful este conex" << std::endl;
	}
	else
	{
		std::cout << "Graful nu este conex" << std::endl;
	}

	std::cout << "Matricea de adiacenta este: " << std::endl;
	for (i = 1; i <= m; i++)
	{
		for (j = 1; j <= m; j++)
		{
			std::cout << A[i][j] << " ";
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
	std::cout << "Matricea de incidenta este: " << std::endl;
	for (i = 1; i <= m; i++)
	{
		for (j = 1; j <= n; j++)
		{
			std::cout << K[i][j] << " ";
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
	std::cout << "Matricea drumurilor este: " << std::endl;
	for (i = 1; i <= m; i++)
	{
		for (j = 1; j <= n; j++)
		{
			std::cout << D[i][j] << " ";
		}
		std::cout << std::endl;
	}
	f.close();
	return 0;
}