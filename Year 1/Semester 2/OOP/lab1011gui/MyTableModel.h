#pragma once
#include <QAbstractTableModel>
#include <vector>
#include <qbrush.h>
#include "oferta.h"

class MyTableModel : public QAbstractTableModel {
private:
	std::vector<Offer> offers;

public:
	MyTableModel(const std::vector<Offer>& offers) : offers{ offers } {};
	int rowCount(const QModelIndex& parent = QModelIndex()) const override {
		return offers.size();
	}

	int columnCount(const QModelIndex& parent = QModelIndex()) const override {
		return 4;
	}

	QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override {
		if (role == Qt::ForegroundRole) {
			Offer ofr = offers[index.row()];
			if (ofr.getPrice() > 0) {
				return QBrush(Qt::red);
			}
		}

		if (role == Qt::DisplayRole) {
			Offer ofr = offers[index.row()];
			if (index.column() == 0) return QString::fromStdString(ofr.getDenumire());
			else if (index.column() == 1) return QString::fromStdString(ofr.getDestinatie());
			else if (index.column() == 2) return QString::fromStdString(ofr.getType());
			else if (index.column() == 3) return QString::number(ofr.getPrice());
		}

		return QVariant{};
	}

	void setOffer(const vector<Offer>& offers) {
		this->offers = offers;
		auto topLeft = createIndex(0, 0);
		auto bottomRight = createIndex(rowCount(), columnCount());
		emit dataChanged(topLeft, bottomRight);
	}
};