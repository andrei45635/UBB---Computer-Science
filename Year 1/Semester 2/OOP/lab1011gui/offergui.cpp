#include "offergui.h"

void OfferGUI::initGUIfields() {
	serv.addObserver(this);
	setLayout(hLay);
	setLayout(vLay);
	QWidget* windLeft = new QWidget();
	QVBoxLayout* leftLayout = new QVBoxLayout();
	windLeft->setLayout(leftLayout);
	offer_list->setFixedSize(460, 200);
	leftLayout->addWidget(offer_list);
	leftLayout->addWidget(btnFiltDest);
	leftLayout->addWidget(btnFiltPrice);
	leftLayout->addWidget(btnSearch);
	leftLayout->addWidget(btnSortDen);
	leftLayout->addWidget(btnSortDest);
	leftLayout->addWidget(btnSortTypePrice);
	hLay->addWidget(windLeft);
	QWidget* wind_det = new QWidget();
	wind_det->setLayout(formLayout);
	formLayout->addRow(new QLabel("Name"), denumire_txt);
	formLayout->addRow(new QLabel("Destination"), destinatie_txt);
	formLayout->addRow(new QLabel("Type"), type_txt);
	formLayout->addRow(new QLabel("Price"), price_txt);
	formLayout->addRow(new QLabel("Position to find"), position_of_offer_to_search);
	dynWindow->setLayout(dynLay);
	updateList(offer_list);
	updateDynBtnGUI();
	hLay->addWidget(dynWindow);
	hLay->addLayout(vLay);
	vLay->addWidget(wind_det);
	vLay->addWidget(btnAdd);
	vLay->addWidget(btnDel);
	vLay->addWidget(btnModify);
	vLay->addWidget(btnUndo);
	vLay->addWidget(btnWish);
	vLay->addWidget(btnPopulate);
	vLay->addWidget(btnWind);
	vLay->addWidget(btnMoisa);
}

void OfferGUI::clearLayout(QLayout* lay) {
	if (lay == NULL) return;
	QLayoutItem* item;
	while ((item = lay->takeAt(0))) {
		if (item->layout()) {
			clearLayout(item->layout());
			delete item->layout();
		}
		if (item->widget()) delete item->widget();
		delete item;
	}
}

int OfferGUI::howMany(const std::vector<Offer>& offers, const string& dest) {
	return std::count_if(offers.begin(), offers.end(), [&](const Offer& ofr) { return ofr.getDestinatie() == dest; });
}

void OfferGUI::updateDynBtnGUI() {
	clearLayout(this->dynLay);
	std::set<string> dests;
	auto offers = serv.getAllService();
	for (const auto& ofr : offers) {
		dests.insert(ofr.getDestinatie());
	}
	for (const auto& dst : dests) {
		auto btnDyn = new QPushButton(QString::fromStdString(dst));
		dynLay->addWidget(btnDyn);
		int many = howMany(offers, dst);
		QObject::connect(btnDyn, &QPushButton::clicked, [this, btnDyn, dst, many]() {
			QMessageBox::information(nullptr, "Info", QString::fromStdString("Oferte cu destinatia: " + dst + ": " + std::to_string(many)));
			//delete btnDyn;
			});
	}
}

void OfferGUI::checkKievGUI() {
	QDialog* kiev = new QDialog();
	QLabel* hohoLabel = new QLabel();
	QVBoxLayout* kieV = new QVBoxLayout();
	kiev->setModal(true);
	auto& hohols = serv.getAllService();
	bool res = std::all_of(hohols.begin(), hohols.end(), [](const Offer& ofr) { return ofr.getDestinatie() == "Kiev"; });
	if (res) hohoLabel->setText("Good luck in Kiev!");
	else hohoLabel->setText("You dodged a bullet!");
	kieV->addWidget(hohoLabel);
	kiev->setLayout(kieV);
	kiev->exec();
}

