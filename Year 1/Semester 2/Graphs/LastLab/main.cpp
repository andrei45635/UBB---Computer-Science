#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>
using namespace std;
ifstream f("in.txt");
ofstream g("out.txt");

int init_l, n, nr, p[100], c[100];

int determina_frunza_minima(int p[]) {
	bool gasit;
	for (int i = 0; i < init_l; i++) {
		if (p[i] != -2) {
			gasit = false;
			for (int j = 0; j < init_l; j++) {
				if (i == p[j]) gasit = true;
			}
			if (!gasit) return i;
		}
	}
}

void elimina_frunza(int p[], int x) {
	p[x] = -2;
	n--;
}

void prufer() {
	while (n > 1) {
		int x = determina_frunza_minima(p);
		c[nr++] = p[x];
		elimina_frunza(p, x);
	}
}

int min_nr(int c[], int nr) {
	bool aux[100];
	for (int i = 0; i < nr + 1; i++) {
		aux[i] = false;
	}

	for (int i = 0; i < nr; i++) {
		if (c[i] >= 0 && c[i] <= nr) {
			aux[c[i]] = true;
		}
	}

	for (int i = 1; i <= nr; i++) {
		if (!aux[i]) return i;
	}

	return nr + 1;
}

void delete_element(int c[], int size, int pos) {
	for (int i = pos - 1; i < size - 1; i++) {
		c[i] = c[i + 1];
	}
	size--;
}

void insert_element(int c[], int size, int pos, int elem) {
	size++;
	for (int i = size - 1; i > pos; i--) {
		c[i] = c[i - 1];
	}
	c[pos - 1] = elem;
}

void decodare_prufer(int nr) {
	p[c[nr - 1]] = -1;
	for (int i = 0; i < nr - 1; i++) {
		auto x = c[0];
		auto y = min_nr(c, nr);
		p[y] = x;
		delete_element(c, nr, 0);
		insert_element(c, nr, nr, y);
	}
}

int main() {

	f >> n;
	for (int i = 0; i < n; i++) f >> c[i];

	prufer();

	g << nr << '\n';
	for (int i = 0; i < nr; i++) g << c[i] << " ";

	decodare_prufer(n);

	init_l = n + 1;

	g << init_l << '\n';
	for (int i = 0; i < init_l; i++) g << p[i] << " ";

	return 0;
}

