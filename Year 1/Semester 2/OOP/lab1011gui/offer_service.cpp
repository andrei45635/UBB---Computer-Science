#include "offer_service.h"
#include <assert.h>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <random>
#include <chrono>

void ServiceOffer::addServiceOffer(string denum, string dest, string type, double price) {
	Offer ofr{ denum, dest, type, price };
	//validare oferta
	valid.validate_offer(ofr);
	repo.addRepoOffer(ofr);
	undoList.push_back(std::make_unique<AddUndo>(repo, ofr));
	notifyLst();
}

const vector<Offer>& ServiceOffer::getAllService() {
	return repo.getAll();
}

void ServiceOffer::deleteServiceOffer(int pos) {
	repo.deleteRepoOffer(pos);
	notifyLst();
}

void ServiceOffer::deleteServiceForUndo(const Offer& ofr) {
	repo.deleteOffersForUndo(ofr);
	undoList.push_back(std::make_unique<DeleteUndo>(repo, ofr));
	notifyLst();
}

void ServiceOffer::modifyServiceOffer(int pos, string new_denum, string new_dest, string new_type, double new_price) {
	Offer new_ofr{ new_denum, new_dest, new_type, new_price };
	//validare oferta
	valid.validate_offer(new_ofr);
	repo.modifyRepoOffer(pos, new_ofr);
	notifyLst();
}

void ServiceOffer::modifyServiceForUndo(const Offer& old_ofr, const Offer& new_ofr) {
	//valid.validate_offer(new_ofr);
	repo.modifyOfferForUndo(old_ofr, new_ofr);
	undoList.push_back(std::make_unique<ModifyUndo>(repo, old_ofr, new_ofr));
	notifyLst();
}

void ServiceOffer::Undo() {
	if (undoList.empty()) throw RepoException{ "Nu exista operatii pentru undo!\n" };
	undoList.back()->doUndo();
	undoList.pop_back();
	notifyLst();
}

Offer ServiceOffer::findOfferService(int pos) {
	return repo.findOfferRepo(pos);
}

vector<Offer> ServiceOffer::filter(std::function<bool(const Offer&)> fct) {
	vector<Offer> res;
	const auto& offers = repo.getAll();
	for (const auto& ofr : offers) {
		if (fct(ofr)) {
			res.push_back(ofr);
		}
	}
	return res;
}

vector<Offer> ServiceOffer::filtrare_pret(int price) {
	return filter([=](const Offer& ofr) { return ofr.getPrice() == price; });
}

vector<Offer> ServiceOffer::filtrare_dest(string dest) {
	return filter([=](const Offer& ofr) { return ofr.getDestinatie() == dest; });
}

vector<Offer> ServiceOffer::generalSort(bool(*cmpMic)(const Offer& ofr1, const Offer& ofr2)) {
	vector<Offer> res{ repo.getAll() };
	for (size_t i = 0; i < res.size(); i++) {
		for (size_t j = i; j < res.size(); j++) {
			if (!cmpMic(res[i], res[j])) {
				Offer aux = res[i];
				res[i] = res[j];
				res[j] = aux;
			}
		}
	}
	return res;
}

bool ServiceOffer::sortByType(const Offer& ofr1, const Offer& ofr2) {
	return ofr1.getType() < ofr2.getType();
}

vector<Offer> ServiceOffer::sortDenumire() {
	//return generalSort(sortByType);
	return generalSort([](const Offer& ofr1, const Offer& ofr2) { return (ofr1.getDenumire() < ofr2.getDenumire()); });
}

vector<Offer> ServiceOffer::sortDest() {
	//return generalSort(sortByType);
	return generalSort([](const Offer& ofr1, const Offer& ofr2) { return (ofr1.getDestinatie() < ofr2.getDestinatie()); });
}

vector<Offer> ServiceOffer::sortFinal() {
	vector<Offer> typed = generalSort([](const Offer& ofr1, const Offer& ofr2) { return (ofr1.getType() < ofr2.getType() || (ofr1.getPrice() < ofr2.getPrice())); });
	vector<Offer> priced = typed;
	priced = generalSort([](const Offer& ofr1, const Offer& ofr2) {return ofr1.getPrice() < ofr2.getPrice(); });
	return priced;
}

vector<Offer> ServiceOffer::sorted() {
	vector<Offer> typed = generalSort([](const Offer& ofr1, const Offer& ofr2) { return (ofr1.getType() < ofr2.getType() || (ofr1.getPrice() < ofr2.getPrice())); });
	auto sortofs = getAllService();
	std::sort(sortofs.begin(), sortofs.end(), [](const Offer& ofr1, const Offer& ofr2) {
		return (ofr1.getType() < ofr2.getType()); });
	std::sort(sortofs.begin(), sortofs.end(), [](const Offer& ofr1, const Offer& ofr2) {
		return (ofr1.getPrice() < ofr2.getPrice()); });
	return sortofs;
}