void OfferGUI::updateList(QListWidget* lst) {
	offer_list->clear();
	for (const auto& ofr : serv.getAllService()) {
		QString string = QString::fromStdString(ofr.toString());
		QListWidgetItem* item = new QListWidgetItem(string, lst);
	}
	updateDynBtnGUI();
}

void OfferGUI::updateWishGen(QTableWidget* wishtbl) {
	wishtbl->clear();
	wishtbl->setRowCount(serv.get_all_from_wish().size());
	wishtbl->setColumnCount(4);
	const auto& offers = serv.get_all_from_wish();
	for (int row = 0; row < offers.size(); row++) {
		wishtbl->setItem(row, 0, new QTableWidgetItem(QString::fromStdString(offers[row].getDenumire())));
		wishtbl->setItem(row, 1, new QTableWidgetItem(QString::fromStdString(offers[row].getDestinatie())));
		wishtbl->setItem(row, 2, new QTableWidgetItem(QString::fromStdString(offers[row].getType())));
		wishtbl->setItem(row, 3, new QTableWidgetItem(QString::number(offers[row].getPrice())));
		for (int j = 0; j < wishtbl->columnCount(); j++) {
			if (QString::fromStdString(offers[row].getDenumire()) == "Honeymoon")
				wishtbl->item(row, j)->setBackground(Qt::green);
			else wishtbl->item(row, j)->setBackground(Qt::red);
		}
	}
	//for (const auto& wsh : offers) {
		//QString string = QString::fromStdString(wsh.toString());
		//QListWidgetItem* item = new QListWidgetItem(string, wishlst);
	//}
}

void OfferGUI::updateWish(QTableWidget* wishtbl) {
	wishtable->clear();
	wishtable->setRowCount(serv.get_all_from_wish().size());
	wishtable->setColumnCount(4);
	const auto& offers = serv.get_all_from_wish();
	for (int row = 0; row < offers.size(); row++) {
		wishtable->setItem(row, 0, new QTableWidgetItem(QString::fromStdString(offers[row].getDenumire())));
		wishtable->setItem(row, 1, new QTableWidgetItem(QString::fromStdString(offers[row].getDestinatie())));
		wishtable->setItem(row, 2, new QTableWidgetItem(QString::fromStdString(offers[row].getType())));
		wishtable->setItem(row, 3, new QTableWidgetItem(QString::number(offers[row].getPrice())));
		for (int j = 0; j < wishtable->columnCount(); j++) {
			if (QString::fromStdString(offers[row].getDenumire()) == "Honeymoon")
				wishtable->item(row, j)->setBackground(Qt::green);
			else wishtable->item(row, j)->setBackground(Qt::red);
		}
	}
	//for (const auto& wsh : offers) {
		//QString string = QString::fromStdString(wsh.toString());
		//QListWidgetItem* item = new QListWidgetItem(string, wishlst);
	//}
}

