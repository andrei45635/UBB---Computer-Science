#include <iostream>
#include <fstream>
ifstream f("in.txt");
int n= 0, m, viz[22], A[22][22];

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
	n = 1;
	int z, y;
	while (f >> z)
	{
		while (f >> y)
		{
			L[z][n] = 1;
			L[y][n] = 1;
		}
	}
	f >> m; //nr varfuri
	for (i = 1; i <= m; i++)
		for (j = 1; j <= m; j++)
		{
			A[i][j] = 0;
		}
	while (f >> i >> j)
	{
		A[i][j] = 1;
		A[j][i] = 1;
		n++; //n este numarul de muchii
	}
	for (i = 1; i <= m; i++)
		for (j = 1; j <= n; j++)
			K[i][j] = 0;
	int x = 1;
	for (i = 1; i <= m; i++)
		for (j = 1; j <= n; j++)
		{
			if (A[i][j] == 1 && A[i][j] == A[i + 1][j - 1])
			{
				K[i][x] = 1;
				K[j][x] = 1;
				x++;
			}
			else if (A[i][j] == 0 && A[i][j] == A[i + 1][j - 1])
				K[i][j] = 0;
		}
	std::cout << n << " " <<m;
	std::cout << std::endl;

	int s1 = 0;
	bool ok = false; //pp ca graful nu e regular
	for (i = 1; i <= m; i++)
	{
		for (j = 1; j <= m; j++)
		{
			s1 += A[i][j];
			A[i][0] = s1;
		}
		std::cout << "suma liniei " << i << " este " << s1 << std::endl;
		if (s1 == 0)
			std::cout << "varful " << i << " este izolat deci graful nu poate fi regular" << std::endl;
		else if (A[i-1][0] == s1)
			ok = true; //graful e regular
		s1 = 0;
	}
	if (ok)
		std::cout << "Graf regular" << std::endl;
	std::cout << std::endl;

	//construim matricea drumurilor
	for(i=1;i<=m;i++
		for (j = 1; j <= m; j++
		{
			if(i!=j && A[i][j] == 0)
				D[i][j] =INF;
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
				if (A[i][k] != NULL && A[k][j] != NULL)
				{
					if (A[i][j] > A[i][k] + A[k][j])
					{
						A[i][j] = A[i][k] + A[k][j];
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

	cout << "Matricea de adiacenta este: " << std::endl;
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
	std::cout << endl;
	std::cout << "Lista de adiacenta este: " << std::endl;
	for (i = 1; i <= m; i++)
	{
		for (j = 1; j <= n; j++)
			std::cout << D[i][j] << " ";
		std::cout << std::endl;
	}
	f.close();
	return 0;
}