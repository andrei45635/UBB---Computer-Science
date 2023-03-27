#pragma once
#include "qwidget.h"
#include "offer_service.h"
#include "Observer.h"
#include "qpainter.h"

class HistogramGUI :public QWidget, public Observer {
private:
	ServiceOffer& serv;
public:
	HistogramGUI(ServiceOffer& serv) : serv{ serv } {
		serv.addObserver(this);
	}
	void paintEvent(QPaintEvent* ev) override {
		QPainter p{ this };
		p.setRenderHint(QPainter::Antialiasing);
		int x = 0;
		int y = 0;
		for (const auto& ofr : serv.get_all_from_wish()) {
			x = rand() % 400 + 1;
			y = rand() % 400 + 1;
			p.drawRect(x, y, 20, 37);
			x += 40;
		}
	}
	void updateLst() override {
		repaint();
	}
	void updateTbl() override {
		repaint();
	}
	~HistogramGUI() {	
		serv.removeObserver(this);
	}
};