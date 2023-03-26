import random
import string

from domain.entitati import Carte, Client, IncRet
from domain.dtos import IncRetDTO, IncRetDTOs, RetIncDTOs, IncRetDTO3
from sortari.sorting import insertion_sort, comb_sort, mycmp
import functools


class ServiceCarte(object):
    def __init__(self, valid_carte, repo_carti):
        self.__valid_carte = valid_carte
        self.__repo_carti = repo_carti

    def get_nr_carti(self):
        """
        intoarce lungimea __repo_carti
        :return:
        """
        return len(self.__repo_carti)

    def adauga_carte(self, id_carte, titlu, desc, autor):
        """
        adaugam carte in service dupa ce este validata si adaugata in repo
        :param id_carte: int
        :param titlu: str
        :param desc: str
        :param autor: str
        :return:
        """
        carte = Carte(id_carte, titlu, desc, autor)
        self.__valid_carte.valideaza(carte)
        self.__repo_carti.adauga_carte_repo(carte)

    def get_all_carte(self):
        """
        getter pentru toate cartile din repo
        :return:
        """
        return self.__repo_carti.get_all_carti()

    def cauta_carte_dupa_id(self, user_input):
        """
        service cautam dupa id
        :param user_input: int
        :return:
        """
        allc = self.__repo_carti.cauta_dupa_id(user_input)
        return allc

    def cauta_carte_dupa_id_recursiv(self, user_input, n):
        """
        service pt cautarea dupa id recursiva
        :param n: int
        :param user_input: int
        :return:
        """
        allc = self.__repo_carti.cauta_dupa_id_recursiv(user_input, n)
        return allc

    def stergere_carti(self, user_input):
        """
        service stergere carti
        :return:
        """
        return self.__repo_carti.sterge_carte(user_input)

    def modifica_carte(self, option1, option2):
        """
        service modificare carte
        :param option2: str
        :param option1: int
        :return:
        """
        allcl = self.__repo_carti.modificare_carte(option1, option2)
        return allcl

    def stergere_carti_recursiv(self, user_input, i):
       return self.__repo_carti.sterge_carte_recursiv(user_input, i)

    def sortare_carti_insertion(self, user_input):
        """
        metoda care sorteaza cartile utilizand Insertion Sort
        :return:
        """
        allcl = self.__repo_carti.get_all_carti()
        insertion_sort(allcl, key=lambda _carte: _carte.get_id_carte(), reverse=False, cmp=lambda a, b, r=False: a < b if r is False else a > b)
        if user_input == "id":
            for _carte in allcl:
                print(_carte.get_id_carte())
        elif user_input == "desc":
            for _carte in allcl:
                print(_carte.get_desc())
        elif user_input == "autor":
            for _carte in allcl:
                print(_carte.get_autor())
        elif user_input == "titlu":
            for _carte in allcl:
                print(_carte.get_titlu())
        elif user_input == "all":
            for _carte in allcl:
                print(_carte)

    def sortare_carti_comb(self, user_input):
        """
        metoda care sorteaza cartile utilizand Comb Sort
        :return:
        """
        allcl = self.__repo_carti.get_all_carti()
        comb_sort(allcl, key=lambda _carte: _carte.get_id_carte(), reverse=True, cmp=lambda a, b, r=False: a < b if r is False else a > b)
        if user_input == "id":
            for _carte in allcl:
                print(_carte.get_id_carte())
        elif user_input == "desc":
            for _carte in allcl:
                print(_carte.get_desc())
        elif user_input == "autor":
            for _carte in allcl:
                print(_carte.get_autor())
        elif user_input == "titlu":
            for _carte in allcl:
                print(_carte.get_titlu())
        elif user_input == "all":
            for _carte in allcl:
                print(_carte)

    def cmp_alt(self):
        allcl = self.__repo_carti.get_all_carti()
        for index, _carte in enumerate(allcl):
            if _carte.get_id_carte()[index] < _carte.get_id_carte()[index+1]:
                return 1

    def sortare_comb_alt(self):
        def cmp_alt(carte1,carte2):
            if carte1.get_desc() < carte2.get_desc():
                return 1
            elif carte1.get_desc() == carte2.get_desc():
                if carte1.get_autor() < carte2.get_autor():
                    return 1
                else:
                    return 0
            else:
                return 0

        allcl = self.__repo_carti.get_all_carti()
        comb_sort(allcl, key=lambda carte: carte, cmp= cmp_alt, reverse=False)
        for _carte in allcl:
            print(_carte)


