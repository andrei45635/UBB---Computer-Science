#pragma once
#include <string>
#include "oferta.h"
//#include "VectDinamic.h"
#include <vector>

using std::vector;

class ValidException {
private:
	vector<std::string> exceptions;
public:
	//constructor pentru validator
	ValidException(vector<std::string> exceptions) : exceptions{ exceptions } {}
	//getter pentru validator
	const vector<std::string>& get_error() const { return this->exceptions; }
	std::string get_msg() const { for (const auto& exp : exceptions) return exp; }
};

class OfferValidator {
public:
	void validate_offer(const Offer& ofr);
};

bool check_if_digit(const string& string);