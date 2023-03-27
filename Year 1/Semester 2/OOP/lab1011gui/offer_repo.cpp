#include "offer_repo.h"
#include <algorithm>
#include <assert.h>
#include <iostream>
#include <fstream>

using std::cout;

string RepoException::getMessage() {
	return mesg;
}

void RepoOffer::addRepoOffer(const Offer& ofr) {
	for (const Offer& oferta : offers) {
		if (oferta.getDenumire() == ofr.getDenumire() && oferta.getDestinatie() == ofr.getDestinatie() && oferta.getType() == ofr.getType())
			throw RepoException("Oferta exista!\n");
	}
	//offers.add(ofr);
	offers.push_back(ofr);
}

const vector<Offer>& RepoOffer::getAll() {
	return offers;
}

void RepoOffer::deleteRepoOffer(int pos) {
	if (pos > offers.size()) {
		throw RepoException("Oferta nu exista!\n");
	}
	for (int i = 0; i < offers.size(); i++) {
		if (pos == i) {
			offers.erase(offers.begin() + pos);
			//offers.delete_elem(pos);
		}
	}
}

void RepoOffer::deleteOffersForUndo(const Offer& ofr) {
	auto found = std::find_if(offers.begin(), offers.end(), [ofr](const Offer& o) {
		return o.getDenumire() == ofr.getDenumire() && o.getDestinatie() == ofr.getDestinatie() && o.getPrice() == ofr.getPrice() && o.getType() == ofr.getType();
		});
	if (found == offers.end()) throw RepoException{ "oferta nu exista!\n" };
	auto rez = offers.erase(found);
}

void RepoOffer::modifyRepoOffer(int pos, const Offer& new_ofr) {
	if (pos > offers.size()) {
		throw RepoException("Oferta nu exista!\n");
	}
	for (int i = 0; i < offers.size(); i++) {
		if (pos == i) {
			offers.erase(offers.begin() + pos);
			offers.insert(offers.begin() + pos, new_ofr);
			//offers.set(pos, new_ofr);
		}
	}
}

void RepoOffer::modifyOfferForUndo(const Offer& old_ofr, const Offer& new_ofr) {
	auto found = std::find_if(offers.begin(), offers.end(), [old_ofr](const Offer& o) {
		return o.getDenumire() == old_ofr.getDenumire() && o.getDestinatie() == old_ofr.getDestinatie() && o.getPrice() == old_ofr.getPrice() && o.getType() == old_ofr.getType();
		});
	if (found == offers.end()) throw RepoException{ "oferta nu exista!\n" };
	auto rez = offers.erase(found);
	offers.push_back(new_ofr);
}

Offer RepoOffer::findOfferRepo(int pos) {
	return offers[pos];
}

void test_create_repo() {
	RepoOffer repots;
	Offer ofr1{ "Vacanta", "Kiev", "Familie", 19 };
	Offer ofr2{ "Croaziera", "Marea Azov", "Familie", 21 };
	repots.addRepoOffer(ofr1);
	repots.addRepoOffer(ofr2);
	const auto& offers = repots.getAll();
	assert(offers.size() == 2);
	try {
		repots.addRepoOffer(ofr1);
		assert(false);
	}
	catch (RepoException&) {
		assert(true);
	}
}

void test_delete_repo() {
	RepoOffer test_repo;
	Offer ofr1{ "Vacanta", "Kiev", "Familie", 19 };
	Offer ofr2{ "Croaziera", "Marea Azov", "Familie", 21 };
	Offer ofr3{ "Business", "Odesa", "Tren", 420 };
	test_repo.addRepoOffer(ofr1);
	test_repo.addRepoOffer(ofr2);
	const auto& offers = test_repo.getAll();
	assert(offers.size() == 2);
	test_repo.deleteRepoOffer(1);
	assert(offers.size() == 1);
	try {
		test_repo.deleteRepoOffer(3);
		assert(false);
	}
	catch (RepoException&) {
		assert(true);
	}
	test_repo.addRepoOffer(ofr2);
	assert(offers.size() == 2);
	const auto& offers2 = test_repo.getAll();
	test_repo.deleteOffersForUndo(ofr1);
	assert(offers2.size() == 1);
	try {
		test_repo.deleteOffersForUndo(ofr3);
		assert(false);
	}
	catch (RepoException&) {
		assert(true);
	}
}

void test_modify_repo() {
	RepoOffer test_repo;
	Offer ofr1{ "Vacanta", "Kiev", "Familie", 19 };
	Offer ofr2{ "Croaziera", "Marea Azov", "Familie", 21 };
	Offer ofr3{ "Business", "Odesa", "Tren", 420 };
	Offer ofr4{ "Familie", "Mariupol", "Voiaj", 69 };
	test_repo.addRepoOffer(ofr1);
	test_repo.addRepoOffer(ofr2);
	const auto& offers = test_repo.getAll();
	assert(offers.size() == 2);
	test_repo.modifyRepoOffer(1, ofr3);
	assert(offers.size() == 2);
	assert(ofr3.getDenumire() == offers[1].getDenumire());
	assert(ofr3.getDestinatie() == offers[1].getDestinatie());
	assert(ofr3.getType() == offers[1].getType());
	assert(ofr3.getPrice() == offers[1].getPrice());
	try {
		test_repo.modifyRepoOffer(3, ofr3);
		assert(false);
	}
	catch (RepoException&) {
		assert(true);
	}
	test_repo.modifyOfferForUndo(ofr1, ofr3);
	assert(offers.size() == 2);
	assert(ofr3.getDenumire() == offers[0].getDenumire());
	assert(ofr3.getDestinatie() == offers[0].getDestinatie());
	assert(ofr3.getType() == offers[0].getType());
	assert(ofr3.getPrice() == offers[0].getPrice());
	try {
		test_repo.modifyOfferForUndo(ofr4, ofr3);
		assert(false);
	}
	catch (RepoException&) {
		assert(true);
	}
}

void test_find_repo() {
	RepoOffer test_repo;
	Offer ofr1{ "Vacanta", "Kiev", "Familie", 19 };
	Offer ofr2{ "Croaziera", "Marea Azov", "Familie", 21 };
	Offer ofr3{ "Business", "Odesa", "Tren", 420 };
	test_repo.addRepoOffer(ofr1);
	test_repo.addRepoOffer(ofr2);
	const auto& offers = test_repo.getAll();
	assert(offers.size() == 2);
	const auto& found = test_repo.findOfferRepo(1);
	assert(found.getDenumire() == ofr2.getDenumire());
	assert(found.getDestinatie() == ofr2.getDestinatie());
	assert(found.getType() == ofr2.getType());
	assert(found.getPrice() == ofr2.getPrice());
}