void OfferGUI::addOfferGUI() {
	try {
		serv.addServiceOffer(denumire_txt->text().toStdString(), destinatie_txt->text().toStdString(), type_txt->text().toStdString(), price_txt->text().toDouble());
		updateList(offer_list);
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
	catch (ValidException& msg) {
		QMessageBox::critical(this, "Critical", QString::fromStdString(msg.get_msg()));
	}
}

void OfferGUI::delOfferGUI() {
	try {
		Offer ofr{ denumire_txt->text().toStdString(), destinatie_txt->text().toStdString(), type_txt->text().toStdString(), price_txt->text().toDouble() };
		serv.deleteServiceForUndo(ofr);
		updateList(offer_list);
		updateDynBtnGUI();
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUI::undoGUI() {
	try {
		serv.Undo();
		updateList(offer_list);
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUI::populateGUI() {
	try {
		serv.addServiceOffer("Familie", "Kiev", "Roadtrip", 69);
		serv.addServiceOffer("Familie", "Odesa", "Voiaj", 100);
		serv.addServiceOffer("Business", "Moscova", "Zbor", 129);
		serv.addServiceOffer("Honeymoon", "Petrograd", "Masina", 420);
		serv.addServiceOffer("Familie", "Kiev", "Masina", 69);
		serv.addServiceOffer("Honeymoon", "Odesa", "Voiaj", 100);
		serv.addServiceOffer("Cruise", "Moscova", "Tren", 129);
		serv.addServiceOffer("Familie", "Petrograd", "Tren", 420);
		updateList(offer_list);
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUI::filtDestGUI() {
	QDialog* dlg = new QDialog();
	QListWidget* dlgList = new QListWidget();
	QHBoxLayout* hDlg = new QHBoxLayout();
	QVBoxLayout* vDlg = new QVBoxLayout();
	QFormLayout* formFiltDest = new QFormLayout();
	QPushButton* btnFiltInside = new QPushButton("Filter!");
	dlg->setModal(true);
	vDlg->addWidget(btnFiltInside);
	hDlg->addWidget(dlgList);
	hDlg->addLayout(vDlg);
	formFiltDest->addRow(new QLabel("Destination to filter"), filter_price);
	hDlg->addLayout(formFiltDest);
	dlg->setLayout(hDlg);
	dlgList->clear();
	QObject::connect(btnFiltInside, &QPushButton::clicked, this, [&]() {
		const auto& filtered = serv.filtrare_dest(filter_price->text().toStdString());
		for (const auto& ofr : filtered) {
			QString string = QString::fromStdString(ofr.toString());
			QListWidgetItem* item = new QListWidgetItem(string, dlgList);
		}
		});
	dlg->exec();
	updateList(dlgList);
	updateList(offer_list);
}

void OfferGUI::filtPriceGUI() {
	QDialog* dlg = new QDialog();
	QListWidget* dlgList = new QListWidget();
	QHBoxLayout* hDlg = new QHBoxLayout();
	QVBoxLayout* vDlg = new QVBoxLayout();
	QFormLayout* formFiltPrice = new QFormLayout();
	QPushButton* btnFiltInside = new QPushButton("Filter!");
	dlg->setModal(true);
	vDlg->addWidget(btnFiltInside);
	hDlg->addWidget(dlgList);
	hDlg->addLayout(vDlg);
	formFiltPrice->addRow(new QLabel("Price to filter"), filter_price);
	hDlg->addLayout(formFiltPrice);
	dlg->setLayout(hDlg);
	dlgList->clear();
	QObject::connect(btnFiltInside, &QPushButton::clicked, this, [&]() {
		const auto& filtered = serv.filtrare_pret(filter_price->text().toInt());
		for (const auto& ofr : filtered) {
			QString string = QString::fromStdString(ofr.toString());
			QListWidgetItem* item = new QListWidgetItem(string, dlgList);
		}
		});
	dlg->exec();
	updateList(dlgList);
	updateList(offer_list);
}

void OfferGUI::searchOfferGUI() {
	QDialog* dlg = new QDialog();
	QVBoxLayout* vdlg = new QVBoxLayout();
	QLabel* lblOffer = new QLabel();
	dlg->setModal(true);
	vdlg->addWidget(lblOffer);
	dlg->setLayout(vdlg);
	auto offer = serv.findOfferService(position_of_offer_to_search->text().toInt());
	lblOffer->setText(QString::fromStdString(offer.toString()));
	position_of_offer_to_search->clear();
	dlg->exec();
	updateList(offer_list);
}

void OfferGUI::modifyOfferGUI() {
	QDialog* dlg = new QDialog();
	QVBoxLayout* vdlg = new QVBoxLayout();
	QVBoxLayout* vdlg1 = new QVBoxLayout();
	QFormLayout* formDlg = new QFormLayout();
	QPushButton* modOffer = new QPushButton("Modify!");
	dlg->setModal(true);
	vdlg1->addWidget(modOffer);
	formDlg->addRow(new QLabel("New offer"));
	formDlg->addRow(new QLabel("New name"), new_denum);
	formDlg->addRow(new QLabel("New destination"), new_dest);
	formDlg->addRow(new QLabel("New type"), new_type);
	formDlg->addRow(new QLabel("New price"), new_price);
	formDlg->addRow(new QLabel("Current offer"));
	formDlg->addRow(new QLabel("Current name"), old_denum);
	formDlg->addRow(new QLabel("Current destination"), old_dest);
	formDlg->addRow(new QLabel("Current type"), old_type);
	formDlg->addRow(new QLabel("Current price"), old_price);
	vdlg1->addLayout(vdlg);
	vdlg->addLayout(formDlg);
	dlg->setLayout(vdlg1);
	try {
		QObject::connect(modOffer, &QPushButton::clicked, this, &OfferGUI::modGUI);
		updateList(offer_list);
	}
	catch (ValidException& msg) {
		QMessageBox::critical(this, "Validation Error!", QString::fromStdString(msg.get_msg()));
	}
	dlg->exec();
}

void OfferGUI::modGUI() {
	//serv.modifyServiceOffer(positionToMod->text().toInt(), new_denum->text().toStdString(), new_dest->text().toStdString(), new_type->text().toStdString(), new_price->text().toDouble());
	Offer old_ofr{ old_denum->text().toStdString(), old_dest->text().toStdString(), old_type->text().toStdString(), old_price->text().toDouble() };
	Offer new_ofr{ new_denum->text().toStdString(), new_dest->text().toStdString(), new_type->text().toStdString(), new_price->text().toDouble() };
	serv.modifyServiceForUndo(old_ofr, new_ofr);
	updateList(offer_list);
}

void OfferGUI::sortDenumGUI() {
	const auto& sorted = serv.sortDenumire();
	offer_list->clear();
	for (const auto& srt : sorted) {
		QString string = QString::fromStdString(srt.toString());
		QListWidgetItem* item = new QListWidgetItem(string, offer_list);
	}
}

void OfferGUI::sortDestGUI() {
	const auto& sorted = serv.sortDest();
	offer_list->clear();
	for (const auto& srt : sorted) {
		QString string = QString::fromStdString(srt.toString());
		QListWidgetItem* item = new QListWidgetItem(string, offer_list);
	}
}

void OfferGUI::sortTypePriceGUI() {
	//const auto& sorted = serv.sortFinal();
	const auto& sorted = serv.sorted();
	offer_list->clear();
	for (const auto& srt : sorted) {
		QString string = QString::fromStdString(srt.toString());
		QListWidgetItem* item = new QListWidgetItem(string, offer_list);
	}
}

void OfferGUI::updateLabel(QLabel* lbl) {
	lbl->clear();
	lbl->setText("Current offers in the wishlist: " + QString::number(serv.get_all_from_wish().size()));
}

void OfferGUI::newWishWindowGUI() {
	serv.wish.addObserver(this);
	QWidget* newWind = new QWidget();
	QVBoxLayout* vLayWishWind = new QVBoxLayout();
	QFormLayout* formLayoutWishWind = new QFormLayout();
	QLineEdit* newWishDest = new QLineEdit();
	QLineEdit* newWishRandomNumber = new QLineEdit();
	QLineEdit* newWishFileName = new QLineEdit();
	QTableWidget* newWishTable = new QTableWidget();
	QPushButton* btnNewAddWishlist = new QPushButton("Add to the wishlist");
	QPushButton* btnNewDelWishlist = new QPushButton("Delete from wishlist");
	QPushButton* btnNewRandomWishlist = new QPushButton("Generate random offers");
	QPushButton* btnNewExportHTML = new QPushButton("Export the wishlist to HTML");
	newWind->setLayout(vLayWishWind);
	//vLayWishWind->addWidget(newWishTable);
	vLayWishWind->addWidget(wishtable);
	QLabel* newCurrOfrs = new QLabel();
	updateLabel(newCurrOfrs);
	vLayWishWind->addWidget(newCurrOfrs);
	vLayWishWind->addLayout(formLayoutWishWind);
	formLayoutWishWind->addRow(new QLabel("Destination"), newWishDest);
	formLayoutWishWind->addRow(new QLabel("Random generator"), newWishRandomNumber);
	formLayoutWishWind->addRow(new QLabel("File name (add .html)"), newWishFileName);
	vLayWishWind->addWidget(btnNewAddWishlist);
	vLayWishWind->addWidget(btnNewDelWishlist);
	vLayWishWind->addWidget(btnNewRandomWishlist);
	vLayWishWind->addWidget(btnNewExportHTML);

	QObject::connect(btnNewAddWishlist, &QPushButton::clicked, this, [=]() {
		try {
			serv.add_to_wishlist(newWishDest->text().toStdString());
			updateWishGen(wishtable);
			updateList(offer_list);
			updateLabel(newCurrOfrs);
		}
		catch (WishExcept& msg) {
			QMessageBox::critical(newWind, "Critical!", QString::fromStdString(msg.getMessage()));
		}});

	QObject::connect(btnNewDelWishlist, &QPushButton::clicked, this, [=]() {
		wishtable->clear();
		serv.delete_from_wishlist();
		updateWishGen(wishtable);
		updateLabel(newCurrOfrs); });

	QObject::connect(btnNewRandomWishlist, &QPushButton::clicked, this, [=]() {
		try {
			if (newWishRandomNumber->text().toInt() < 0) {
				QMessageBox::critical(newWind, "Critical!", QString::fromStdString("You can't generate negative offers!"));
			}
			else if (newWishRandomNumber->text().toInt() > serv.getAllService().size()) {
				QMessageBox::critical(newWind, "Critical!", QString::fromStdString("Invalid number!"));
			}
			else {
				serv.generate_random_offers(newWishRandomNumber->text().toInt());
				updateWishGen(wishtable);
				updateList(offer_list);
				updateLabel(newCurrOfrs);
				newWishRandomNumber->clear();
			}
		}
		catch (WishExcept& msg) {
			QMessageBox::critical(newWind, "Critical!", QString::fromStdString(msg.getMessage()));
		}
		catch (ValidException& msg) {
			QMessageBox::critical(newWind, "Critical!", QString::fromStdString(msg.get_msg()));
		}
		catch (RepoException& msg) {
			QMessageBox::critical(newWind, "Critical!", QString::fromStdString(msg.getMessage()));
		}
		});

	QObject::connect(btnNewExportHTML, &QPushButton::clicked, this, [=]() {
		try {
			serv.exporta_cos_HTML(newWishFileName->text().toStdString());
		}
		catch (RepoException& msg) {
			QMessageBox::critical(newWind, "Critical!", QString::fromStdString(msg.getMessage()));
		}
		QMessageBox::information(newWind, "Success!", QString::fromStdString("Successfully exported!"));
		});

	updateWish(newWishTable);
	newWind->show();
}

void OfferGUI::createWishlistGUI() {
	serv.wish.addObserver(this);
	QWidget* newWind = new QWidget();
	wish->setLayout(vLayWish);
	vLayWish->addWidget(wishtable);
	updateLabel(currOfrs);
	vLayWish->addWidget(currOfrs);
	vLayWish->addLayout(formLayoutWish);
	formLayoutWish->addRow(new QLabel("Destination"), wish_dest);
	formLayoutWish->addRow(new QLabel("Random generator"), randomNumber);
	formLayoutWish->addRow(new QLabel("File name (add .html)"), fileName);
	vLayWish->addWidget(btnAddWishlist);
	vLayWish->addWidget(btnDelWishlist);
	vLayWish->addWidget(btnRandomWishlist);
	vLayWish->addWidget(btnExportHTML);
	//newWind->set
	wish->show();
}

void OfferGUI::addWishlistGUI() {
	try {
		serv.add_to_wishlist(wish_dest->text().toStdString());
		updateWish(wishtable);
		updateList(offer_list);
		updateLabel(currOfrs);
	}
	catch (WishExcept& msg) {
		QMessageBox::critical(this->wish, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUI::delWishlistGUI() {
	wishtable->clear();
	serv.delete_from_wishlist();
	updateWish(wishtable);
	updateLabel(currOfrs);
}

void OfferGUI::randomWishlistGUI() {
	try {
		if (randomNumber->text().toInt() < 0) {
			QMessageBox::critical(this->wish, "Critical!", QString::fromStdString("You can't generate negative offers!"));
		}
		else if (randomNumber->text().toInt() > serv.getAllService().size()) {
			QMessageBox::critical(this->wish, "Critical!", QString::fromStdString("Invalid number!"));
		}
		else {
			serv.generate_random_offers(randomNumber->text().toInt());
			updateWish(wishtable);
			updateList(offer_list);
			updateLabel(currOfrs);
			randomNumber->clear();
		}
	}
	catch (WishExcept& msg) {
		QMessageBox::critical(this->wish, "Critical!", QString::fromStdString(msg.getMessage()));
	}
	catch (ValidException& msg) {
		QMessageBox::critical(this->wish, "Critical!", QString::fromStdString(msg.get_msg()));
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this->wish, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUI::exportHTMLGUI() {
	try {
		serv.exporta_cos_HTML(fileName->text().toStdString());
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this->wish, "Critical!", QString::fromStdString(msg.getMessage()));
	}
	QMessageBox::information(wish, "Success!", QString::fromStdString("Successfully exported!"));
}

void OfferGUI::moisaGUI() {
	QWidget* dlg = new QWidget();
	QVBoxLayout* vdlg = new QVBoxLayout();
	QHBoxLayout* hdlg = new QHBoxLayout();
	QListWidget* moisaList = new QListWidget();
	QLabel* moisaLbl = new QLabel();
	QLabel* moisaLbl1 = new QLabel();
	dlg->setLayout(vdlg);
	vdlg->addWidget(moisaList);
	moisaList->setFixedSize(425, 50);
	QPixmap pic("moisa_good.png");
	moisaLbl->setPixmap(pic.scaled(150, 150, Qt::KeepAspectRatio));
	moisaLbl1->setText("Moisa's approved capitalist capitals offer!\n\nNow with Moisa's seal of approval!");
	QFont font = moisaLbl1->font();
	font.setPointSize(12);
	moisaLbl1->setFont(font);
	hdlg->addWidget(moisaLbl);
	hdlg->addWidget(moisaLbl1);
	vdlg->addLayout(hdlg);
	vector<std::string> capitals{ "Paris", "Washington D.C.", "London", "Hong Kong", "Sydney", "Berlin", "Rome", "Madrid", "Lisbon", "Dublin", "Ottawa", "Beijing" };
	vector<std::string> types{ "Voyage", "Roadtrip", "Train", "Flight" };
	vector<std::string> names{ "Business", "Family", "Leisure", "Couples", "Group" };
	int randIndexCapitals = rand() % 12;
	int randIndexTypes = rand() % 4;
	int randIndexNames = rand() % 5;
	auto sneed = std::chrono::system_clock::now().time_since_epoch().count();
	double price = std::rand();
	std::shuffle(names.begin(), names.end(), std::default_random_engine((unsigned int)sneed));
	std::shuffle(capitals.begin(), capitals.end(), std::default_random_engine((unsigned int)sneed + 1));
	std::shuffle(types.begin(), types.end(), std::default_random_engine((unsigned int)sneed + 2));
	Offer ofr{ names[randIndexNames], capitals[randIndexCapitals], types[randIndexTypes], round(price) / 100.00 };
	try {
		serv.addServiceOffer(names[randIndexNames], capitals[randIndexCapitals], types[randIndexTypes], round(price) / 100.00);
		updateList(offer_list);
	}
	catch (ValidException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.get_msg()));
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
	QString moisaString = QString::fromStdString(ofr.toString());
	QListWidgetItem* item = new QListWidgetItem(moisaString, moisaList);
	updateList(offer_list);
	//updateDynBtnGUI();
	dlg->show();
}

void OfferGUI::on_click_add() {
	QObject::connect(btnAdd, &QPushButton::clicked, this, &OfferGUI::addOfferGUI);
}

void OfferGUI::on_click_del() {
	QObject::connect(btnDel, &QPushButton::clicked, this, &OfferGUI::delOfferGUI);
}

void OfferGUI::on_click_filter_dest() {
	QObject::connect(btnFiltDest, &QPushButton::clicked, this, &OfferGUI::filtDestGUI);
}

void OfferGUI::on_click_filter_price() {
	QObject::connect(btnFiltPrice, &QPushButton::clicked, this, &OfferGUI::filtPriceGUI);
}

void OfferGUI::on_click_search() {
	QObject::connect(btnSearch, &QPushButton::clicked, this, &OfferGUI::searchOfferGUI);
}

void OfferGUI::on_click_modify() {
	QObject::connect(btnModify, &QPushButton::clicked, this, &OfferGUI::modifyOfferGUI);
}

void OfferGUI::on_click_sort_denum() {
	QObject::connect(btnSortDen, &QPushButton::clicked, this, &OfferGUI::sortDenumGUI);
}

void OfferGUI::on_click_sort_dest() {
	QObject::connect(btnSortDest, &QPushButton::clicked, this, &OfferGUI::sortDestGUI);
}

void OfferGUI::on_click_sort_type_price() {
	QObject::connect(btnSortTypePrice, &QPushButton::clicked, this, &OfferGUI::sortTypePriceGUI);
}

void OfferGUI::on_click_add_wishlist() {
	QObject::connect(btnAddWishlist, &QPushButton::clicked, this, &OfferGUI::addWishlistGUI);
}

void OfferGUI::on_click_del_wishlist() {
	QObject::connect(btnDelWishlist, &QPushButton::clicked, this, &OfferGUI::delWishlistGUI);
}

void OfferGUI::on_click_random_wishlist() {
	QObject::connect(btnRandomWishlist, &QPushButton::clicked, this, &OfferGUI::randomWishlistGUI);
}

void OfferGUI::on_click_export_HTML() {
	QObject::connect(btnExportHTML, &QPushButton::clicked, this, &OfferGUI::exportHTMLGUI);
}

void OfferGUI::on_click_undo() {
	QObject::connect(btnUndo, &QPushButton::clicked, this, &OfferGUI::undoGUI);
}

void OfferGUI::on_click_createWishlistGUI() {
	QObject::connect(btnWish, &QPushButton::clicked, this, &OfferGUI::createWishlistGUI);
}

void OfferGUI::on_click_populate() {
	QObject::connect(btnPopulate, &QPushButton::clicked, this, &OfferGUI::populateGUI);
}

void OfferGUI::on_click_moisa() {
	QObject::connect(btnMoisa, &QPushButton::clicked, this, &OfferGUI::moisaGUI);
}

void OfferGUI::on_click_Kiev() {
	QObject::connect(btnKiev, &QPushButton::clicked, this, &OfferGUI::checkKievGUI);
}

void OfferGUI::on_click_new_window() {
	QObject::connect(btnWind, &QPushButton::clicked, this, &OfferGUI::newWishWindowGUI);
}

void OfferGUI::on_click_neue() {
	QObject::connect(btnWind, &QPushButton::clicked, this,[=](){
		auto nw = new OfferGUI(serv);
		nw->show();
		});
}