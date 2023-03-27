#include "IteratorColectie.h"
#include "Colectie.h"

using namespace std;

// O(n) - capacitatea curenta
IteratorColectie::IteratorColectie(const Colectie& c) : col(c)
{
	curent = col.rad;
	int anterior = -1;
	// adaug in stiva ramura stanga a elementului curent
	while (curent != -1)
	{
		s.push(curent);
		anterior = curent;
		curent = col.stang[curent];
	}
	// sterg frunza din varful stivei
	if (!s.empty())
	{
		s.pop();
		curent = anterior;
	}
}

TElem IteratorColectie::element()
{
	if (!valid())
		throw exception();

	return col.elems[curent].first;
}

bool IteratorColectie::valid() const
{
	return curent != -1;
}

// O(n) - capacitatea curenta a colectiei
void IteratorColectie::urmator()
{
	if (!valid())
		throw exception();

	// sterg nodul din varful stivei
	if (!s.empty())
	{
		curent = s.top();
		s.pop();
	}
	if (col.drept[curent] != -1)
	{
		curent = col.drept[curent];
		// adaug in stiva ramura stanga a elementului curent
		while (curent != -1) {
			s.push(curent);
			curent = col.stang[curent];
		}
	}
	// sterg nodul din varful stivei
	if (!s.empty())
		curent = s.top();
	else
		curent = -1;
}

// O(n) - capacitatea curenta a colectiei
void IteratorColectie::prim()
{
	// sterg toate elementele adaugate din stiva
	while (!s.empty())
		s.pop();

	curent = col.rad;
	// adaug in stiva ramura stanga a elementului curent
	while (curent != -1)
	{
		s.push(curent);
		curent = col.stang[curent];
	}
	// sterg frunza din varful stivei
	if (!s.empty())
	{
		s.pop();
		curent = s.top();
	}
}