class ServiceClient(object):
    def __init__(self, valid_client, repo_clienti):
        self.__valid_client = valid_client
        self.__repo_clienti = repo_clienti

    def get_nr_clienti(self):
        """
        intoarce numarul de clienti din __repo_clienti
        :return:
        """
        return len(self.__repo_clienti)

    def adauga_client(self, id_client, nume, cnp):
        """
        adaugam client in service dupa ce este validat si adaugat in repo
        :param id_client: int
        :param nume: str
        :param cnp: int
        :return:
        """
        client = Client(id_client, nume, cnp)
        self.__valid_client.valideaza(client)
        self.__repo_clienti.adauga_client_repo(client)

    def get_all_clienti(self):
        """
        getter pentru toti clientii
        :return:
        """
        return self.__repo_clienti.get_all_clients()

    def cauta_clienti_dupa_id(self, user_input):
        """
        service cauta dupa id
        :param user_input: int
        :return:
        """
        allc = self.__repo_clienti.cauta_dupa_id_client(user_input)
        return allc

    def sterge_clienti(self, user_input):
        """
        service stergere
        :return:
        """
        return self.__repo_clienti.stergere_clienti(user_input)

    def modifica_client(self, option1, option2):
        """
        service modificare
        :param option2: str
        :param option1: int
        :return:
        """
        allcl = self.__repo_clienti.modificare_client(option1, option2)
        return allcl

    def generare_aleator_string(self, lungime):
        """
        functie care genereaza string-uri random pentru numele unui client
        :param lungime: int
        :return:
        """
        chars = string.ascii_uppercase
        return ''.join(random.choice(chars) for _ in range(lungime))

    def generare_aleator_int(self, lungime):
        """
        functie care genereaza int-uri random pentru ID si CNP
        metoda pentru CNP, intrucat furnizeaza numere foarte mari
        :param lungime:
        :return:
        """
        intg = string.digits
        return ''.join(random.choice(intg) for _ in range(lungime))

    def generare_aleator_id(self):
        """
        functie care genereaza un id aleator
        metoda pentru ID, intrucat furnizeaza numere mai mici
        :return:
        """
        id_client = random.randint(1, 1000)
        return id_client

    def generare_clienti_random(self, user_input):
        """
        functie care genereaza clienti random
        :return:
        """
        for _ in range(user_input):
            _client = Client(int(self.generare_aleator_id()),
                             self.generare_aleator_string(random.randrange(3, 12)),
                             int(self.generare_aleator_int(random.randrange(14, 15))))
            self.__valid_client.valideaza(_client)
            self.__repo_clienti.adauga_client_repo(_client)


