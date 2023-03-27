#pragma once

#include "oferta.h"
//#include "VectDinamic.h"
#include <vector>

using std::vector;

/*
* Clasa RepoException
* Intoarce un mesaj de eroare daca este cazul
*/
class RepoException {
private:

	string mesg;

public:

	/*
	* Constructor pentru clasa RepoException
	* Primeste atributul string msg = mesajul erorii
	*/
	RepoException(string msg) : mesg{ msg } {

	}

	/*
	* getter pentru mesaj
	*/
	string getMessage();
	//std::string get_msg() const { for (const auto& exp : exceptions) return exp; }

};

class RepoOffer {
private:

	/*
	* Lista cu oferte din repo, reprezentata pe vector dinamic din STL
	*/
	//VectDinamic<Offer> offers;
	vector<Offer> offers;

public:

	/*
	* Adauga oferte in repo
	* pre: ofr = oferta
	* post: oferta a fost adaugata in repo
	*/
	void addRepoOffer(const Offer& ofr);

	/*
	* Nu permitem copierea de obiecte
	*/
	RepoOffer(const RepoOffer& ot) = delete;
	RepoOffer() = default;

	/*
	* getter pentru toate ofertele
	*/
	//const VectDinamic<Offer>& getAll();
	const vector<Offer>& getAll();

	/*
	* Sterge oferta din repo
	* pre: pos = pozitia din repo
	* post: oferta a fost stearsa
	*/
	void deleteRepoOffer(int pos);

	/*
	* Modifica oferta din repo
	* pre: pos = pozitia din repo
	*	   new_ofr = oferta noua cu care se va inlocui
	* post: oferta a fost modificata
	*/
	void modifyRepoOffer(int pos, const Offer& new_ofr);

	/*
	* Returneaza oferta de pe pozitia cautata
	* pre: pos = pozitia cautata
	* post: oferta de pe pozitia cautata
	*/
	Offer findOfferRepo(int pos);

	void deleteOffersForUndo(const Offer& ofr);

	void modifyOfferForUndo(const Offer& old_ofr, const Offer& new_ofr);
};

/*
* clasa FileRepoOffer mosteneste metodele publice din clasa RepoOffer

class FileRepoOffer : public RepoOffer {
private:
	string fileName;
	void loadFromFile();
	void writeToFile();

public:
	FileRepoOffer(const string& fileName) : RepoOffer(), fileName{ fileName } {
		loadFromFile(); //incarcam datele din fisier
	};

	void addRepoOffer(const Offer& ofr) override {
		RepoOffer::addRepoOffer(ofr);
		writeToFile();
	}

	void deleteRepoOffer(int pos) override {
		RepoOffer::deleteRepoOffer(pos);
		writeToFile();
	}
};*/

void test_create_repo();
void test_delete_repo();
void test_modify_repo();
void test_find_repo();