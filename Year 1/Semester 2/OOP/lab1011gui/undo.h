#pragma once
#include "offer_repo.h"
#include "oferta.h"

class ActiuneUndo {
public:
	virtual void doUndo() = 0;
	virtual ~ActiuneUndo() = default;
};

class AddUndo : public ActiuneUndo {
private:
	RepoOffer& repo_undo;
	Offer offer_undo;
public:
	AddUndo(RepoOffer& repo_undo, Offer offer_undo) : repo_undo{ repo_undo }, offer_undo{ offer_undo }{};
	void doUndo() override {
		repo_undo.deleteOffersForUndo(offer_undo);
	}
};

class DeleteUndo : public ActiuneUndo {
private:
	RepoOffer& repo_undo;
	Offer offer_undo;
public:
	DeleteUndo(RepoOffer& repo_undo, Offer offer_undo) : repo_undo{ repo_undo }, offer_undo{ offer_undo }{};
	void doUndo() override {
		repo_undo.addRepoOffer(offer_undo);
	}
};

class ModifyUndo : public ActiuneUndo {
private:
	RepoOffer& repo_undo;
	Offer old_offer, modified_offer;
public:
	ModifyUndo(RepoOffer& repo_undo, Offer old_offer, Offer modified_offer) : repo_undo{ repo_undo }, old_offer{ old_offer }, modified_offer{ modified_offer }{};
	void doUndo() override {
		repo_undo.deleteOffersForUndo(modified_offer);
		repo_undo.addRepoOffer(old_offer);
	}
};