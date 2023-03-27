#include "Dictionar.h"
#include <iostream>
#include "IteratorDictionar.h"

Dictionar::Dictionar() {
	/* de adaugat */
	/*
	*  CF: 0(this->size)
	*  CD: 0(this->size)
	*  CG: 0(this->size)
	*  CM: 0(this->size)
	*/
	this->size = INIT_SIZE;
	for (int i = 0; i < this->size-1; i++) {
		//this->elems[i]->first = NULL_TVALOARE;
		//this->elems[i]->second = NULL_TVALOARE;
		this->elems[i] = 0;
		this->urm[i] = -1;
	}
	this->primLiber = 0;
}

int Dictionar::hashF(TCheie c) {
	return abs(c) % this->size;
}

Dictionar::~Dictionar() {
	/* de adaugat */
}

void Dictionar::updatePrimLiber() {
	this->primLiber++;
	while (this->primLiber <= this->size - 1 && this->elems[this->primLiber]->first != -1) {
		this->primLiber++;
	}
}

TValoare Dictionar::adauga(TCheie c, TValoare v) {
	/* de adaugat */
	int i = hashF(c); //hash function
	int prec = 0;
	if (this->elems[i]->first != -1) {
		this->elems[i]->first = c;
		this->elems[i]->second = v;
		if (this->primLiber == i) updatePrimLiber();
	}
	else {
		//adaugam la finalul listei inlantuite memorata la loc i
		//daca gasim cheia, stop
		while (i != -1 && this->elems[i]->first != c) {
			prec = i; //precendent
			i = this->urm[i];
		}
		if (i != -1) throw std::exception("cheie existenta\n");
		else if (this->primLiber <= this->size - 1) {
			this->elems[this->primLiber]->first = c;
			this->elems[this->primLiber]->second = v;
			this->urm[prec] = this->primLiber;
			updatePrimLiber();
		}
		else throw std::exception("depasire tabela\n");
	}
	return NULL_TVALOARE;
}

//cauta o cheie si returneaza valoarea asociata (daca dictionarul contine cheia) sau null
TValoare Dictionar::cauta(TCheie c) const {
	/* de adaugat */
	/*
	*  CF: 0(1)
	*  CD: O(this->size)
	*  CG: O(this->size)
	*  CM: O(this->size)
	*/
	auto i = abs(c) % this->size;
	while (i != -1 && this->elems[i]->first != c) {
		i = this->urm[i];
	}
	if (i == -1) return NULL_TVALOARE;
	else return this->elems[i]->second;
}


TValoare Dictionar::sterge(TCheie c) {
	/* de adaugat */
	/*
	*  CF: 0(1)
	*  CD: 0(this->size)
	*  CG: O(this->size)
	*  CM: O(this->size)
	*/
	auto hash_val = hashF(c);
	auto prec = -1; // pp ca !E precedent pt vid
	auto i = 0;
	while (i < this->size && prec == -1) {
		if (this->urm[i] == hash_val) prec = i;
		else i++;
	}
	i = hash_val; //i este poz de pe care stergem
	auto j = prec; //j este poz prec a lui i
	/*while (i != -1 && this->elems[i]->first != c) {
		j = i;
		i = this->urm[i];
	}*/
	if (i == -1) return NULL_TVALOARE;
	else {
		auto val = this->elems[i]->second;
		bool gata = false;
		do {
			auto p = this->urm[i];
			auto pp = i;
			while (p != -1 && (abs(this->elems[p]->first) % this->size != i)){
				pp = p;
				p = this->urm[p];
			}
			if (p == -1) gata = true;
			else {
				this->elems[i] = this->elems[p];
				i = p;
				j = pp;
			}
		} while (gata);
		if (j != -1) {
			while (i != -1 && this->elems[i]->first != c) {
				j = i;
				i = this->urm[i];
			}
			this->urm[j] = this->urm[i];
		}
		this->elems[i]->first = NULL_TVALOARE;
		this->elems[i]->second = NULL_TVALOARE;
		this->urm[i] = -1;
		if (this->primLiber > i) this->primLiber = i;

	}
}

int Dictionar::dim() const {
	/* de adaugat */
	int dim = 0;
	IteratorDictionar itd = this->iterator();
	itd.prim();
	while (itd.valid()) {
		dim++;
		itd.urmator();
	}
	return dim;
}

bool Dictionar::vid() const {
	/* de adaugat */
	if (this->size < 0) return false;
	else return true;
}


IteratorDictionar Dictionar::iterator() const {
	return  IteratorDictionar(*this);
}