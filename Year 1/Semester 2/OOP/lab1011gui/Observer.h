#pragma once
#include <vector>
#include <algorithm>

using std::vector;

class Observer {
public:
	virtual void updateTbl() = 0;
	virtual void updateLst() = 0;
};

class Observable {
private:
	vector<Observer*> observed;
protected:
	void notifyTbl() {
		for (auto obs : observed) {
			obs->updateTbl();
		}
	}
	void notifyLst() {
		for (auto obs : observed) {
			obs->updateLst();
		}
	}
public:
	void addObserver(Observer* obs) {
		observed.push_back(obs);
	}
	void removeObserver(Observer* obs) {
		observed.erase(std::remove(observed.begin(), observed.end(), obs));
	}
};