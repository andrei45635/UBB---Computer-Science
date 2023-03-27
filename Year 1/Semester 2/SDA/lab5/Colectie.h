#pragma once

#define CAPACITY 100

#include "IteratorColectie.h"

#include <vector>

using namespace std;

typedef int TElem;

typedef std::pair<TElem, int> TComparabil;

typedef bool(*Relatie)(TElem, TElem);

// in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class IteratorColectie;

class Colectie {
	friend class IteratorColectie;
private:
	int cp, size; // capacitatea listelor si nr de elem
	TComparabil* elems; // sir de elem
	int* stang; // sir de fii stangi
	int* drept; // sir de fii drepti
	int rad, primLiber; // referinte catre indexul radacinii si al primului spatiu liber

	// dealoca spatiu pentru un element
	void dealoca(int p);

	// aloca spatiu pentru un nou element
	// returneaza pozitia spatiului nou alocat
	int aloca();

	// redimensioneaza listele
	void resize();

	// functie de creare a unui nou nod in arbore, redimensioneaza daca e nevoie
	// returneaza pozitia pe care e inserat elementul
	int creeazaNod(TElem e);

	// sterge o aparitie a unui element din colectie recursiv
	bool stergeRec(int curent, int anterior, TElem e);

	// elimina toate aparitiile unui element din colectie recursiv
	int eliminaRec(int curent, int anterior, TElem e);

	// returneaza minimul dintr-un subarbore
	int minim(int p);
public:
	// constructorul implicit
	Colectie();

	void stergeAparitiiMultiple(int nr, TElem elem);

	// adauga un element in colectie
	void adauga(TElem e);

	// sterge o aparitie a unui element din colectie
	// returneaza adevarat daca s-a putut sterge
	bool sterge(TElem e);

	// elimina toate aparitiile elementului elem din colectie
	// returneaza numarul de elemente eliminate
	int eliminaToateAparitiile(TElem elem);

	// verifica daca un element se afla in colectie
	bool cauta(TElem elem) const;

	// returneaza numar de aparitii ale unui element in colectie
	int nrAparitii(TElem elem) const;

	// intoarce numarul de elemente din colectie;
	int dim() const;

	// verifica daca colectia e vida;
	bool vida() const;

	// returneaza un iterator pe colectie
	IteratorColectie iterator() const;

	// destructorul colectiei
	~Colectie();
};