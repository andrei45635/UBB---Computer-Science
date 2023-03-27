#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#include <iostream>
#include "oferta.h"
#include "offer_repo.h"
#include "offer_service.h"
#include "UI.h"

void runAllTests_console() {
	std::cout << "beginning testing..." << std::endl;
	testCreateOffer();
	test_create_repo();
	test_delete_repo();
	test_modify_repo();
	test_find_repo();
	testCreateService();
	testDeleteOfferService();
	testModifyOfferService();
	testFindOfferService();
	testFilters();
	testSorts();
	testAddCart();
	testDeleteFromCart();
	testGenerateRandom();
	testAddToWish();
	testDeleteWish();
	testGenerateWish();
	std::cout << "finished testing..." << std::endl;
}

void main2() {
	runAllTests_console();
	OfferValidator valid;
	RepoOffer repo;
	//FileRepoOffer file_repo("oferte.txt");
	Wishlist wish;
	ServiceOffer serv(repo, valid);
	UI ui(serv);
	ui.startUI();
}

int main_console() {
	main2();
	_CrtDumpMemoryLeaks();
	return 0;
}