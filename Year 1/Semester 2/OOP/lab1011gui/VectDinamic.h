#pragma once

#define INIT_CAP 10

template<typename TElem>
class Iterator;

template<typename TElem>
class VectDinamic {
private:
	int lg; //lungimea
	int cap; //capacitatea
	TElem* elems;

	void ensureCapacity();

public:

	//constructor
	VectDinamic();

	//constructor de copiere
	VectDinamic(const VectDinamic& ot);

	//destructor
	~VectDinamic();

	/*
	Operator assignment
	elibereaza ce era in obiectul curent (this)
	aloca spatiu pentru elemente
	copieaza elementele din ot in this
	*/
	VectDinamic& operator=(const VectDinamic& ot);

	/*
	Move constructor
	Apelat daca construim un nou vector dintr-un r-value (ex temporary, expresie de la return)
	Obiectul ot nu se mai foloseste astfel se poate refolosi interiorul lui
	*/
	VectDinamic(VectDinamic&& ot) noexcept;

	/*
	Move assignment
	Similar cu move constructor
	Folosit la assignment
	*/
	VectDinamic& operator=(VectDinamic&& ot);

	void add(const TElem& elem);

	void delete_elem(int pos);

	int getSize() const noexcept;

	TElem& getElem(size_t pos) const;

	void set(int pos, const TElem& elem);

	friend class Iterator<TElem>;
	//functii care creeaza iteratori
	Iterator<TElem> begin();
	Iterator<TElem> end();
};

template <typename TElem> VectDinamic<TElem>::VectDinamic() : lg{ 0 }, cap{ INIT_CAP }, elems{ new TElem[INIT_CAP] }{}

template <typename TElem> VectDinamic<TElem>::~VectDinamic() {
	delete[] elems;
}

template <typename TElem> VectDinamic<TElem>::VectDinamic(const VectDinamic& ot) {
	elems = new TElem[ot.cap];
	for (int i = 0; i < ot.lg; i++) {
		elems[i] = ot.elems[i];
	}
	lg = ot.lg;
	cap = ot.cap;
}

template <typename TElem> VectDinamic<TElem>& VectDinamic<TElem>::operator=(const VectDinamic& ot) {
	if (this == &ot) {
		return *this;
	}
	delete[] elems;
	elems = new TElem[ot.cap];
	for (int i = 0; i < ot.lg; i++) {
		elems[i] = ot.elems[i];
	}
	lg = ot.lg;
	cap = ot.cap;
	return *this;
}

template<typename TElem> VectDinamic<TElem>::VectDinamic(VectDinamic&& ot) noexcept {
	//copiaza datele de la un pointer la altul
	elems = ot.elems;
	lg = ot.lg;
	cap = ot.cap;

	//elibereaza memoria celuilalt pointer
	ot.elems = nullptr;
	ot.lg = 0;
	ot.cap = 0;
}

template<typename TElem> VectDinamic<TElem>& VectDinamic<TElem>::operator=(VectDinamic&& ot) {
	if (this == &ot) {
		return *this;
	}
	delete[] elems;
	elems = ot.elems;
	lg = ot.lg;
	cap = ot.cap;

	ot.elems = nullptr;
	ot.lg = 0;
	ot.cap = 0;

	return *this;
}

template<typename TElem> void VectDinamic<TElem>::ensureCapacity() {
	if (lg >= cap) {
		cap *= 2;
		TElem* new_elems = new TElem[cap];
		for (int i = 0; i < lg; i++) {
			new_elems[i] = elems[i];
		}
		delete[] elems;
		elems = new_elems;
	}
}

template<typename TElem> void VectDinamic<TElem>::add(const TElem& el) {
	ensureCapacity();
	elems[lg++] = el;
}

template<typename TElem> void VectDinamic<TElem>::delete_elem(int pos) {
	ensureCapacity();
	elems[pos] = elems[pos + 1];
	lg--;
}

template<typename TElem> int VectDinamic<TElem>::getSize() const noexcept {
	return lg;
}

template<typename TElem> TElem& VectDinamic<TElem>::getElem(size_t pos) const {
	return elems[pos];
}

template<typename TElem> void VectDinamic<TElem>::set(int pos, const TElem& elem) {
	elems[pos] = elem;
}

template<typename TElem> Iterator<TElem> VectDinamic<TElem>::begin() {
	return Iterator<TElem>(*this);
}

template<typename TElem> Iterator<TElem> VectDinamic<TElem>::end() {
	return Iterator<TElem>(*this, lg);
}

template<typename TElem>
class Iterator {
private:
	int index{};
	const VectDinamic<TElem>& vect;

public:
	Iterator(const VectDinamic<TElem>& vect) noexcept;
	Iterator(const VectDinamic<TElem>& vect, int index) noexcept;
	bool valid() const;
	void next();
	TElem& element();
	TElem& operator*();
	Iterator& operator++();
	bool operator==(const Iterator& ot) noexcept;
	bool operator!=(const Iterator& ot) noexcept;

};

template<typename TElem> Iterator<TElem>::Iterator(const VectDinamic<TElem>& vect) noexcept : vect{ vect } {}

template<typename TElem> Iterator<TElem>::Iterator(const VectDinamic<TElem>& vect, int index) noexcept : vect{ vect }, index{ index }{}

template<typename TElem> bool Iterator<TElem>::valid() const {
	return index < vect.lg;
}

template<typename TElem> void Iterator<TElem>::next() {
	index++;
}

template<typename TElem> TElem& Iterator<TElem>::element() {
	return vect.elems[index];
}

template <typename TElem> TElem& Iterator<TElem>::operator*() {
	return element();
}

template<typename TElem> Iterator<TElem>& Iterator<TElem>::operator++() {
	next();
	return (*this);
}

template<typename TElem> bool Iterator<TElem>::operator==(const Iterator& ot) noexcept {
	return index == ot.index;
}

template<typename TElem> bool Iterator<TElem>::operator!=(const Iterator& ot) noexcept {
	return !(*this == ot);
}