class ServiceIncRet(object):
    def __init__(self, valid_inc_ret, repo_inc_ret, repo_carti, repo_clienti):
        self.__valid_inc_ret = valid_inc_ret
        self.__repo_inc_ret = repo_inc_ret
        self.__repo_carti = repo_carti
        self.__repo_clienti = repo_clienti

    def get_all_inc_ret(self):
        """
        functie care returneaza toate inchirieri_returnari
        :return:
        """
        return self.__repo_inc_ret.get_all_inc_ret_repo()

    def get_nr_inc_ret(self):
        """
        functie care returneaza numarul de inchirieri_returnari
        :return:
        """
        return len(self.__repo_inc_ret)

    def get_all_inc_ret_carti_inchirieri(self):
        """
        metoda care returneaza toate inchirierile cartilor cu ajutorul DTO-urilor
        :return:
        """
        inc_ret_dtos = self.__repo_inc_ret.get_all_inc_ret_repo()
        ret_inc = {}
        for inc_ret_dto in inc_ret_dtos:
            carte = self.__repo_carti.cauta_dupa_id(inc_ret_dto.get_id_carte())
            client = self.__repo_clienti.cauta_dupa_id_client(inc_ret_dto.get_id_client())
            inc_ret_dto.set_carte(carte)
            inc_ret_dto.set_client(client)
            if carte.get_id_carte() not in ret_inc:
                ret_inc[carte.get_id_carte()] = []
            ret_inc[carte.get_id_carte()].append(inc_ret_dto)
        rezultat = []
        sortedret_inc = sorted(ret_inc.items(), key=lambda item: inc_ret_dto.get_nr_inchirieri(),
                               reverse=True)  # cheile dictionarului sortate dupa nr de inchirieri
        # sortedret_inc_max = max(sortedret_inc, key=lambda  item:inc_ret_dto.get_nr_inchirieri())
        # print(sortedret_inc_max)
        nr_inc = next(iter(sortedret_inc))  # primul element din dictionar
        for _carte in sortedret_inc:
            # if _carte == nr_inc:
            id_carte = _carte[0]
            carte_cox = self.__repo_inc_ret.cauta_dupa_id_carte(id_carte)
            carti = _carte[1]
            incretdto = IncRetDTOs(carte_cox.get_carte().get_titlu(), carti)
            rezultat.append(incretdto)
        return rezultat

    def get_all_inc_ret_clienti_inchirieri(self):
        """
        metoda care returneaza clientii cu cele mai multe inchirieri cu ajutorul DTO-urilor
        :return:
        """
        inc_ret_dtos = self.__repo_inc_ret.get_all_inc_ret_repo()
        ret_inc = {}
        for inc_ret_dto in inc_ret_dtos:
            carte = self.__repo_carti.cauta_dupa_id(inc_ret_dto.get_id_carte())
            client = self.__repo_clienti.cauta_dupa_id_client(inc_ret_dto.get_id_client())
            inc_ret_dto.set_carte(carte)
            inc_ret_dto.set_client(client)
            if client.get_id_client() not in ret_inc:
                ret_inc[client.get_id_client()] = []
            ret_inc[client.get_id_client()].append(inc_ret_dto)
        rezultat = []
        sortedret_inc = sorted(ret_inc.items(), key=lambda item: inc_ret_dto.get_nr_inchirieri(),
                               reverse=True)  # cheile dictionarului sortate dupa nr de inchirieri
        # nr_inc = next(iter(sortedret_inc))  # primul element din dictionar
        for _client in sortedret_inc:
            # if _carte == nr_inc:
            id_client = _client[0]
            client_cox = self.__repo_inc_ret.cauta_dupa_id_client(id_client)
            clienti = _client[1]
            incretdto = RetIncDTOs(client_cox.get_client().get_nume(), clienti)
            rezultat.append(incretdto)
        return rezultat

    def get_top_20_clienti(self):
        """
        metoda care returneaza top 20% clienti
        :return:
        """
        inc_ret_dtos_clt = self.__repo_inc_ret.get_all_inc_ret_repo()
        ret_inc = {}
        for inc_ret_dto in inc_ret_dtos_clt:
            carte = self.__repo_carti.cauta_dupa_id(inc_ret_dto.get_id_carte())
            client = self.__repo_clienti.cauta_dupa_id_client(inc_ret_dto.get_id_client())
            inc_ret_dto.set_carte(carte)
            inc_ret_dto.set_client(client)
            if client.get_id_client() not in ret_inc:
                ret_inc[client.get_id_client()] = []
            ret_inc[client.get_id_client()].append(inc_ret_dto)
        sortedclt = sorted(ret_inc.items(), key=lambda item: inc_ret_dto.get_nr_inchirieri(), reverse=True)
        sorted_top = []
        for _clt in sortedclt:
            id_client = _clt[0]
            ct = self.__repo_clienti.cauta_dupa_id_client(id_client)
            clienti = _clt[1]
            incretclientidto = RetIncDTOs(ct.get_nume(), clienti)
            sorted_top.append(incretclientidto)
        return sorted_top

    def get_trei_autori(self):
        """
        metoda care returneaza primii 3 autori inchiriati cu inchirierile lor
        :return:
        """
        inc_ret_dtos = self.__repo_inc_ret.get_all_inc_ret_repo()
        ret_inc = {}
        for inc_ret_dto in inc_ret_dtos:
            carte = self.__repo_carti.cauta_dupa_id(inc_ret_dto.get_id_carte())
            client = self.__repo_clienti.cauta_dupa_id_client(inc_ret_dto.get_id_client())
            inc_ret_dto.set_carte(carte)
            inc_ret_dto.set_client(client)
            if carte.get_id_carte() not in ret_inc:
                ret_inc[carte.get_id_carte()] = []
            ret_inc[carte.get_id_carte()].append(inc_ret_dto)
        rezultat = []
        sortedret_inc = sorted(ret_inc.items(), key=lambda item: inc_ret_dto.get_nr_inchirieri(),
                               reverse=True)  # cheile dictionarului sortate dupa nr de inchirieri
        nr_inc = next(iter(sortedret_inc))  # primul element din dictionar
        for _carte in sortedret_inc:
            # if _carte == nr_inc:
            id_carte = _carte[0]
            carte_cox = self.__repo_inc_ret.cauta_dupa_id_carte(id_carte)
            carti = _carte[1]
            incretdto = IncRetDTO3(carte_cox.get_carte().get_autor(), carti)
            rezultat.append(incretdto)
        lista_aut = rezultat[0:3]
        return lista_aut

    def adauga_inc_ret(self, id_inc_ret, id_carte, id_client, durata):
        """
        functie service care adauga in lista o inchiriere_returnare dupa ce este validata
        :param id_inc_ret: int
        :param id_carte: int
        :param id_client: int
        :param durata: int
        :return:
        """
        carte = self.__repo_carti.cauta_dupa_id(id_carte)
        client = self.__repo_clienti.cauta_dupa_id_client(id_client)
        inc_ret_dto = IncRetDTO(id_inc_ret, id_carte, id_client, durata)
        inc_ret_dto.set_carte(carte)
        inc_ret_dto.set_client(client)
        allic = self.__repo_inc_ret.get_all_inc_ret_repo()
        for carte_n in allic:
            if carte.get_id_carte() == carte_n.get_id_carte():
                carte_n.add_inchirieri()
        for client_n in allic:
            if client.get_id_client() == client_n.get_id_client():
                client_n.add_inchirieri_client()
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        # self.__valid_inc_ret.valideaza(inc_ret)
        self.__valid_inc_ret.valideaza_dto(inc_ret_dto)
        self.__repo_inc_ret.adauga_inc_ret_repo(inc_ret_dto)

    def add_inc_ret_recursiv_service(self, id_inc_ret, id_carte, id_client, durata, n):
        carte = self.__repo_carti.cauta_dupa_id(id_carte)
        client = self.__repo_clienti.cauta_dupa_id_client(id_client)
        inc_ret_dto = IncRetDTO(id_inc_ret, id_carte, id_client, durata)
        inc_ret_dto.set_carte(carte)
        inc_ret_dto.set_client(client)
        allic = self.__repo_inc_ret.get_all_inc_ret_repo()
        for carte_n in allic:
            if carte.get_id_carte() == carte_n.get_id_carte():
                carte_n.add_inchirieri()
        for client_n in allic:
            if client.get_id_client() == client_n.get_id_client():
                client_n.add_inchirieri_client()
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        # self.__valid_inc_ret.valideaza(inc_ret)
        self.__valid_inc_ret.valideaza_dto(inc_ret_dto)
        self.__repo_inc_ret.add_inc_ret_recursiv(inc_ret_dto, n)

    def sterge_inc_ret(self, user_input):
        """
        sterge din lista self.__inc_ret toate inchirierile_returnarile cu un id_carte sau id_client dat
        :return:
        """
        return self.__repo_inc_ret.sterge_inc_ret_dupa_id(user_input), self.__repo_carti.sterge_carte(
            user_input), self.__repo_clienti.stergere_clienti(user_input)

    def modifica_inc_ret(self, option1, option2):
        """
        service modificare pentru inchiriere_returnare
        :param option2: int
        :param option1: int
        :return:
        """
        allir = self.__repo_inc_ret.modificare_inc_ret(option1, option2)
        return allir
