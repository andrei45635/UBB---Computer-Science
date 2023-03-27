#include "Iterator.h"
#include "DO.h"
#include <iostream>

#include <exception>
using namespace std;

DO::DO(Relatie r) {
	/* de adaugat */
	this->cap = 5;
	this->lg = 0;
	this->r = r;
	elems = new TElem[cap];
	//am alocat dinamic vector de elemente
	// am initializat capacitatea cu 5, iar lungimea cu 0 (nu sunt elemente)
	//relatia este r
}

//adauga o pereche (cheie, valoare) in dictionar
//daca exista deja cheia in dictionar, inlocuieste valoarea asociata cheii si returneaza vechea valoare
//daca nu exista cheia, adauga perechea si returneaza null
TValoare DO::adauga(TCheie c, TValoare v) {
	/* de adaugat */
	/* CF: 0(1), lg < cap, cheia exista in dictionar si e pe prima pozitie
	*  CD: O(3*lg), lg > cap, cheia nu exista in dictionar si o adaugam pe ultima pozitie
	*  CM: 0(lg), lg < cap, cheia nu exista in dictionar si o adaugam pe o pozitie aleatoare
	*  CG: O(lg)
	*/
	//daca lungimea depaseste capacitatea, atunci dublam capacitatea
	if (lg >= cap) {
		TElem* new_elems = new TElem[2 * cap];
		cap = 2 * cap;
		for (int i = 0; i < lg; i++) {
			new_elems[i].first = this->elems[i].first;
			new_elems[i].second = this->elems[i].second;
		}
		delete[] elems;
		elems = new_elems;
	}
	//daca exista cheia in dictionar, atunci inlocuim val initiala cu v si returnam val initiala
	for (int i = 0; i < lg; i++) {
		if (this->elems[i].first == c) {
			TValoare old_val = this->elems[i].second;
			this->elems[i].second = v;
			return old_val;
		}
	}
	//adaugam perechea in dictionar pe pozitia corecta
	for (int i = 0; i < lg; i++) {
		if (r(this->elems[i].first, c) == true) {
			lg++;
			for (int j = lg - 1; j > i; j--) {
				this->elems[j].first = this->elems[j - 1].first;
				this->elems[j].second = this->elems[j - 1].second;
			}
			this->elems[i].first = c;
			this->elems[i].second = v;
			return NULL_TVALOARE;
		}
	}
	//adaugam pe ultima pozitie perechea daca nu s-a adaugat
	lg++;
	this->elems[lg - 1].first = c;
	this->elems[lg - 1].second = v;
	return NULL_TVALOARE;
}

//cauta o cheie si returneaza valoarea asociata (daca dictionarul contine cheia) sau null
TValoare DO::cauta(TCheie c) const {
	/* de adaugat */
	//CF: O(1)
	//CD: O(lg)
	//CM: O(lg)
	int i;
	for (i = 0; i < lg; i++) {
		if (this->elems[i].first == c) {
			return this->elems[i].second;
		}
	}
	return NULL_TVALOARE;
}

//sterge o cheie si returneaza valoarea asociata (daca exista) sau null
TValoare DO::sterge(TCheie c) {
	/* de adaugat */
	/* CF: 0(lg)
	*  CD: 0(lg)
	*  CM: 0(lg)
	*  CG: 0(lg)
	*/
	for (int i = 0; i < lg; i++) {
		if (this->elems[i].first == c) {
			TValoare val = this->elems[i].second;
			for (int j = i; j < lg - 1; j++) {
				this->elems[j].first = this->elems[j+1].first;
				this->elems[j].second = this->elems[j + 1].second;
			}
			lg--;
			return val;
		}
	}
	return NULL_TVALOARE;
}

//returneaza numarul de perechi (cheie, valoare) din dictionar
int DO::dim() const {
	/* de adaugat */
	return lg;
}

//verifica daca dictionarul e vid
bool DO::vid() const {
	/* de adaugat */
	if (lg > 0) {
		return false;
	}
	else return true;
}

Iterator DO::iterator() const {
	return  Iterator(*this);
}

DO::~DO() {
	/* de adaugat */
	delete[] elems;
}
