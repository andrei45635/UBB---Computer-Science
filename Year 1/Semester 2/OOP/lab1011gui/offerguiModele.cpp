#include "offerguiModele.h"


void OfferGUIModele::initGUIfields() {
	setLayout(hLay);
	setLayout(vLay);
	QWidget* windLeft = new QWidget();
	QVBoxLayout* leftLayout = new QVBoxLayout();
	windLeft->setLayout(leftLayout);
	lstV = new QListView();
	lstV->setUniformItemSizes(true);
	leftLayout->addWidget(lstV);
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

void OfferGUIModele::clearLayout(QLayout* lay) {
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

int OfferGUIModele::howMany(const std::vector<Offer>& offers, const string& dest) {
	return std::count_if(offers.begin(), offers.end(), [&](const Offer& ofr) { return ofr.getDestinatie() == dest; });
}

void OfferGUIModele::updateDynBtnGUI() {
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

void OfferGUIModele::checkKievGUI() {
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

void OfferGUIModele::updateList(const std::vector<Offer>& offers) {
	modelList->setOffersList(offers);
	updateDynBtnGUI();
}

void OfferGUIModele::updateListOld(QListWidget* lst) {
	lst->clear();
	for (const auto& ofr : serv.getAllService()) {
		QString string = QString::fromStdString(ofr.toString());
		QListWidgetItem* item = new QListWidgetItem(string, lst);
	}
}

void OfferGUIModele::updateWishGen(QTableWidget* wishtbl) {
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
}

void OfferGUIModele::updateWish(const std::vector<Offer>& offers) {
	modelTable->setOffer(offers);
}

void OfferGUIModele::addOfferGUI() {
	try {
		serv.addServiceOffer(denumire_txt->text().toStdString(), destinatie_txt->text().toStdString(), type_txt->text().toStdString(), price_txt->text().toDouble());
		updateList(serv.getAllService());
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
	catch (ValidException& msg) {
		QMessageBox::critical(this, "Critical", QString::fromStdString(msg.get_msg()));
	}
}

void OfferGUIModele::delOfferGUI() {
	try {
		Offer ofr{ denumire_txt->text().toStdString(), destinatie_txt->text().toStdString(), type_txt->text().toStdString(), price_txt->text().toDouble() };
		serv.deleteServiceForUndo(ofr);
		updateList(serv.getAllService());
		updateDynBtnGUI();
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUIModele::undoGUI() {
	try {
		serv.Undo();
		updateList(serv.getAllService());
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUIModele::populateGUI() {
	try {
		serv.addServiceOffer("Familie", "Kiev", "Roadtrip", 69);
		serv.addServiceOffer("Familie", "Odesa", "Voiaj", 100);
		serv.addServiceOffer("Business", "Moscova", "Zbor", 129);
		serv.addServiceOffer("Honeymoon", "Petrograd", "Masina", 420);
		serv.addServiceOffer("Familie", "Kiev", "Masina", 69);
		serv.addServiceOffer("Honeymoon", "Odesa", "Voiaj", 100);
		serv.addServiceOffer("Cruise", "Moscova", "Tren", 129);
		serv.addServiceOffer("Familie", "Petrograd", "Tren", 420);
		updateList(serv.getAllService());
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUIModele::filtDestGUI() {
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
	updateListOld(dlgList);
	updateList(serv.getAllService());
}

void OfferGUIModele::filtPriceGUI() {
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
	updateListOld(dlgList);
	updateList(serv.getAllService());
}

void OfferGUIModele::searchOfferGUI() {
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
	updateList(serv.getAllService());
}

void OfferGUIModele::modifyOfferGUI() {
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
		QObject::connect(modOffer, &QPushButton::clicked, this, &OfferGUIModele::modGUI);
		updateList(serv.getAllService());
	}
	catch (ValidException& msg) {
		QMessageBox::critical(this, "Validation Error!", QString::fromStdString(msg.get_msg()));
	}
	dlg->exec();
}

void OfferGUIModele::modGUI() {
	Offer old_ofr{ old_denum->text().toStdString(), old_dest->text().toStdString(), old_type->text().toStdString(), old_price->text().toDouble() };
	Offer new_ofr{ new_denum->text().toStdString(), new_dest->text().toStdString(), new_type->text().toStdString(), new_price->text().toDouble() };
	serv.modifyServiceForUndo(old_ofr, new_ofr);
	updateList(serv.getAllService());
}

void OfferGUIModele::sortDenumGUI() {
	const auto& sorted = serv.sortDenumire();
	updateList(sorted);
}

void OfferGUIModele::sortDestGUI() {
	const auto& sorted = serv.sortDest();
	updateList(sorted);
}

void OfferGUIModele::sortTypePriceGUI() {
	const auto& sorted = serv.sorted();
	updateList(sorted);
}

void OfferGUIModele::updateLabel(QLabel* lbl) {
	lbl->clear();
	lbl->setText("Current offers in the wishlist: " + QString::number(serv.get_all_from_wish().size()));
}

void OfferGUIModele::createWishlistGUI() {
	wish->setLayout(vLayWish);
	tblV = new QTableView();
	vLayWish->addWidget(tblV);
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
	wish->show();
}

void OfferGUIModele::addWishlistGUI() {
	try {
		serv.add_to_wishlist(wish_dest->text().toStdString());
		updateWish(serv.get_all_from_wish());
		updateList(serv.getAllService());
		updateLabel(currOfrs);
	}
	catch (WishExcept& msg) {
		QMessageBox::critical(this->wish, "Critical!", QString::fromStdString(msg.getMessage()));
	}
}

void OfferGUIModele::delWishlistGUI() {
	serv.delete_from_wishlist();
	updateWish(serv.get_all_from_wish());
	updateLabel(currOfrs);
}

void OfferGUIModele::randomWishlistGUI() {
	try {
		if (randomNumber->text().toInt() < 0) {
			QMessageBox::critical(this->wish, "Critical!", QString::fromStdString("You can't generate negative offers!"));
		}
		else if (randomNumber->text().toInt() > serv.getAllService().size()) {
			QMessageBox::critical(this->wish, "Critical!", QString::fromStdString("Invalid number!"));
		}
		else {
			serv.generate_random_offers(randomNumber->text().toInt());
			updateWish(serv.get_all_from_wish());
			updateList(serv.getAllService());
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

void OfferGUIModele::exportHTMLGUI() {
	try {
		serv.exporta_cos_HTML(fileName->text().toStdString());
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this->wish, "Critical!", QString::fromStdString(msg.getMessage()));
	}
	QMessageBox::information(wish, "Success!", QString::fromStdString("Successfully exported!"));
}

void OfferGUIModele::moisaGUI() {
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
		updateList(serv.getAllService());
	}
	catch (ValidException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.get_msg()));
	}
	catch (RepoException& msg) {
		QMessageBox::critical(this, "Critical!", QString::fromStdString(msg.getMessage()));
	}
	QString moisaString = QString::fromStdString(ofr.toString());
	QListWidgetItem* item = new QListWidgetItem(moisaString, moisaList);
	updateList(serv.getAllService());
	dlg->show();
}

void OfferGUIModele::on_click_add() {
	QObject::connect(btnAdd, &QPushButton::clicked, this, &OfferGUIModele::addOfferGUI);
}

void OfferGUIModele::on_click_del() {
	QObject::connect(btnDel, &QPushButton::clicked, this, &OfferGUIModele::delOfferGUI);
}

void OfferGUIModele::on_click_filter_dest() {
	QObject::connect(btnFiltDest, &QPushButton::clicked, this, &OfferGUIModele::filtDestGUI);
}

void OfferGUIModele::on_click_filter_price() {
	QObject::connect(btnFiltPrice, &QPushButton::clicked, this, &OfferGUIModele::filtPriceGUI);
}

void OfferGUIModele::on_click_search() {
	QObject::connect(btnSearch, &QPushButton::clicked, this, &OfferGUIModele::searchOfferGUI);
}

void OfferGUIModele::on_click_modify() {
	QObject::connect(btnModify, &QPushButton::clicked, this, &OfferGUIModele::modifyOfferGUI);
}

void OfferGUIModele::on_click_sort_denum() {
	QObject::connect(btnSortDen, &QPushButton::clicked, this, &OfferGUIModele::sortDenumGUI);
}

void OfferGUIModele::on_click_sort_dest() {
	QObject::connect(btnSortDest, &QPushButton::clicked, this, &OfferGUIModele::sortDestGUI);
}

void OfferGUIModele::on_click_sort_type_price() {
	QObject::connect(btnSortTypePrice, &QPushButton::clicked, this, &OfferGUIModele::sortTypePriceGUI);
}

void OfferGUIModele::on_click_add_wishlist() {
	QObject::connect(btnAddWishlist, &QPushButton::clicked, this, &OfferGUIModele::addWishlistGUI);
}

void OfferGUIModele::on_click_del_wishlist() {
	QObject::connect(btnDelWishlist, &QPushButton::clicked, this, &OfferGUIModele::delWishlistGUI);
}

void OfferGUIModele::on_click_random_wishlist() {
	QObject::connect(btnRandomWishlist, &QPushButton::clicked, this, &OfferGUIModele::randomWishlistGUI);
}

void OfferGUIModele::on_click_export_HTML() {
	QObject::connect(btnExportHTML, &QPushButton::clicked, this, &OfferGUIModele::exportHTMLGUI);
}

void OfferGUIModele::on_click_undo() {
	QObject::connect(btnUndo, &QPushButton::clicked, this, &OfferGUIModele::undoGUI);
}

void OfferGUIModele::on_click_createWishlistGUI() {
	QObject::connect(btnWish, &QPushButton::clicked, this, &OfferGUIModele::createWishlistGUI);
}

void OfferGUIModele::on_click_populate() {
	QObject::connect(btnPopulate, &QPushButton::clicked, this, &OfferGUIModele::populateGUI);
}

void OfferGUIModele::on_click_moisa() {
	QObject::connect(btnMoisa, &QPushButton::clicked, this, &OfferGUIModele::moisaGUI);
}

void OfferGUIModele::on_click_Kiev() {
	QObject::connect(btnKiev, &QPushButton::clicked, this, &OfferGUIModele::checkKievGUI);
}

void OfferGUIModele::on_click_neue() {
	QObject::connect(btnWind, &QPushButton::clicked, this, [=]() {
		auto nw = new OfferGUIModele(serv);
		nw->show();
		});
}

void OfferGUIModele::on_click_item_show() {
	lstV->setModel(modelList);
	QObject::connect(lstV->selectionModel(), &QItemSelectionModel::selectionChanged, [&]() {
		if (lstV->selectionModel()->selectedIndexes().isEmpty()) {
			denumire_txt->setText("");
			destinatie_txt->setText("");
			type_txt->setText("");
			price_txt->setText("");
			return;
		}
		auto selectedIndex = lstV->selectionModel()->selectedIndexes().at(0);
		QString denum = selectedIndex.data(Qt::DisplayRole).toString();
		denumire_txt->setText(denum);
		QString dest = selectedIndex.data(Qt::UserRole).toString();
		destinatie_txt->setText(dest);
		QString type = selectedIndex.data(Qt::DecorationRole).toString();
		type_txt->setText(type);
		QString price = selectedIndex.data(Qt::BackgroundRole).toString();
		price_txt->setText(price);
		});
	QObject::connect(tblV->selectionModel(), &QItemSelectionModel::selectionChanged, [&]() {
		if (tblV->selectionModel()->selectedIndexes().isEmpty()) {
			denumire_txt->setText("");
			destinatie_txt->setText("");
			type_txt->setText("");
			price_txt->setText("");
			return;
		}
		auto selectedRow = tblV->selectionModel()->selectedIndexes().at(0).row();
		auto cell0Index = tblV->model()->index(selectedRow, 0);
		auto cell0Value = cell0Index.data(Qt::ForegroundRole).toString();
		denumire_txt->setText(cell0Value);
		auto cell1Index = tblV->model()->index(selectedRow, 1);
		auto cell1Value = cell1Index.data(Qt::DisplayRole).toString();
		denumire_txt->setText(cell1Value);
		auto cell2Index = tblV->model()->index(selectedRow, 2);
		auto cell2Value = cell2Index.data(Qt::DisplayRole).toString();
		denumire_txt->setText(cell2Value);
		auto cell3Index = tblV->model()->index(selectedRow, 3);
		auto cell3Value = cell3Index.data(Qt::DisplayRole).toString();
		denumire_txt->setText(cell3Value);
		});
}