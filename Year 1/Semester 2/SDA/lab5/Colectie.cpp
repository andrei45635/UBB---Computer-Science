#include "Colectie.h"
#include "IteratorColectie.h"

#include <iostream>

using namespace std;

bool rel(TElem e1, TElem e2)
{
	return e1 <= e2;
}

// O(n) - capacitatea curenta a colectiei
void Colectie::resize()
{
	// redimensionare pentru cele 3 tablouri
	TComparabil* new_elems = new TComparabil[cp * 2];
	int* new_drept = new int[cp * 2];
	int* new_stang = new int[cp * 2];
	for (int i = 0; i < cp; i++)
	{
		new_elems[i] = elems[i];
		new_drept[i] = drept[i];
		new_stang[i] = stang[i];
	}

	// dealoc spatiul pentru tablourile ant si le init
	delete elems;
	delete drept;
	delete stang;

	elems = new_elems;
	drept = new_drept;
	stang = new_stang;

	// reinitializez lista de spatii libere
	for (int i = cp; i < cp * 2 - 1; i++)
		drept[i] = i + 1;

	stang[cp * 2 - 1] = -1;
	primLiber = cp;
	cp = cp * 2;
}

int Colectie::aloca()
{
	int p = primLiber;
	primLiber = drept[primLiber];
	return p;
}

void Colectie::dealoca(int p)
{
	drept[p] = primLiber;
	stang[p] = -1;
	primLiber = p;
}

// O(n) - capacitatea curenta a colectiei
int Colectie::creeazaNod(TElem e)
{
	if (size >= cp)
		resize();

	int p = aloca();
	elems[p] = std::make_pair(e, 1);
	stang[p] = -1;
	drept[p] = -1;
	return p;
}

/*
* subalgoritm stergeAparitiiMultiple(int nr, TElem elem)
*	daca nr < 0 sau nrAparitii(elem) < nr atunci
*		arunca exceptie
*	sfDaca
*	pentru i = 0, n, 1 executa
*		sterge(elem)
*	sfPentr
* sfSubalgoritm
*/

void Colectie::stergeAparitiiMultiple(int nr, TElem elem)
{
	if (nr < 0 || nrAparitii(elem) < nr)
		throw exception();

	if (cauta(elem))
		for (int i = 0; i < nr; i++)
			sterge(elem);
	else
		return;
}

Colectie::Colectie()
{
	/*
	* CF: O(n)
	* CD: O(n)
	* CG: O(n)
	* CM: O(n)
	*/
	cp = CAPACITY;
	size = 0;

	elems = new TComparabil[cp];
	stang = new int[cp];
	drept = new int[cp];
	rad = -1;

	for (int i = 0; i < cp - 1; i++)
	{
		drept[i] = i + 1;
		stang[i + 1] = i;
	}
	stang[0] = -1;
	drept[cp - 1] = -1;
	primLiber = 0;
}

void Colectie::adauga(TElem e)
{
	/*
	* CF: O(n)
	* CD: O(n)
	* CG: O(n)
	* CM: O(n)
	*/
	size++;
	// daca colectia e vida
	if (rad == -1)
	{
		rad = creeazaNod(e);
		return;
	}
	// parcurg arborele pana gasesc locul de adaugat
	int pos = rad;
	int parent = pos;
	while (pos != -1)
	{
		parent = pos;

		// daca elementul exista deja incrementez frecventa
		if (e == elems[pos].first)
		{
			elems[pos].second++;
			return;
		}

		// daca este in relatie cu elementul curent parcurg subarborele stang, altfel pe cel drept
		if (rel(e, elems[pos].first))
			pos = stang[pos];
		else
			pos = drept[pos];
	}

	// creez noul nod si subarborii
	int p = creeazaNod(e);
	if (rel(e, elems[parent].first))
		stang[parent] = p;
	else
		drept[parent] = p;
}

int Colectie::minim(int p)
{
	while (p != -1)
		p = stang[p];

	return p;
}

bool Colectie::stergeRec(int curent, int anterior, TElem e)
{
	/*
	* CF: O(n)
	* CD: O(n)
	* CG: O(n)
	* CM: O(n)
	*/
	// daca am ajuns la un subarbore vid
	if (curent == -1)
		return false;

	// daca am ajuns la elementul de sters
	if (elems[curent].first == e)
	{
		size--;
		// daca elementul are mai mult de o singura aparitie, decrementez frecventa
		if (elems[curent].second > 1)
		{
			elems[curent].second--;
			return true;
		}
		// daca nodul are si subarbore stang si drept
		else if (stang[curent] != -1 && drept[curent] != -1)
		{
			int min = minim(drept[curent]);
			elems[curent] = elems[min];
			return stergeRec(drept[curent], curent, elems[min].first);
		}
		// daca nodul este o frunza
		else if (stang[curent] == -1 && drept[curent] == -1)
		{
			if (curent == rad)
				rad = -1;
			else
			{
				if (stang[anterior] == curent)
					stang[anterior] = -1;
				else
					drept[anterior] = -1;
			}
		}
		// daca nodul are un singur fiu, stang
		else if (stang[curent] == -1)
		{
			if (anterior == -1)
				rad = drept[curent];
			else if (stang[anterior] == curent)
				stang[anterior] = drept[curent];
			else
				drept[anterior] = drept[curent];
		}
		// daca nodul are un singur fiu, drept
		else
		{
			if (anterior == -1)
				rad = stang[curent];
			else if (stang[anterior] == curent)
				stang[anterior] = stang[curent];
			else
				drept[anterior] = stang[curent];
		}
		dealoca(curent);
		return true;
	}

	// daca este in relatie cu elementul curent parcurg subarborele stang, altfel pe cel drept
	if (rel(e, elems[curent].first))
		return stergeRec(stang[curent], curent, e);
	else
		return stergeRec(drept[curent], curent, e);
}

