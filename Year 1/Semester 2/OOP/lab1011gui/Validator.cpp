#include "validator.h"
#include <cmath>
#include <iostream>
#include <algorithm>

void OfferValidator::validate_offer(const Offer& ofr) {

	vector<std::string> errs;
	if (ofr.getDenumire().empty() || check_if_digit(ofr.getDenumire())) {
		errs.push_back("denumirea nu poate fi vida sau un numar!\n");
	}
	if (ofr.getDestinatie().empty() || check_if_digit(ofr.getDestinatie())) {
		errs.push_back("destinatia nu poate fi vida sau un numar!\n");
	}
	if (ofr.getType().empty() || check_if_digit(ofr.getType())) {
		errs.push_back("tipul nu poate fi vid sau un numar!\n");
	}
	if (fabs(ofr.getPrice() < 0.00001)) {
		errs.push_back("pretul nu poate fi negativ!\n");
	}
	if (errs.size() != 0) {
		throw ValidException(errs);
	}
}

bool check_if_digit(const string& string) {
	for (int i = 0; i < string.size(); i++) {
		if (string[i] >= 48 && string[i] <= 57) {
			return true;
		}
	}
	return false;
}