void ServiceOffer::check_if_Kiev(const vector<Offer>& hohols) {
	bool hohol_counter = false;
	for (int i = 0; i < hohols.size(); i++) {
		if (std::all_of(hohols.begin(), hohols.end(), [](const Offer& ofr) {return ofr.getDestinatie() == "Kiev"; })) {
			hohol_counter = true;
		}
	}
	if (!hohol_counter) std::cout << "Nu toate ofertele au destinatia Kiev!\n";
	else std::cout << "Toate ofertele au destinatia Kiev!\n";
}

void ServiceOffer::generate_random_offers(int number) {
	auto offers = getAllService();
	auto sneed = std::chrono::system_clock::now().time_since_epoch().count();
	std::shuffle(offers.begin(), offers.end(), std::default_random_engine((unsigned int)sneed));
	vector<Offer> to_add;
	for (int i = 0; i < number; i++) {
		to_add.push_back(offers[i]);
	}
	wish.generate_offers(to_add);
}

void ServiceOffer::add_to_wishlist(const string& destinatie) {
	const auto& offers = getAllService();
	for (const auto& ofr : offers) {
		if (ofr.getDestinatie() == destinatie) {
			wish.add_wishlist(ofr);
		}
	}
}

void ServiceOffer::delete_from_wishlist() {
	wish.delete_all_wishlist();
}

vector<Offer> ServiceOffer::get_all_from_wish() {
	return wish.get_all_wishlist();
}

void ServiceOffer::exporta_cos_HTML(const string& fileName){
	exportToHTML(fileName, this->wish.get_all_wishlist());
}

void testCreateService() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	test_serv.addServiceOffer(denum, dest, type, price);
	const auto& offers = test_serv.getAllService();
	assert(offers.size() == 1);
}

void testDeleteOfferService() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	Offer ofr{ denum, dest, type, price };
	test_serv.addServiceOffer(denum, dest, type, price);
	const auto& offers = test_serv.getAllService();
	assert(offers.size() == 1);
	test_serv.deleteServiceOffer(0);
	const auto& offers2 = test_serv.getAllService();
	assert(offers2.size() == 0);
	test_serv.addServiceOffer(denum, dest, type, price);
	const auto& offers3 = test_serv.getAllService();
	assert(offers3.size() == 1);
	test_serv.deleteServiceForUndo(ofr);
	const auto& offers4 = test_serv.getAllService();
	assert(offers4.size() == 0);
}

void testModifyOfferService() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	Offer ofr{ denum, dest, type, price };
	test_serv.addServiceOffer(denum, dest, type, price);
	const auto& offers = test_serv.getAllService();
	assert(offers.size() == 1);
	string new_denum = "Business";
	string new_dest = "Odesa";
	string new_type = "Tren";
	double new_price = 169;
	Offer new_ofr{ new_denum, new_dest, new_type, new_price };
	test_serv.modifyServiceOffer(0, new_denum, new_dest, new_type, new_price);
	const auto& offers2 = test_serv.getAllService();
	assert(offers2.size() == 1);
	assert(offers2[0].getDenumire() == "Business");
	assert(offers2[0].getDestinatie() == "Odesa");
	assert(offers2[0].getType() == "Tren");
	assert(offers2[0].getPrice() == 169);
	test_serv.addServiceOffer(denum, dest, type, price);
	const auto& offers3 = test_serv.getAllService();
	assert(offers3.size() == 2);
	test_serv.modifyServiceForUndo(new_ofr, ofr);
	assert(offers2[0].getDenumire() == denum);
	assert(offers2[0].getDestinatie() == dest);
	assert(offers2[0].getType() == type);
	assert(offers2[0].getPrice() == price);
}

void testFindOfferService() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	test_serv.addServiceOffer(denum, dest, type, price);
	string denum2 = "Business";
	string dest2 = "Odesa";
	string type2 = "Tren";
	double price2 = 169;
	test_serv.addServiceOffer(denum2, dest2, type2, price2);
	const auto& offers = test_serv.getAllService();
	assert(offers.size() == 2);
	const auto& found = test_serv.findOfferService(1);
	assert(found.getDenumire() == "Business");
	assert(found.getDestinatie() == "Odesa");
	assert(found.getType() == "Tren");
	assert(found.getPrice() == 169);
}

