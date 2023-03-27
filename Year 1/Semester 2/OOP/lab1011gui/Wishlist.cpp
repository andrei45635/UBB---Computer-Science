#include "Wishlist.h"
#include <cassert>
#include <iostream>

string WishExcept::getMessage() {
	return mesg;
}

/*
* getter pentru toate ofertele din wishlist
* pre: -
* post: avem ofertele din wishlist
*/
vector<Offer> Wishlist::get_all_wishlist() {
	return wishlist;
}

/*
* sterge toate ofertele din wishlist
* pre: -
* post: ofertele au fost sterse
*/
void Wishlist::delete_all_wishlist() {
	vector<Offer> to_del;
	wishlist = to_del;
	notifyTbl();
}

bool Wishlist::find_in_wishlist(const Offer& ofr) {
	const auto& all_ofrs = get_all_wishlist();
	for (const auto& offer : all_ofrs) {
		if (offer.getDenumire() == ofr.getDenumire() && offer.getDestinatie() == ofr.getDestinatie() && offer.getType() == ofr.getType() && offer.getPrice() == ofr.getPrice()) {
			return true;
		}
	}
	return false;
}

/*
* adauga oferta in wishlist
* pre: oferta ofr
* post: oferta a fost adaugata in wishlist
*/
void Wishlist::add_wishlist(const Offer& ofr) {
	if (find_in_wishlist(ofr)) {
		throw WishExcept("oferta este deja in lista!\n");
	}
	else {
		wishlist.push_back(ofr);
		notifyTbl();
	}
}

/*
* genereaza oferte random
* pre: lista cu oferte din service
* post: ofertele au fost generate
*/
void Wishlist::generate_offers(const vector<Offer>& list) {
	delete_all_wishlist();
	for (const auto& ofr : list) {
		add_wishlist(ofr);
		notifyTbl();
	}
}

void testAddToWish() {
	auto wish = Wishlist();
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	Offer ofr{ denum, dest, type, price };
	wish.add_wishlist(ofr);
	assert(wish.get_all_wishlist().size() == 1);
	auto wishlist = wish.get_all_wishlist();
	assert(wishlist[0].getDenumire() == denum);
	assert(wishlist[0].getDestinatie() == dest);
	assert(wishlist[0].getType() == type);
	assert(wishlist[0].getPrice() == price);
	try {
		wish.add_wishlist(ofr);
		assert(false);
	}
	catch (WishExcept&) {
		assert(true);
	}
}

void testDeleteWish() {
	auto wish = Wishlist();
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	Offer ofr{ denum, dest, type, price };
	wish.add_wishlist(ofr);
	assert(wish.get_all_wishlist().size() == 1);
	wish.delete_all_wishlist();
	assert(wish.get_all_wishlist().empty());
}

void testGenerateWish() {
	vector<Offer> offers;
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	Offer ofr{ denum, dest, type, price };
	offers.push_back(ofr);
	string denum2 = "Business";
	string dest2 = "Odesa";
	string type2 = "Tren";
	double price2 = 169;
	Offer ofr2{ denum2, dest2, type2, price2 };
	offers.push_back(ofr2);
	assert(offers.size() == 2);
	auto wish = Wishlist();
	wish.generate_offers(offers);
	assert(wish.get_all_wishlist().size() == 2);
}