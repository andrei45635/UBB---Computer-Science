#include "TestScurt.h"
#include <assert.h>
#include "Dictionar.h"
#include "IteratorDictionar.h"
#include <iostream>

using std::cout;

void testall() { //apelam fiecare functie sa vedem daca exista
	Dictionar d;
	cout << "aici-1" << '\n';
	assert(d.vid() == true);
	cout << "aici0" << '\n';
	cout << d.dim() << " \n";
	assert(d.dim() == 0); //adaug niste elemente
	cout << "aici1" << '\n';
	assert(d.adauga(5, 5) == NULL_TVALOARE);
	cout << "aici2" << '\n';
	assert(d.adauga(1, 111) == NULL_TVALOARE);
	cout << "aici3" << '\n';
	assert(d.adauga(10, 110) == NULL_TVALOARE);
	cout << "aici4" << '\n';
	assert(d.adauga(7, 7) == NULL_TVALOARE);
	cout << "aici5" << '\n';
	assert(d.adauga(1, 1) == 111);
	cout << "aici5" << '\n';
	assert(d.adauga(10, 10) == 110);
	cout << "aici6" << '\n';
	assert(d.adauga(-3, -3) == NULL_TVALOARE);
	cout << "aici7" << '\n';
	assert(d.dim() == 5);
	cout << "aici8" << '\n';
	assert(d.cauta(10) == 10);
	cout << "aici9" << '\n';
	assert(d.cauta(16) == -1);
	cout << "aici10" << '\n';
	assert(d.sterge(1) == 1);
	cout << "aici11" << '\n';
	assert(d.sterge(6) == -1);
	cout << "aici12" << '\n';
	assert(d.dim() == 4);
	cout << "aici13" << '\n';


	TElem e;
	IteratorDictionar id = d.iterator();
	id.prim();
	int s1 = 0, s2 = 0;
	while (id.valid()) {
		e = id.element();
		s1 += e.first;
		s2 += e.second;
		id.urmator();
	}
	assert(s1 == 19);
	assert(s2 == 19);

}














void testAll() {
	//testall();
}