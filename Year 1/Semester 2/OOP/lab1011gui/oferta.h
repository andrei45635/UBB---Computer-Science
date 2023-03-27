#pragma once

#include <string>
using std::string;

/*
* Clasa oferta:
* Atribute:
* -> string denum: denumirea ofertei
* -> string dest: destinatia ofertei
* -> string type: tipul ofertei
* -> double price: pretul ofertei
*/
class Offer {
private:

	string denum;
	string dest;
	string type;
	double price{};

public:

	/*
	* getter pentru denumire
	*/
	string getDenumire() const;

	/*
	* getter pentru destinatie
	*/
	string getDestinatie() const;

	/*
	* getter pentru tip
	*/
	string getType() const;

	/*
	* getter pentru pret
	*/
	double getPrice() const;

	/*
	* Constructorul ofertei
	* Primeste ca parametri atributele private ale ofertei
	*/
	Offer(string denum, string dest, string type, double price) : denum{ denum }, dest{ dest }, type{ type }, price{ price }{
	}

	string toString() const;
};

void testCreateOffer();