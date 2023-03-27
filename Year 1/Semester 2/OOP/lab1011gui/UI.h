#pragma once
#include "offer_service.h"

class UI {
private:

	ServiceOffer& serv;

public:

	UI(ServiceOffer& serv) : serv{ serv } {

	}

	void startUI();

};
