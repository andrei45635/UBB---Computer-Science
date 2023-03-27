#pragma once
#include <vector>
#include "oferta.h"
#include "Observer.h"

using std::vector;

class WishExcept {
private:

	string mesg;

public:

	/*
	* Constructor pentru clasa WishExcept
	* Primeste atributul string msg = mesajul erorii
	*/
	WishExcept(string msg) : mesg{ msg } {

	}

	/*
	* getter pentru mesaj
	*/
	string getMessage();
};

class Wishlist: public Observable{
private:
	vector<Offer> wishlist;

public:
	void delete_all_wishlist();

	void add_wishlist(const Offer& ofr);

	bool find_in_wishlist(const Offer& ofr);

	void generate_offers(const vector<Offer>& list);

	vector<Offer> get_all_wishlist();
};

void testAddToWish();
void testDeleteWish();
void testGenerateWish();