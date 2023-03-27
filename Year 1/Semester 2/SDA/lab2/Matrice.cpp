#include "Matrice.h"
#include <exception>
#include <iostream>

using namespace std;

Matrice::Matrice(int m, int n) {
	/* de adaugat */
	if (m <= 0 || n <= 0) {
		throw exception("date invalide\n");
	}
	else {
		this->linii = m;
		this->cols = n;
		LSI lsi;
	}
} 

int Matrice::nrLinii() const {
	/* de adaugat */
	return this->linii;
}

int Matrice::nrColoane() const {
	/* de adaugat */
	return this->cols;
}

//returnare element de pe o linie si o coloana
//se arunca exceptie daca (i,j) nu e pozitie valida in Matrice
//indicii se considera incepand de la 0
TElem Matrice::element(int i, int j) {
	/* de adaugat */
	/*
	* CF: 0(1), elementul cautat este primul 
	* CD: 0(i*j), elementul este ultimul
	* CM: 0(i*j)
	* CG: O(i*j)
	*/
	if (i < 0 || j < 0 || i > this->linii || j > this->cols) {
		throw exception("date invalide\n");
	}
	cout << "aproape am intrat"<<endl;
	if (this->lsi.cautare(i, j) == true) {
		cout << "am intrat" << endl;
		TElem elem = this->lsi.getElem(i, j);
		return elem;
	}
	return NULL_TELEMENT;
} 

// modificare element de pe o linie si o coloana si returnarea vechii valori
// se arunca exceptie daca (i,j) nu e o pozitie valida in Matrice
TElem Matrice::modifica(int i, int j, TElem e) {
	/* de adaugat */
	if (i < 0 || j < 0 || i > this->linii || j > this->cols) {
		throw exception("date invalide\n");
	} else if (e != 0) {
		TElem elem = this->lsi.modify(i, j, e);
		return elem;
	} else return NULL_TELEMENT;
}