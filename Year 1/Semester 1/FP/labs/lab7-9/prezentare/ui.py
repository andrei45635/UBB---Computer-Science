from erori.exceptii import ValidationError, RepositoryError


class Consola(object):

    def __init__(self, srv_carte, srv_client, srv_inc_ret):
        self.__srv_carte = srv_carte
        self.__srv_client = srv_client
        self.__srv_inc_ret = srv_inc_ret

    def __ui_adauga_carte(self):
        try:
            id_carte = int(input("Introduceti ID-ul: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        titlu = input("Introduceti titlul: ")
        desc = input("Introduceti descrierea: ")
        autor = input("Introduceti autorul: ")
        self.__srv_carte.adauga_carte(id_carte, titlu, desc, autor)
        print("carte adaugata cu succes!")

    def __ui_cauta_carti_id(self):
        try:
            user_input = int(input("Introduceti ID-ul pe care doriti sa il cautati: "))
        except ValueError:
            print("valoare numerica invalida!")
            return

        try:
            print(self.__srv_carte.cauta_carte_dupa_id(user_input))
        except RepositoryError as re:
            print("repository error: " + str(re))

    def __ui_stergere_carti(self):
        if self.__srv_carte.get_nr_carti() == 0:
            print("Nu exista carti!")
        else:
            try:
                user_input = int(input("Introduceti id-ul pe care vreti sa il stergeti: "))
            except ValueError:
                print("valoare numerica invalida!")
                return
            self.__srv_carte.stergere_carti(user_input)

    def __ui_print_carti(self):
        carti = self.__srv_carte.get_all_carte()
        if len(carti) == 0:
            print("Nu exista carti!")
        else:
            for _carti in carti:
                print(_carti)

    def __ui_adauga_client(self):
        try:
            id_client = int(input("Introduceti ID-ul clientului: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        nume = input("Introduceti numele clientului: ")
        try:
            cnp = int(input("Introduceti CNP-ul clientului: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        self.__srv_client.adauga_client(id_client, nume, cnp)
        print("client adaugat cu succes!")

    def __ui_cauta_clienti_dupa_id(self):
        try:
            user_input = int(input("Introduceti ID-ul pe care doriti sa il cautati: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        try:
            print(self.__srv_client.cauta_clienti_dupa_id(user_input))
        except RepositoryError as re:
            print("Repository error: " + str(re))

    def __ui_stergere_clienti(self):
        if self.__srv_client.get_nr_clienti() == 0:
            print("Nu exista clienti!")
        else:
            try:
                user_input = int(input("Introduceti ID-ul pe care doriti sa il stergeti: "))
            except ValueError:
                print("valoare numerica invalida!")
                return
            self.__srv_client.sterge_clienti(user_input)

    def __ui_print_clienti(self):
        clienti = self.__srv_client.get_all_clienti()
        if len(clienti) == 0:
            print("Nu exista clienti!")
        else:
            for _clienti in clienti:
                print(_clienti)

    def __ui_modificare_carte(self):
        try:
            option1 = int(input("Ce carte ati dori sa modificati: "))
        except ValueError:
            print("valoare numerica invalida")
            return
        option2 = input("Descriere noua: ")
        self.__srv_carte.modifica_carte(option1, option2)

    def __ui_modificare_client(self):
        try:
            option1 = int(input("Ce client ati dori sa modificati: "))
        except ValueError:
            print("valoare numerica invalida")
            return
        try:
            option2 = input("Nume nou: ")
        except ValueError:
            print("valoare numerica invalida")
            return
        self.__srv_client.modifica_client(option1, option2)

    def __ui_inc_ret(self):
        try:
            id_inc_ret = int(input("Introduceti ID-ul inchirierii: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        try:
            id_carte = int(input("Introduceti ID-ul cartii: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        try:
            id_client = int(input("Introduceti ID-ul clientului: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        try:
            durata = int(input("Introduceti durata: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        self.__srv_inc_ret.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)

    """
    def __ui_print_inc_ret(self):
        inc_ret = self.__srv_inc_ret.get_all_inc_ret()
        if len(inc_ret) == 0:
            print("Nu exista inchirieri_returnari!")
        else:
            for _inc_ret in inc_ret:
                print(_inc_ret)
    """

    def __ui_print_inc_ret(self):
        inc_ret = self.__srv_inc_ret.get_all_inc_ret()
        for _inc_ret in inc_ret:
            print(_inc_ret)

    def __ui_sterge_ir(self):
        if self.__srv_inc_ret.get_all_inc_ret() == 0:
            print("Nu exista inchirieri_returnari!")
        else:
            try:
                user_input = int(input("Introduceti ID-ul pe care doriti sa il stergeti: "))
            except ValueError:
                print("valoare numerica invalida!")
                return
            self.__srv_inc_ret.sterge_inc_ret(user_input)

    def __ui_generare_random(self):
        try:
            user_input = int(input("Introduceti numarul de entitati clienti pe care doriti sa le creati: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        try:
            self.__srv_client.generare_clienti_random(user_input)
        except RepositoryError as re:
            print("Repository error: " + str(re))

    def __ui_modificare_inc_ret(self):
        try:
            option1 = int(input("Ce inchiriere_returnare ati dori sa modificati: "))
        except ValueError:
            print("valoare numerica invalida")
            return
        try:
            option2 = input("Durata noua: ")
        except ValueError:
            print("valoare numerica invalida")
            return
        self.__srv_inc_ret.modifica_inc_ret(option1, option2)

    def __ui_print_cele_mai_inchiriate_carti(self):
        l = self.__srv_inc_ret.get_all_inc_ret_carti_inchirieri()
        for _carte in l:
            print(_carte)

    def __ui_print_clienti_inchirieri_carti(self):
        l = self.__srv_inc_ret.get_all_inc_ret_clienti_inchirieri()
        for _client in l:
            print(_client)

    def __ui_print_top_clienti(self):
        l = self.__srv_inc_ret.get_top_20_clienti()
        for _clt in l:
            print(_clt)

    def __ui_print_top_autori(self):
        l = self.__srv_inc_ret.get_trei_autori()
        for _aut in l:
            print(_aut)

    def __ui_print_cauta_id_carte_recursiv(self):
        try:
            user_input = int(input("Introduceti ID-ul pe care doriti sa il cautati: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        """
        try:
            n = int(input("introduceti numarul de cautari pe care doriti sa il faceti: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        """
        self.__srv_carte.get_nr_carti()
        try:
            print(self.__srv_carte.cauta_carte_dupa_id_recursiv(user_input, 0))
        except RepositoryError as re:
            print("repository error: " + str(re))

    def __ui_inc_ret_recursiv(self):
        try:
            id_inc_ret = int(input("Introduceti ID-ul inchirierii: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        try:
            id_carte = int(input("Introduceti ID-ul cartii: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        try:
            id_client = int(input("Introduceti ID-ul clientului: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        try:
            durata = int(input("Introduceti durata: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        """
        try:
            n = int(input("introduceti numarul de cautari pe care doriti sa il faceti: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        """
        self.__srv_inc_ret.get_all_inc_ret()
        self.__srv_inc_ret.add_inc_ret_recursiv_service(id_inc_ret, id_carte, id_client, durata, 0)

    def __ui_sorting_carti_insertion(self):
        user_input = input("Introduceti cheia dupa care doriti sa cautati: ")
        self.__srv_carte.sortare_carti_insertion(user_input)

    def __ui_sortare_carti_comb(self):
        user_input = input("Introduceti cheia dupa care doriti sa cautati: ")
        self.__srv_carte.sortare_carti_comb(user_input)

    def __ui_sterge_carte_recursiv(self):
        try:
            user_input = int(input("Introduceti ID-ul cartii pe care doriti sa o stergeti"))
        except ValueError:
            print('valoare numerica gresita!')
            return
        self.__srv_carte.stergere_carti_recursiv(user_input, 0)

    def __ui_alt_sort(self):
        self.__srv_carte.sortare_comb_alt()

    def __ui_afiseaza_meniu(self):
        print("--------------------------- APLICATIE PENTRU BIBLIOTECA ---------------------------\n")
        print("1. add_carte = adauga carte in lista")
        print("2. add_client = adauga client in lista")
        print("3. print_carti = tipareste lista de carti")
        print("4. print_clienti = tipareste lista de clienti")
        print("5. inchiriere_returnare = asigneaza unui client o carte")
        print("6. stergere_carti = sterge carti din lista dupa ID")
        print("7. stergere_clienti = sterge clienti din lista dupa ID")
        print("8. stergere_ir = sterge inchirieri/returnari din lista inc_ret si din clienti si carti daca e nevoie")
        print("9. print_ir = printeaza lista de inchirieri")
        print("10. cauta_clienti_id = afiseaza clientul cautat dupa ID")
        print("11. cauta_carti_id = afiseaza cartea cautata dupa ID")
        print("12. modificare_carte = modifica o carte")
        print("13. modificare_client = modifica un client")
        print("14. generate = genereaza un nr dat de user de clienti")
        print("15. mod_inc_ret = modificarea inchirierii/returnarii")
        print("16. meniu = afiseaza meniul")
        print("17. exit = iesire din program")
        print("18. raport1")
        print("19. raport2")
        print("20. raport3")
        print("21. top 3 autori")
        print("22. cautare dupa id recursiva")
        print("23. adaugare recursiva\n")

    def run(self):
        while True:
            cmd = int(input(">>>"))
            if cmd == 17:
                return
            if cmd == " ":
                continue
            elif cmd == 1:
                try:
                    self.__ui_adauga_carte()
                except ValidationError as ve:
                    print("validation error: " + str(ve))
                except RepositoryError as re:
                    print("repository error: " + str(re))
            elif cmd == 3:
                self.__ui_print_carti()
            elif cmd == 2:
                try:
                    self.__ui_adauga_client()
                except ValidationError as ve:
                    print("validation error: " + str(ve))
                except RepositoryError as re:
                    print("repository error: " + str(re))
            elif cmd == 10:
                self.__ui_cauta_clienti_dupa_id()
            elif cmd == 4:
                self.__ui_print_clienti()
            elif cmd == 11:
                self.__ui_cauta_carti_id()
            elif cmd == 7:
                self.__ui_stergere_clienti()
            elif cmd == 6:
                self.__ui_stergere_carti()
            elif cmd == 12:
                self.__ui_modificare_carte()
            elif cmd == 13:
                self.__ui_modificare_client()
            elif cmd == 5:
                self.__ui_inc_ret()
            elif cmd == 9:
                self.__ui_print_inc_ret()
            elif cmd == 8:
                self.__ui_sterge_ir()
            elif cmd == 14:
                self.__ui_generare_random()
            elif cmd == 16:
                self.__ui_afiseaza_meniu()
            elif cmd == 15:
                self.__ui_modificare_inc_ret()
            elif cmd == 18:
                self.__ui_print_cele_mai_inchiriate_carti()
            elif cmd == 19:
                self.__ui_print_clienti_inchirieri_carti()
            elif cmd == 20:
                self.__ui_print_top_clienti()
            elif cmd == 21:
                self.__ui_print_top_autori()
            elif cmd ==22:
                self.__ui_print_cauta_id_carte_recursiv()
            elif cmd == 23:
                self.__ui_sterge_carte_recursiv()
            elif cmd == 24:
                self.__ui_sorting_carti_insertion()
            elif cmd == 25:
                self.__ui_sortare_carti_comb()
            elif cmd == 26:
                self.__ui_alt_sort()
            else:
                print("comanda invalida!")
