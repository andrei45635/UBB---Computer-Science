#pragma once
#include <QAbstractListModel>
#include <vector>
#include "oferta.h"

class MyListModel : public QAbstractListModel {
private:
	std::vector<Offer> offers;
public:
	MyListModel(const std::vector<Offer>& offers) : offers{ offers } {};

	int rowCount(const QModelIndex& parent = QModelIndex()) const override { return offers.size(); };

	int columnCount(const QModelIndex& parent = QModelIndex()) const override { return 4; }

	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override {
		if (role == Qt::DisplayRole) {
			auto denum = offers[index.row()].getDenumire();
			return QString::fromStdString(denum);
		}

		if (role == Qt::UserRole) {
			auto dest = offers[index.row()].getDestinatie();
			return QString::fromStdString(dest);
		}

		if (role == Qt::DecorationRole) {
			auto type = offers[index.row()].getType();
			return QString::fromStdString(type);
		}

		if (role == Qt::BackgroundRole) {
			auto price = offers[index.row()].getPrice();
			return QString::number(price);
		}

		return QVariant{};
	}

	void setOffersList(const std::vector<Offer>& offers) {
		this->offers = offers;
		auto topLeft = createIndex(0, 0);
		auto bottomRight = createIndex(rowCount(), 1);
		emit dataChanged(topLeft, bottomRight);
	}

};