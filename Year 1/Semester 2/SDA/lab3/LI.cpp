#include <exception>
#include <iostream>
#include "LI.h"
#include "IteratorLI.h"

LI::LI() {
	/* de adaugat */
	this->cap = INIT_CAP;
	this->size = 0;

	this->elems = new TElem[cap];
	this->urm = new int[cap];

	this->head = -1;
	for (int i = 0; i < cap - 1; i++) {
		this->urm[i] = i + 1;
	}
	this->urm[cap - 1] = -1;
	this->primLiber = 0;
}

int LI::aloca() {
	auto i = this->primLiber;
	this->primLiber = this->urm[this->primLiber];
	return i;
}

void LI::dealoca(int i) {
	this->urm[i] = this->primLiber;
	this->primLiber = i;
}

int LI::createNode(TElem e) {
	if (this->primLiber == this->cap - 1) {
		check_if_resize();
	}
	int i = aloca();
	if (i != -1) {
		this->elems[i] = e;
		this->urm[i] = -1;
	}
	return i;
}

int LI::dim() const {
	/* de adaugat*/
	return this->size;
}

bool LI::vida() const {
	/* de adaugat */
	return this->head == -1;
}

void LI::check_if_resize() {

	int newcap = 2 * this->cap + 1;
	TElem* new_elems = new TElem[newcap];
	int* new_urm = new int[newcap];
	this->primLiber = this->cap;
	this->cap = newcap;
	for (int i = 0; i < cap - 1; i++) {
		new_urm[i] = i + 1;
	}
	new_urm[this->cap - 1] = -1;
	for (int i = 0; i < this->dim(); i++) {
		new_elems[i] = this->elems[i];
		new_urm[i] = this->urm[i];
	}
	delete[] this->elems;
	this->elems = new_elems;
	delete[] this->urm;
	this->urm = new_urm;
}

// returnare element
// arunca exceptie daca i nu e valid
TElem LI::element(int i) const {
	/* de adaugat
	* CF: 0(1)
	* CD: 0(1)
	* CG: 0(1)
	* CM: 0(1)
	*/
	if (i < 0 || i > this->size) {
		throw std::exception("invalid\n");
	}
	else return this->elems[i];
}

// modifica element de pe pozitia i si returneaza vechea valoare
// arunca exceptie daca i nu e valid
TElem LI::modifica(int i, TElem e) {
	/* de adaugat
	* CF: 0(1)
	* CD: 0(this->size)
	* CG: O(this->size)
	* CM: O(this->size)
	*/
	if (i < 0 || i > this->size) {
		throw std::exception("invalid\n");
	}
	TElem vechi = this->elems[i];
	this->elems[i] = e;
	return vechi;
}

// adaugare element la sfarsit
void LI::adaugaSfarsit(TElem e) {
	/* de adaugat
	* CF: 0(1)
	* CD: 0(1)
	* CG: 0(1)
	* CM: 0(1)
	*/
	//check_if_resize();
	if (this->head == -1) this->head = 0;
	if (this->size >= this->cap) check_if_resize();
	auto i = this->primLiber;
	this->primLiber = this->urm[this->primLiber];
	this->elems[i] = e;
	this->urm[i] = -1;
	this->size++;
}

// adaugare element pe o pozitie i 
// arunca exceptie daca i nu e valid
void LI::adauga(int i, TElem e) {
	/* de adaugat
	* CF: 0(1)
	* CD: 0(this->size)
	* CG: O(this->size)
	* CM: O(this->size)
	*/
	if (i < 0 || i >= this->dim()) {
		throw std::exception("invalid\n");
	}
	int free_pos = createNode(e);
	this->urm[free_pos] = this->urm[i];
	this->elems[free_pos] = i;
	this->elems[i] = e;

	this->urm[free_pos] = -1;
	this->urm[i] = free_pos;
}

// sterge element de pe o pozitie i si returneaza elementul sters
// arunca exceptie daca i nu e valid
TElem LI::sterge(int i) {
	/* de adaugat
	* CF: 0(1)
	* CD: 0(this->size)
	* CG: O(this->size)
	* CM: O(this->size)
	*/
	if (i < 0 || i > this->size) {
		throw std::exception("invalid\n");
	}
	TElem cautat = this->elems[i];
	for (int k = 0; k <= this->size; k++) {
		if (i == this->head) {
			this->head = this->urm[k];
			this->size--;
		} 
		if (i == this->size && k > 0) {
			this->urm[this->elems[k - 1]] = -1;
			this->primLiber = 0;
			this->size--;
		}
		else if (i > 0 && i < this->size && k > 0 && k < this->size) {
			this->urm[this->elems[k - 1]] = this->urm[this->elems[i]];
			this->size--;
		}
	}
	return cautat;
}

// cauta element si returneaza prima pozitie pe care apare (sau -1)
int LI::cauta(TElem e) const {
	/* de adaugat
	* CF: 0(1)
	* CD: 0(this->size)
	* CG: O(this->size)
	* CM: O(this->size)
	*/
	if (!vida()) {
		for (int i = 0; i <= this->size; i++) {
			if (this->elems[i] == e)
				return i;
		}
	}
	return -1;
}

//complexitate O(sfarsit-inceput+1)
//caz favorabil -> una din pozitii nu e valida => 0(1)
//caz defavorabil -> pozitiile sunt valide => 0(sfarsit-inceput+1)
//caz mediu -> nu se arunca exceptie => 0(sfarsit-inceput+1)

//invesreazaIntre(inceput, sfarsit, LI lista)
//pre: inceput->numar intreg, pozitia de inceput
//	   sfarsit->numar intreg, pozitia de sfarsit
//post: lista'
//
//	daca inceput < 0 sau sfarsit < 0 sau inceput > dimensiune sau sfarsit > dimensiune
//		@arunca exceptie
//	cat timp inceput <= sfarsit executa
//		aux <- elems[inceput]
//		elems[inceput] <- elems[sfarsit]
//		elems[sfarist] <- aux
//		inceput <- inceput + 1
//		sfarsit <- sfarsit -1
//Sf algoritm

void LI::inverseazaIntre(int inceput, int sfarsit)
{
	if (inceput < 0 || sfarsit < 0 || inceput > this->size || sfarsit > this->size)
		throw std::exception();

	while (inceput <= sfarsit)
	{
		TElem aux;
		aux = this->elems[inceput];
		this->elems[inceput] = this->elems[sfarsit];
		this->elems[sfarsit] = aux;
		inceput++;
		sfarsit--;
	}
}

IteratorLI LI::iterator() const {
	return  IteratorLI(*this);
}

// destructor
LI::~LI() {
	/* de adaugat */
	delete[] this->elems;
	delete[] this->urm;
}
