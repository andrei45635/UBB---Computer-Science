#include "IteratorLI.h"
#include "LI.h"
#include <exception>

IteratorLI::IteratorLI(const LI& li) : lista(li) {
	/* de adaugat */
	this->index = li.head;
}

void IteratorLI::prim() {
	/* de adaugat */
	this->index = this->lista.head;
}

void IteratorLI::urmator() {
	/* de adaugat */
	if (this->index == -1) {
		throw std::exception("iterator invalid!\n");
	}
	//this->index++;
	this->index = this->lista.urm[this->index];
}

bool IteratorLI::valid() const {
	/* de adaugat */
	return this->index != -1;
}

TElem IteratorLI::element() const {
	/* de adaugat */
	if (this->index > this->lista.size || this->index < 0) {
		throw std::exception("iterator invalid!\n");
	}
	return this->lista.elems[this->index];
}
