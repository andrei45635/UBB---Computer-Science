#include <iostream>
#include <algorithm>
#include <vector>
#include "UI.h"

using std::cin;
using std::cout;

void UI::startUI() {
	while (true) {
		cout << "1. Adauga oferte\n2. Printeaza oferte\n3. Populeaza cu 8 oferte\n4. Sterge oferte\n5. Modifica oferte\n6. Cauta oferte\n7. Filtrare dupa pret\n8. Filtrare dupa destinatie\n9. Sortare dupa denumire\n10. Sortare dupa destinatie\n11. Sortare dupa pret si tip\n12. Adaugare in cos\n13. Stergere de oferte din wishlist\n14. Generare de oferte random\n15. Easter Egg\n16. Afiseaza wishlist\n17. Exporta HTML\n18. BETTER delete\n19. BETTER modify\n22. Undo\n0. Exit\nIntroduceti comanda: ";
		int cmd = 0;
		cin >> cmd;
		if (cmd == 0) {
			cout << "Bye bye!\n";
			break;
		}
		else if (cmd == 1) {
			string denum;
			string dest;
			string type;
			double price;
			cout << "Introduceti denumirea ofertei: ";
			cin >> denum;
			cout << "Introduceti destinatia ofertei: ";
			cin >> dest;
			cout << "Introduceti tipul ofertei: ";
			cin >> type;
			cout << "Introduceti pretul ofertei: ";
			cin >> price;
			try {
				serv.addServiceOffer(denum, dest, type, price);
				cout << "Oferta adaugata cu succes!\n";
			}
			catch (ValidException& msg) {
				const auto& expt = msg.get_error();
				for (const auto& ex : expt) {
					cout << ex << std::endl;
				}
				//cout << msg.getMessage() << std::endl;
			}
			catch (RepoException& msg) {
				cout << msg.getMessage() << std::endl;
			}
		}
		else if (cmd == 2) {
			const auto& offers = serv.getAllService();
			int pos = 0;
			for (const auto& ofr : offers) {
				cout << pos << ") Denumirea ofertei este : " << ofr.getDenumire() << ", destinatia este : " << ofr.getDestinatie() << ", tipul este : " << ofr.getType() << ", iar pretul este : " << ofr.getPrice() << std::endl;
				pos++;
			}
		}
		else if (cmd == 3) {
			try {
				serv.addServiceOffer("Familie", "Kiev", "Roadtrip", 69);
				serv.addServiceOffer("Familie", "Odesa", "Voiaj", 100);
				serv.addServiceOffer("Business", "Moscova", "Zbor", 129);
				serv.addServiceOffer("Honeymoon", "Petrograd", "Masina", 420);
				serv.addServiceOffer("Familie", "Kiev", "Masina", 69);
				serv.addServiceOffer("Honeymoon", "Odesa", "Voiaj", 100);
				serv.addServiceOffer("Cruise", "Moscova", "Tren", 129);
				serv.addServiceOffer("Familie", "Petrograd", "Tren", 420);
				cout << "Populat cu succes!\n";
			}
			catch (RepoException& msg) {
				cout << msg.getMessage() << '\n';
			}

		}
		else if (cmd == 4) {
			int pos;
			cout << "Introduceti pozitia elementului pe care doriti sa il stergeti: ";
			cin >> pos;
			try {
				try {
					serv.deleteServiceOffer(pos);
					cout << "Oferta " << pos << " a fost stearsa cu succes!\n";
				}
				catch (ValidException& msg) {
					const auto& expt = msg.get_error();
					for (const auto& ex : expt) {
						cout << ex << std::endl;
					}
				}
			}
			catch (RepoException& msg) {
				cout << msg.getMessage() << std::endl;
			}
		}
		else if (cmd == 5) {
			int pos;
			cout << "Introduceti pozitia elementului pe care doriti sa il modificati: ";
			cin >> pos;
			string new_denum;
			string new_dest;
			string new_type;
			double new_price;
			try {
				cout << "Introduceti noua denumire a ofertei: ";
				cin >> new_denum;
				cout << "Introduceti noua destinatie a ofertei: ";
				cin >> new_dest;
				cout << "Introduceti noul tip al ofertei: ";
				cin >> new_type;
				cout << "Introduceti noul pret al ofertei: ";
				cin >> new_price;

				serv.modifyServiceOffer(pos, new_denum, new_dest, new_type, new_price);
				cout << "Oferta " << pos << " a fost modificata cu succes!\n";
			}
			catch (ValidException& msg) {
				const auto& expt = msg.get_error();
				for (const auto& ex : expt) {
					cout << ex << std::endl;
				}
			}
			catch (RepoException& msg) {
				cout << msg.getMessage() << std::endl;
			}
		}
		else if (cmd == 6) {
			int pos;
			cout << "Introduceti pozitia elementului pe care doriti sa il cautati: ";
			cin >> pos;
			const auto& found = serv.findOfferService(pos);
			cout << "Oferta cautata este: " << pos << ") Denumirea ofertei este : " << found.getDenumire() << ", destinatia este : " << found.getDestinatie() << ", tipul este : " << found.getType() << ", iar pretul este : " << found.getPrice() << std::endl;
		}
		else if (cmd == 7) {
			int price;
			cout << "Introduceti pretul dupa care doriti sa filtrati: ";
			cin >> price;
			int pos = 0;
			const auto& filtered = serv.filtrare_pret(price);
			for (const auto& fl : filtered) {
				cout << "Oferta filtrata " << pos << " este: " << "Denumirea ofertei este : " << fl.getDenumire() << ", destinatia este : " << fl.getDestinatie() << ", tipul este : " << fl.getType() << ", iar pretul este : " << fl.getPrice() << std::endl;
				pos++;
			}
		}
		else if (cmd == 8) {
			string dest;
			cout << "Introduceti destinatia dupa care doriti sa filtrati: ";
			cin >> dest;
			int pos = 0;
			const auto& filtered = serv.filtrare_dest(dest);
			for (const auto& fl : filtered) {
				cout << "Oferta filtrata " << pos << " este: " << "Denumirea ofertei este : " << fl.getDenumire() << ", destinatia este : " << fl.getDestinatie() << ", tipul este : " << fl.getType() << ", iar pretul este : " << fl.getPrice() << std::endl;
				pos++;
			}
		}
		else if (cmd == 9) {
			int pos = 1;
			int reverse = 0;
			cout << "Introduceti directia dupa care doriti sa sortati: (0 - normal, 1 - reverse) ";
			cin >> reverse;
			const auto& sorted = serv.sortDenumire();
			for (const auto& srt : sorted) {
				if (pos != 0 && !reverse) {
					cout << pos << ") Denumirea ofertei este : " << srt.getDenumire() << ", destinatia este : " << srt.getDestinatie() << ", tipul este : " << srt.getType() << ", iar pretul este : " << srt.getPrice() << std::endl;
					pos++;
				}
				/*else if (pos != 0 && reverse) {
					std::reverse(sorted.begin(), sorted.end());
					for (const auto& rev : sorted) {
						cout << pos << ") Denumirea ofertei este : " << rev.getDenumire() << ", destinatia este : " << rev.getDestinatie() << ", tipul este : " << rev.getType() << ", iar pretul este : " << rev.getPrice() << '\n';
						pos++;
					}
					for (size_t i = sorted.size(); i > 0; i--) {
						cout << pos << ") Denumirea ofertei este : " << sorted[i].getDenumire() << ", destinatia este : " << sorted[i].getDestinatie() << ", tipul este : " << sorted[i].getType() << ", iar pretul este : " << sorted[i].getPrice() << std::endl;
						pos++;
					}
				}*/
			}
		}
		else if (cmd == 10) {
			int pos = 1;
			int reverse = 0;
			cout << "Introduceti directia dupa care doriti sa sortati: (0 - normal, 1 - reverse)";
			cin >> reverse;
			const auto& sorted = serv.sortDest();
			for (const auto& srt : sorted) {
				if (pos != 0 && !reverse) {
					cout << pos << ") Denumirea ofertei este : " << srt.getDenumire() << ", destinatia este : " << srt.getDestinatie() << ", tipul este : " << srt.getType() << ", iar pretul este : " << srt.getPrice() << std::endl;
					pos++;
				}
				/*else if (pos != 0 && reverse) {
					std::reverse(sorted.begin(), sorted.end());
					for (const auto& rev : sorted) {
						cout << pos << ") Denumirea ofertei este : " << rev.getDenumire() << ", destinatia este : " << rev.getDestinatie() << ", tipul este : " << rev.getType() << ", iar pretul este : " << rev.getPrice() << std::endl;
						pos++;
					}
				}*/
			}
		}
		else if (cmd == 11) {
			int pos = 1;
			int reverse = 0;
			cout << "Introduceti directia dupa care doriti sa sortati: (0 - normal, 1 - reverse)";
			cin >> reverse;
			const auto& sorted = serv.sortFinal();
			for (const auto& srt : sorted) {
				if (!reverse) {
					cout << pos << ") Denumirea ofertei este : " << srt.getDenumire() << ", destinatia este : " << srt.getDestinatie() << ", tipul este : " << srt.getType() << ", iar pretul este : " << srt.getPrice() << std::endl;
					pos++;
				}
				/*else if (reverse) {
					std::reverse(sorted.begin(), sorted.end());
					for (const auto& rev : sorted) {
						cout << pos << ") Denumirea ofertei este : " << rev.getDenumire() << ", destinatia este : " << rev.getDestinatie() << ", tipul este : " << rev.getType() << ", iar pretul este : " << rev.getPrice() << std::endl;
						pos++;
					}
				}*/
			}
		}
		else if (cmd == 12) {
			string dest;
			cout << "Introduceti destinatia pe care doriti sa o selectati: ";
			cin >> dest;
			try {
				serv.add_to_wishlist(dest);
			}
			catch (WishExcept& msg) {
				cout << msg.getMessage() << " ";
			}
			cout << "Exista " << serv.get_all_from_wish().size() << " oferte in cos!\n";
		}
		else if (cmd == 13) {
			serv.delete_from_wishlist();
			cout << "Ofertele au fost sterse din wishlist!\n";
			cout << "Exista " << serv.get_all_from_wish().size() << " oferte in cos!\n";
		}
		else if (cmd == 14) {
			int number;
			cout << "Introduceti numarul de oferte de generat: ";
			cin >> number;
			if (number > serv.getAllService().size())
			{
				cout << "Nu sunt destule oferte de generat!\n";
			}
			else serv.generate_random_offers(number);
			cout << "Exista " << serv.get_all_from_wish().size() << " oferte in cos!\n";
		}
		else if (cmd == 15) {
			const auto& hohols = serv.getAllService();
			serv.check_if_Kiev(hohols);
		}
		else if (cmd == 16) {
			int pos = 1;
			const auto& wishes = serv.get_all_from_wish();
			for (const auto& wish : wishes) {
				cout << pos << ") Denumirea ofertei este : " << wish.getDenumire() << ", destinatia este : " << wish.getDestinatie() << ", tipul este : " << wish.getType() << ", iar pretul este : " << wish.getPrice() << '\n';
				pos++;
			}
		}
		else if (cmd == 17) {
			string fileName;
			cout << "Introduceti numele fisierului in care doriti sa salvati (nu uitati de extensia .html): ";
			cin >> fileName;
			serv.exporta_cos_HTML(fileName);
			cout << "Exista " << serv.get_all_from_wish().size() << " oferte in cos!\n";
		}
		else if (cmd == 18) {
			string denum;
			string dest;
			string type;
			double price;
			cout << "Introduceti denumirea ofertei: ";
			cin >> denum;
			cout << "Introduceti destinatia ofertei: ";
			cin >> dest;
			cout << "Introduceti tipul ofertei: ";
			cin >> type;
			cout << "Introduceti pretul ofertei: ";
			cin >> price;
			Offer ofr{ denum, dest, type, price };
			try {
				serv.deleteServiceForUndo(ofr);
			}
			catch (RepoException& msg) {
				cout << msg.getMessage() << std::endl;
			}
		}
		else if (cmd == 19) {
			string denum;
			string dest;
			string type;
			double price;
			cout << "Introduceti denumirea ofertei: ";
			cin >> denum;
			cout << "Introduceti destinatia ofertei: ";
			cin >> dest;
			cout << "Introduceti tipul ofertei: ";
			cin >> type;
			cout << "Introduceti pretul ofertei: ";
			cin >> price;
			Offer ofr{ denum, dest, type, price };
			string new_denum;
			string new_dest;
			string new_type;
			double new_price;
			cout << "Introduceti noua denumire a ofertei: ";
			cin >> new_denum;
			cout << "Introduceti noua destinatie a ofertei: ";
			cin >> new_dest;
			cout << "Introduceti noul tip al ofertei: ";
			cin >> new_type;
			cout << "Introduceti noul pret al ofertei: ";
			cin >> new_price;
			Offer new_ofr{ new_denum, new_dest, new_type, new_price };
			try {
				serv.modifyServiceForUndo(ofr, new_ofr);
			}
			catch (RepoException& msg) {
				cout << msg.getMessage() << std::endl;
			}
		}
		else if (cmd == 22) {
			serv.Undo();
			std::cout << "Exista " << serv.getAllService().size() << " oferte\n";
		}
	}
}
