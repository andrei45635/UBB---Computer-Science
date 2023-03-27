#include "IteratorDictionar.h"
#include "Dictionar.h"

using namespace std;

IteratorDictionar::IteratorDictionar(const Dictionar& d) : dict(d) {
	/* de adaugat */
	this->index = 0;
	//this->current->key = -1;
	//this->current->val = -1;
	//this->current->next = NULL;
}

void IteratorDictionar::prim() {
	/* de adaugat */
	this->index = dict.primLiber;
}


void IteratorDictionar::urmator() {
	/* de adaugat */
	this->index++;
	//while ((this->index < dict.size) && (dict.elems[this->index]->first != -1 && dict.elems[this->index]->second != -1)) this->index++;
}


TElem IteratorDictionar::element() const {
	/* de adaugat */
	if (!valid()) return pair <TCheie, TValoare>(-1, -1);
	else return pair <TCheie, TValoare>(dict.elems[this->index]->first, dict.elems[this->index]->second);
}

bool IteratorDictionar::valid() const {
	/* de adaugat */
	if (this->index != -1) return true;
	return false;
}

