#pragma once

class Node {
public:
	int linie;
	int coloana;
	int val;
	Node* next;

	//constructor pentru nod
	Node(int linie, int coloana, int val);

	//destructor pentru nod
	~Node();
};