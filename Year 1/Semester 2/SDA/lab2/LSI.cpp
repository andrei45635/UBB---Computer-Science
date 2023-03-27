#include "LSI.h"
#include <iostream>

LSI::LSI() {
	head = NULL;
	size = 0;
}

bool LSI::valid() {
	if (size <= 0) {
		return false;
	}
	else return true;
}

bool LSI::cautare(int i, int j) {
	if (!valid()) {
		std::cout << "cine stie" << std::endl;
		Node* temp = head;
		while (temp) {
			std::cout << "cine stie 2" << std::endl;
			if (temp->linie == i && temp->coloana == j) {
				std::cout << "cine stie3" << std::endl;
				return true;
			}
			temp = temp->next;
		}
	}
	else return false;
}

int LSI::modify(int i, int j, int new_val) {
	int check = 0;
	if (!valid()) {
		Node* temp = head;
		while (temp) {
			if (temp->linie == i && temp->coloana == j) {
				check = 1;
				int old_val = temp->val;
				temp->val = new_val;
				return old_val;
			}
			temp = temp->next;
		}
		if (check == 0) {
			Node* temp = head->next;
			temp->linie = i;
			temp->coloana = j;
			temp->val = new_val;
		}
	}
	else {
		head->linie = i;
		head->coloana = j;
		head->val = new_val;
		this->size++;
	}
}

int LSI::getElem(int linie, int coloana) {
	if (!valid()) {
		Node* temp = head;
		while (temp) {
			if (temp->linie == linie && temp->coloana == coloana) {
				return temp->val;
			}
			temp = temp->next;
		}
	}
	else return NULL;
}

LSI::~LSI() {

}