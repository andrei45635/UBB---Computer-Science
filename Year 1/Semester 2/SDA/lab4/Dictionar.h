#pragma once


#define NULL_TVALOARE -1
#define INIT_SIZE 10
typedef int TCheie;
typedef int TValoare;

class IteratorDictionar;

#include <utility>
#include <exception>
typedef std::pair<TCheie, TValoare> TElem;

class Node {
public:
	TCheie key;
	TValoare val;
	Node* next;
};

class Dictionar {
	friend class IteratorDictionar;
	friend class Node;

private:
	/* aici e reprezentarea */
	int size;
	TElem* elems[INIT_SIZE];
	//Node* elem;
	int urm[INIT_SIZE];
	int primLiber;
	int hashF(TCheie c);
	void updatePrimLiber();

public:

	// constructorul implicit al dictionarului
	Dictionar();

	// adauga o pereche (cheie, valoare) in dictionar	
	//daca exista deja cheia in dictionar, inlocuieste valoarea asociata cheii si returneaza vechea valoare
	// daca nu exista cheia, adauga perechea si returneaza null: NULL_TVALOARE
	TValoare adauga(TCheie c, TValoare v);

	//cauta o cheie si returneaza valoarea asociata (daca dictionarul contine cheia) sau null: NULL_TVALOARE
	TValoare cauta(TCheie c) const;

	//sterge o cheie si returneaza valoarea asociata (daca exista) sau null: NULL_TVALOARE
	TValoare sterge(TCheie c);

	//returneaza numarul de perechi (cheie, valoare) din dictionar 
	int dim() const;

	//verifica daca dictionarul e vid 
	bool vid() const;

	// se returneaza iterator pe dictionar
	IteratorDictionar iterator() const;


	// destructorul dictionarului	
	~Dictionar();

};



