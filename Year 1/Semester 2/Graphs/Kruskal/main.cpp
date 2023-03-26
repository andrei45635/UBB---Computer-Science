#include <iostream>
#include <fstream>
using namespace std;
ifstream f("in.txt");
ofstream g("out.txt");

#define INF 9999

int V, E, G[100][100] = { 0 }, x, y, w;

void Prim() {
	int no_edge = 0;

	int sum = 0;

	bool selected[100];
	memset(selected, false, sizeof(selected));

	selected[0] = true;

	while (no_edge < V - 1) {
		int min = INF;
		for (int i = 0; i < V; i++) {
			if (selected[i]) {
				for (int j = 0; j < V; j++) {
					if ((!selected[j] && G[i][j]) && (min > G[i][j])) {
						min = G[i][j];
						x = i;
						y = j;
					}
				}
			}
		}
		g << x << " - " << y << '\n';
		selected[y] = true;
		no_edge++;
		sum += G[x][y];
	}
	g << sum << '\n';
	g << no_edge << '\n';
}

int main() {

	f >> V >> E;

	while (f >> x >> y >> w) {
		G[x][y] = w;
		G[y][x] = w;
	}

	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			g << G[i][j] << " ";
		}
		g << '\n';
	}

	g << '\n';

	Prim();

	return 0;
}

