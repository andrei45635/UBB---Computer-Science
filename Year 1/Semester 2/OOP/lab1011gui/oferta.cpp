#include "oferta.h"
#include <cassert>
#include <string>
#include <cmath>
#include <iostream>

string Offer::getDenumire() const {
	return denum;
}

string Offer::getDestinatie() const {
	return dest;
}

string Offer::getType() const {
	return type;
}

double Offer::getPrice() const {
	return round(price * 1000.0)/1000.0;
}

string Offer::toString() const {
	return "Name: " + denum + ", destination: " + dest + ", type: " + type + ", price: " + std::to_string(round(price * 1000.0) / 1000.0);
}

void testCreateOffer() {
	string denum = "Familie";
	string dest = "Kiev";
	string type = "Roadtrip";
	double price = 69;
	Offer ofr{ denum, dest, type, price };
	assert(ofr.getDenumire() == denum);
	assert(ofr.getDestinatie() == dest);
	assert(ofr.getType() == type);
	assert(fabs(ofr.getPrice() - price) < 0.00001);
	ofr.toString();
}