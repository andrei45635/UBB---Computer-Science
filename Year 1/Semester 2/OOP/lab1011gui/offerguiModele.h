#pragma once
#include "qwidget.h"
#include "qlabel.h"
#include "qpushbutton.h"
#include "offer_service.h"
#include "qlineedit.h"
#include "qlistwidget.h"
#include "qboxlayout.h"
#include "qformlayout.h"
#include "qmessagebox.h"
#include "qpixmap.h"
#include "qfont.h"
#include "qtableview.h"
#include "qtablewidget.h"
#include "Observer.h"
#include "MyListModel.h"
#include "MyTableModel.h"
#include <time.h>
#include <algorithm>
#include <chrono>
#include <random>
#include <set>
#include <vector>

class OfferGUIModele : public QWidget{
private:
	ServiceOffer& serv;
	QWidget* wish = new QWidget();
	QWidget* window = new QWidget();
	QWidget* dynWindow = new QWidget();
	QLabel* currOfrs = new QLabel();
	QVBoxLayout* dynLay = new QVBoxLayout();
	QHBoxLayout* hLay = new QHBoxLayout(window);
	QVBoxLayout* vLay = new QVBoxLayout(window);
	QVBoxLayout* vLayWish = new QVBoxLayout();
	QFormLayout* formLayout = new QFormLayout();
	QFormLayout* formLayoutWish = new QFormLayout();
	QPushButton* btnAdd = new QPushButton("Add");
	QPushButton* btnDel = new QPushButton("Delete");
	QPushButton* btnModify = new QPushButton("Modify");
	QPushButton* btnFiltDest = new QPushButton("Destination Filter");
	QPushButton* btnFiltPrice = new QPushButton("Price Filter");
	QPushButton* btnSearch = new QPushButton("Search for an Offer");
	QPushButton* btnSortDen = new QPushButton("Sort by name");
	QPushButton* btnSortDest = new QPushButton("Sort by destination");
	QPushButton* btnSortTypePrice = new QPushButton("Sort by type and price");
	QPushButton* btnUndo = new QPushButton("Undo last operation");
	QPushButton* btnWish = new QPushButton("Generate a wishlist");
	QPushButton* btnKiev = new QPushButton("Hohol finder");
	QPushButton* btnAddWishlist = new QPushButton("Add to the wishlist");
	QPushButton* btnDelWishlist = new QPushButton("Delete from wishlist");
	QPushButton* btnRandomWishlist = new QPushButton("Generate random offers");
	QPushButton* btnExportHTML = new QPushButton("Export the wishlist to HTML");
	QPushButton* btnPopulate = new QPushButton("Populate with 8 offers!");
	QPushButton* btnMoisa = new QPushButton("Capitalist Capitals");
	QPushButton* btnWind = new QPushButton("New Window");
	QLineEdit* denumire_txt = new QLineEdit();
	QLineEdit* destinatie_txt = new QLineEdit();
	QLineEdit* type_txt = new QLineEdit();
	QLineEdit* price_txt = new QLineEdit();
	QLineEdit* new_denum = new QLineEdit();
	QLineEdit* new_dest = new QLineEdit();
	QLineEdit* new_type = new QLineEdit();
	QLineEdit* new_price = new QLineEdit();
	QLineEdit* old_denum = new QLineEdit();
	QLineEdit* old_dest = new QLineEdit();
	QLineEdit* old_type = new QLineEdit();
	QLineEdit* old_price = new QLineEdit();
	QLineEdit* wish_dest = new QLineEdit();
	QLineEdit* filter_dest = new QLineEdit();
	QLineEdit* filter_price = new QLineEdit();
	QLineEdit* position_of_offer_to_search = new QLineEdit();
	QLineEdit* position_of_offer_to_del = new QLineEdit();
	QLineEdit* randomNumber = new QLineEdit();
	QLineEdit* fileName = new QLineEdit();
	QLineEdit* positionToMod = new QLineEdit();
	MyListModel* modelList;
	MyTableModel* modelTable;
	QListView* lstV = new QListView();
	QTableView* tblV = new QTableView();

	void addOfferGUI();
	void delOfferGUI();
	void modifyOfferGUI();
	void modGUI();
	void searchOfferGUI();
	void filtDestGUI();
	void filtPriceGUI();
	void sortDenumGUI();
	void sortDestGUI();
	void sortTypePriceGUI();
	void createWishlistGUI();
	void addWishlistGUI();
	void delWishlistGUI();
	void randomWishlistGUI();
	void exportHTMLGUI();
	void undoGUI();
	void moisaGUI();
	void populateGUI();
	void updateDynBtnGUI();
	void clearLayout(QLayout* lay);
	int howMany(const std::vector<Offer>& offers, const string& dest);
	void on_click_add();
	void on_click_del();
	void on_click_filter_dest();
	void on_click_filter_price();
	void on_click_search();
	void on_click_modify();
	void on_click_sort_denum();
	void on_click_sort_dest();
	void on_click_sort_type_price();
	void on_click_add_wishlist();
	void on_click_del_wishlist();
	void on_click_random_wishlist();
	void on_click_export_HTML();
	void on_click_undo();
	void on_click_createWishlistGUI();
	void on_click_populate();
	void on_click_moisa();
	void initGUIfields();
	void checkKievGUI();
	void on_click_Kiev();
	void on_click_neue();
	void on_click_item_show();
	void updateList(const std::vector<Offer>& offers);
	void updateListOld(QListWidget* lst);
	void updateWish(const std::vector<Offer>& offers);
	void updateWishGen(QTableWidget* wishtbl);
	void updateLabel(QLabel* lbl);

public:
	OfferGUIModele(ServiceOffer& serv) : serv{ serv } {
		initGUIfields();
		modelList = new MyListModel(serv.getAllService());
		modelTable = new MyTableModel(serv.get_all_from_wish());
		lstV->setModel(modelList);
		tblV->setModel(modelTable);
		on_click_createWishlistGUI();
		on_click_add();
		on_click_del();
		on_click_filter_dest();
		on_click_filter_price();
		on_click_search();
		on_click_modify();
		on_click_sort_denum();
		on_click_sort_dest();
		on_click_sort_type_price();
		on_click_add_wishlist();
		on_click_del_wishlist();
		on_click_random_wishlist();
		on_click_export_HTML();
		on_click_undo();
		on_click_populate();
		on_click_moisa();
		on_click_Kiev();
		on_click_neue();
		on_click_item_show();
		updateDynBtnGUI();
	}
};