void testFilters() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	test_serv.addServiceOffer(denum, dest, type, price);
	string denum2 = "Business";
	string dest2 = "Odesa";
	string type2 = "Tren";
	double price2 = 169;
	test_serv.addServiceOffer(denum2, dest2, type2, price2);
	const auto& offers = test_serv.getAllService();
	assert(offers.size() == 2);
	const auto& fct = test_serv.filtrare_pret(169);
	assert(fct.size() == 1);
	assert(fct[0].getDenumire() == "Business");
	assert(fct[0].getDestinatie() == "Odesa");
	assert(fct[0].getType() == "Tren");
	assert(fct[0].getPrice() == 169);
	const auto& fct2 = test_serv.filtrare_dest("Kiev");
	assert(fct2.size() == 1);
	assert(fct2[0].getDenumire() == "Familie");
	assert(fct2[0].getDestinatie() == "Kiev");
	assert(fct2[0].getType() == "Roadtrip");
	assert(fct2[0].getPrice() == 69);
}

void testSorts() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Woadtrip";
	double price = 69;
	test_serv.addServiceOffer(denum, dest, type, price);
	string denum2 = "Business";
	string dest2 = "Odesa";
	string type2 = "Tren";
	double price2 = 169;
	test_serv.addServiceOffer(denum2, dest2, type2, price2);
	const auto& sorted = test_serv.sortDenumire();
	assert(sorted[0].getDenumire() == "Business");
	assert(sorted[0].getDestinatie() == "Odesa");
	assert(sorted[0].getType() == "Tren");
	assert(sorted[0].getPrice() == 169);
	const auto& sorted2 = test_serv.sortDest();
	assert(sorted2[0].getDenumire() == "Familie");
	assert(sorted2[0].getDestinatie() == "Kiev");
	assert(sorted2[0].getType() == "Woadtrip");
	assert(sorted2[0].getPrice() == 69);
	const auto& sorted3 = test_serv.sortFinal();
	assert(sorted3[0].getDenumire() == "Familie");
	const auto& sorted4 = test_serv.sorted();
	assert(sorted4[0].getDenumire() == "Familie");
}

void testAddCart() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Woadtrip";
	double price = 69;
	Offer ofr1{ denum, dest, type, price };
	test_serv.addServiceOffer(denum, dest, type, price);
	string denum2 = "Business";
	string dest2 = "Odesa";
	string type2 = "Tren";
	double price2 = 169;
	test_serv.addServiceOffer(denum2, dest2, type2, price2);
	assert(test_serv.getAllService().size() == 2);
	test_serv.add_to_wishlist(dest);
	assert(test_serv.get_all_from_wish().size() == 1);
}

void testDeleteFromCart() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Woadtrip";
	double price = 69;
	test_serv.addServiceOffer(denum, dest, type, price);
	string denum2 = "Business";
	string dest2 = "Odesa";
	string type2 = "Tren";
	double price2 = 169;
	test_serv.addServiceOffer(denum2, dest2, type2, price2);
	test_serv.add_to_wishlist(dest);
	test_serv.add_to_wishlist(dest2);
	assert(test_serv.get_all_from_wish().size() == 2);
	test_serv.delete_from_wishlist();
	assert(test_serv.get_all_from_wish().size() == 0);
}

void testGenerateRandom() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Woadtrip";
	double price = 69;
	Offer ofr1{ denum, dest, type, price };
	test_serv.addServiceOffer(denum, dest, type, price);
	string denum2 = "Business";
	string dest2 = "Odesa";
	string type2 = "Tren";
	double price2 = 169;
	test_serv.addServiceOffer(denum2, dest2, type2, price2);
	test_serv.generate_random_offers(2);
	assert(test_serv.get_all_from_wish().size() == 2);
	test_serv.exporta_cos_HTML("test_file.html");
}

void testUndo() {
	RepoOffer test_repo;
	OfferValidator test_valid;
	Wishlist test_wish;
	ServiceOffer test_serv(test_repo, test_valid);
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	test_serv.addServiceOffer(denum, dest, type, price);
	string denum2 = "Business";
	string dest2 = "Odesa";
	string type2 = "Tren";
	double price2 = 169;
	test_serv.addServiceOffer(denum2, dest2, type2, price2);
	auto& offers = test_serv.getAllService();
	assert(offers.size() == 2);
	test_serv.Undo();
	assert(offers.size() == 1);
	test_serv.addServiceOffer(denum2, dest2, type2, price2);
	Offer ofr1{ denum, dest, type, price };
	test_serv.deleteServiceForUndo(ofr1);
	assert(offers.size() == 1);
	test_serv.Undo();
	assert(offers.size() == 2);
	Offer new_ofr{ "a", "b", "c", 14 };
	test_serv.modifyServiceForUndo(ofr1, new_ofr);
	assert(offers.size() == 2);
	assert(offers[1].getDenumire() == "a");
	test_serv.Undo();
	assert(offers[1].getDenumire() == denum);
	assert(offers.size() == 2);
}