bool Colectie::sterge(TElem e)
{
	/*
	* CF: O(n)
	* CD: O(n)
	* CG: O(n)
	* CM: O(n)
	*/
	return stergeRec(rad, -1, e);
}

int Colectie::eliminaRec(int curent, int anterior, TElem e)
{
	/*
	* CF: O(n)
	* CD: O(n)
	* CG: O(n)
	* CM: O(n)
	*/
	// daca am ajuns la un subarbore vid
	if (curent == -1)
		return false;

	// daca sunt la elementul de sters
	if (elems[curent].first == e)
	{
		size--;
		int nrAp;
		// daca nodul are si subarbore stang si drept
		if (stang[curent] != -1 && drept[curent] != -1)
		{
			nrAp = elems[curent].second;
			int min = minim(drept[curent]);
			elems[curent] = elems[min];
			stergeRec(drept[curent], curent, elems[min].first);
			return nrAp;
		}
		// daca nodul este o frunza
		else if (stang[curent] == -1 && drept[curent] == -1)
		{
			if (curent == rad)
				rad = -1;
			else
			{
				if (stang[anterior] == curent)
					stang[anterior] = -1;
				else
					drept[anterior] = -1;
			}
		}
		// daca nodul are un singur fiu, stang
		else if (stang[curent] == -1)
		{
			if (anterior == -1)
				rad = drept[curent];
			else if (stang[anterior] == curent)
				stang[anterior] = drept[curent];
			else
				drept[anterior] = drept[curent];
		}
		// daca nodul are un singur fiu, drept
		else
		{
			if (anterior == -1)
				rad = stang[curent];
			else if (stang[anterior] == curent)
				stang[anterior] = stang[curent];
			else
				drept[anterior] = stang[curent];
		}
		nrAp = elems[curent].second;
		dealoca(curent);
		return nrAp;
	}

	// daca este in relatie cu elementul curent parcurgem subarborele stang, altfel pe cel drept
	if (rel(e, elems[curent].first))
		return eliminaRec(stang[curent], curent, e);
	else
		return eliminaRec(drept[curent], curent, e);
}

// O(n) - inaltimea curenta a arborelui
// cf: theta(1) - elementul este radacina
// cd: theta(n) - elementele sunt adaugate in ordine cresc/desc
// cm: O(log2n) - arborele este aproape de un arbore echilibrat
int Colectie::eliminaToateAparitiile(TElem elem)
{
	return eliminaRec(rad, -1, elem);
}

bool Colectie::cauta(TElem elem) const
{
	/*
	* CF: O(n)
	* CD: O(n)
	* CG: O(n)
	* CM: O(n)
	*/
	// parcurgem arborele pana gasim elementul sau ajungem la capatul arborelui
	int pos = rad;
	while (pos != -1)
	{
		if (elem == elems[pos].first)
			return true;
		// daca este in relatie cu elementul curent parcurgem subarborele stang, altfel pe cel drept
		if (rel(elem, elems[pos].first))
			pos = stang[pos];
		else
			pos = drept[pos];
	}
	return false;
}

int Colectie::nrAparitii(TElem elem) const
{
	/*
	* CF: O(n)
	* CD: O(n)
	* CG: O(n)
	* CM: O(n)
	*/
	// parcurgem arborele
	int pos = rad;
	while (pos != -1)
	{
		// daca am gasit elementul
		if (elem == elems[pos].first)
			return elems[pos].second;
		// daca este in relatie cu elementul curent parcurg subarborele stang, altfel pe cel drept
		if (rel(elem, elems[pos].first))
			pos = stang[pos];
		else
			pos = drept[pos];
	}
	// daca elementul nu a fost gasit
	return 0;
}

int Colectie::dim() const
{
	return size;
}

bool Colectie::vida() const
{
	return size == 0;
}

IteratorColectie Colectie::iterator() const
{
	return IteratorColectie(*this);
}

Colectie::~Colectie()
{
	delete[] elems;
	delete[] stang;
	delete[] drept;
}