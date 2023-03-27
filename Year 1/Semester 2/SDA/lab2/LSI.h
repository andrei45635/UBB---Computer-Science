#pragma once

#include "Node.h"

class LSI {
private:
	Node* head;
	int size;

public:

	//constructor lista
	LSI();

	//destructor lista
	~LSI();

	//cautare in matrice
	bool cautare(int i, int j);

	//modificare element
	int modify(int i, int j, int elem_nou);

	//getter pentru element
	int getElem(int linie, int coloana);

	//verificam daca lista e valida
	bool valid();
};