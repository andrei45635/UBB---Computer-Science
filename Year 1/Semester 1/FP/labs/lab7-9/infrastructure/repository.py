from domain.entitati import Carte, Client, IncRet
from erori.exceptii import RepositoryError


class RepoCarti(object):
    def __init__(self):
        self._carte = []

    def __len__(self):
        return len(self._carte)

    def adauga_carte_repo(self, carte):
        """
        adauga obiectul de tip carte in repo
        daca doua carti au acelasi id, atunci se arunca eroarea "id existent!\n"
        :param carte: obiect
        :return:
        """
        for _carte in self._carte:
            if _carte == carte:
                raise RepositoryError("id existent!\n")
        self._carte.append(carte)

    def cauta_dupa_id(self, id_carte):
        """
        cautam o carte dupa id
        daca se gaseste, atunci o afisam
        altfel, daca nu gasim id-ul, se arunca eroarea "id inexistent!\n"
        :param id_carte: int
        :return:

        Complexitatea functiei este O(n)
        Caz favorabili primul element este cel cautat, se executa un singur pas, T(n) = 1 ce gpartine de 0(1)
        Caz defadvorabil: nu exista filmul cautat in lista, se executa n pasi, T(n) = n ce apartine de O(n)
        Caz mediu: for poate fi executat de 1,2,3,...,n ori(aceeasi probabilitate), deci T(n) = (n+1)/2 ce apartine de O(n)
        """
        ok = True
        for _carte in self._carte:
            if _carte.get_id_carte() == id_carte:
                return _carte
        if ok:
            raise RepositoryError("id inexistent!")

    def cauta_dupa_id_recursiv(self, id_carte, n):
        """
        metoda care cauta dupa id in mod recursiv
        id_carte = int
        n = int
        input = id-ul cartii cautate
        output = cartea cautata
        :return:
        """
        if n >= len(self._carte):
            raise RepositoryError("id inexistent!")
        if self._carte[n].get_id_carte() == id_carte:
            return self._carte[n]
        else:
            return self.cauta_dupa_id_recursiv(id_carte, n+1)

    def get_all_carti(self):
        """
        getter pentru toate cartile din repo
        :return:
        """
        return self._carte[:]

    def sterge_carte(self, user_input):
        """
        stergem cartile din  dupa id-ul dat de user_input
        :user_input: int
        :return:
        """
        allcr = self._carte
        allcr[:] = [_carte for _carte in allcr if not _carte.get_id_carte() == user_input]
        return allcr

    def sterge_carte_recursiv(self, user_input, i=0):
        """
        metoda care sterge o carte recursiv
        :param user_input: int, id
        :return:
        """
        if i>=len(self._carte):
            raise RepositoryError("id inexistent!\n")
        if self._carte[i].get_id_carte() == user_input:
            del self._carte[i]
            return
        return self.sterge_carte_recursiv(user_input, i+1)


    def modificare_carte(self, option1, option2):
        """
        modificam o anumita carte din repo, conform option1, care este input de la user
        option1 reprezinta cartea din lista pe care o vom updata
        :param option2: str
        :param option1: int
        :return:
        """
        allcr = self._carte
        for _carte in allcr:
            if _carte.get_id_carte() == option1:
                _carte.set_desc(option2)
        return allcr


class FileRepoCarti(RepoCarti):
    def __init__(self, filePath):
        """
        suprascriem functia __init__ din RepoCarti
        :param filePath: path-ul relativ al fisierului
        """
        RepoCarti.__init__(self)
        self.__filePath = filePath

    def __read_all_from_file(self):
        """
        citim toate elementele din fisier
        :return:
        """
        self._carte = []
        with open(self.__filePath, "r") as f:
            lines = f.readlines()
            contor_linii = 1
            for line in lines:
                line.strip()  # curat linia, elimin spatiile
                if len(line) > 0:
                    if contor_linii % 4 == 1:
                        id_carte = int(line)
                    elif contor_linii % 4 == 2:
                        titlu = str(line)
                        desc = str(line)
                    elif contor_linii % 4 == 3:
                        desc = str(line)
                    elif contor_linii % 4 == 0:
                        autor = str(line)
                        carte = Carte(id_carte, titlu, desc, autor)
                        self._carte.append(carte)
                contor_linii += 1

    def __append_to_file(self, carte):
        """
        adaugam in fisier o carte
        :param carte: obiect de tip carte
        :return:
        """
        with open(self.__filePath, "a") as f:
            f.write(
                str(carte.get_id_carte()) + "\n" + carte.get_titlu() + "\n" + carte.get_desc() + "\n" + carte.get_autor() + "\n")

    def adauga_carte_repo(self, carte):
        """
        adaugam in fisier o carte
        :param carte: obiect de tip carte
        :return:
        """
        self.__read_all_from_file()
        RepoCarti.adauga_carte_repo(self, carte)
        self.__append_to_file(carte)

    def cauta_dupa_id(self, id_carte):
        """
        cautam dupa id in fisier o carte si o returnam
        :param id_carte: int
        :return:
        """
        self.__read_all_from_file()
        try:
            return RepoCarti.cauta_dupa_id(self, id_carte)
        except RepositoryError as re:
            raise RepositoryError("id inexistent!\n")

    def cauta_dupa_id_recursiv(self, id_carte, n):
        """
        metoda care cauta recursiv dupa id
        :param id_carte: int
        :param n: int
        :return:
        """
        self.__read_all_from_file()
        try:
            return RepoCarti.cauta_dupa_id_recursiv(self, id_carte, n)
        except RepositoryError as re:
            raise RepositoryError("id inexistent\n")

    def sterge_carte_recursiv(self, user_input, i=0):
        self.__read_all_from_file()
        try:
            RepoCarti.sterge_carte_recursiv(self,user_input,i)
        except RepositoryError as re:
            raise RepositoryError("id inexistent\n")
        self.write_all_to_file()

    def get_all_carti(self):
        """
        returneaza toate cartile din fisier
        :return:
        """
        self.__read_all_from_file()
        return RepoCarti.get_all_carti(self)

    def __len__(self):
        """
        suprascrie metoda __len__ din RepoCarti
        :return:
        """
        self.__read_all_from_file()
        return RepoCarti.__len__(self)

    def write_all_to_file(self):
        with open(self.__filePath, "w") as f:
            for crt in self._carte:
                f.write(str(crt.get_id_carte()) + "\n" + crt.get_titlu() + "\n" + crt.get_desc() + "\n" + crt.get_autor() + "\n" + "\n")

    def modificare_carte(self, option1, option2):
        self.__read_all_from_file()
        RepoCarti.modificare_carte(self, option1, option2)
        self.write_all_to_file()

    def sterge_carte(self, user_input):
        self.__read_all_from_file()
        RepoCarti.sterge_carte(self, user_input)
        self.write_all_to_file()


class RepoClienti(object):
    def __init__(self):
        self._client = []

    def __len__(self):
        return len(self._client)

    def adauga_client_repo(self, client):
        """
        adaugam obiectul client in repo
        daca cnp-ul si id-ul exista deja, atunci se vor arunca erorile "cnp existent!\n" si "id existent!\n"
        :param client: obiect
        :return:
        """
        for _client in self._client:
            if _client.get_cnp() == client.get_cnp() and _client.get_id_client() == client.get_id_client():
                raise RepositoryError("cnp existent!\nid existent!\n")
            if _client.get_id_client() == client.get_id_client():
                # print("Repo Error: ID existent!\n")
                raise RepositoryError("id existent!\n")
            if _client.get_cnp() == client.get_cnp():
                raise RepositoryError("cnp existent!\n")
        self._client.append(client)

    def get_all_clients(self):
        """
        getter pentru toti clientii din repo clienti
        :return:
        """
        return self._client[:]

    def cauta_dupa_id_client(self, id_client):
        """
        cautam clientii dupa id
        daca getter-ul id-ului clientului este egal cu id_client pe care il cautam, atunci se va afisa clientul
        altfel, daca nu exista id-ul, se va arunca eroarea "id inexistent!\n"
        :param id_client: int
        :return:
        """
        ok = True
        for _clients in self._client:
            if _clients.get_id_client() == id_client:
                return _clients
        if ok:
            raise RepositoryError("id inexistent!\n")

    def stergere_clienti(self, user_input):
        """
        stergem clientii din lista repo dupa user_input
        :return:
        """
        allcl = self._client
        allcl[:] = [_client for _client in allcl if not _client.get_id_client() == user_input]
        return allcl

    def modificare_client(self, option1, option2):
        """
        modificam clientii din lista in functie de input-ul de la user : option1
        option1 reprezinta clientul din lista pe care urmeaza sa il updatam
        :param option2: str
        :param option1: int
        :return:
        """
        allcl = self._client
        ok = False
        for _client in allcl:
            if _client.get_id_client() == option1:
                ok = True
                _client.set_nume(option2)
        if ok:
            return allcl
        else:
            raise RepositoryError("inexistent!\n")


class FileRepoClienti(RepoClienti):
    def __init__(self, filePath):
        RepoClienti.__init__(self)
        self.__filePath = filePath

    def __read_all_from_file(self):
        self._client = []
        with open(self.__filePath, "r") as f:
            lines = f.readlines()
            contor_linii = 1
            for line in lines:
                line.strip()  # curat linia, elimin spatiile
                if len(line) > 0:
                    if contor_linii % 3 == 1:
                        id_client = int(line)
                    elif contor_linii % 3 == 2:
                        nume = str(line)
                    elif contor_linii % 3 == 0:
                        cnp = int(line)
                        client = Client(id_client, nume, cnp)
                        self._client.append(client)
                contor_linii += 1

    def __append_to_file(self, client):
        """
        adaugam in fisier un client
        :param client: obiect de tip client
        :return:
        """
        with open(self.__filePath, "a") as f:
            f.write(str(client.get_id_client()) + "\n" + client.get_nume() + "\n" + str(client.get_cnp()) + "\n")

    def adauga_client_repo(self, client):
        """
        adaugam in fisier un client
        :param client: obiect de tip client
        :return:
        """
        self.__read_all_from_file()
        RepoClienti.adauga_client_repo(self, client)
        self.__append_to_file(client)

    def cauta_dupa_id_client(self, id_client):
        """
        cautam in fisier dupa id un client
        :param id_client: int
        :return:
        """
        self.__read_all_from_file()
        return RepoClienti.cauta_dupa_id_client(self, id_client)

    def get_all_clients(self):
        """
        getter pentru toti clientii
        :return:
        """
        self.__read_all_from_file()
        return RepoClienti.get_all_clients(self)

    def __len__(self):
        """
        suprascriem len-ul
        :return:
        """
        self.__read_all_from_file()
        return RepoClienti.__len__(self)

    def write_all_to_file(self):
        with open(self.__filePath, "w") as f:
            for cl in self._client:
                f.write(str(cl.get_id_client()) + "\n" + cl.get_nume() + "\n" + str(cl.get_cnp()) + "\n")

    def modificare_client(self, option1, option2):
        self.__read_all_from_file()
        RepoClienti.modificare_client(self, option1, option2)
        self.write_all_to_file()

    def stergere_clienti(self, user_input):
        self.__read_all_from_file()
        RepoClienti.stergere_clienti(self, user_input)
        self.write_all_to_file()


class RepoIncRet(object):
    def __init__(self):
        self.__inc_ret = []

    def __len__(self):
        return len(self.__inc_ret)

    def adauga_inc_ret_repo(self, inc_ret):
        """
        adaugam inchiriere_returnare in lista
        daca exista deja un id_inc_ret atunci se va arunca eroarea "id inchiriere_returnare existent!\n"
        :param inc_ret: int
        :return:
        """
        for _inc_ret in self.__inc_ret:
            if _inc_ret == inc_ret:
                raise RepositoryError("id inchiriere_returnare existent!\n")
        self.__inc_ret.append(inc_ret)

    def add_inc_ret_recursiv(self, inc_ret, n):
        """
        metoda care adauga o inchiere_returnare in lista recursiv
        daca exista deja un id_inc_ret atunci se va arunca eroarea "id inchiriere_returnare existent!\n"
        :param inc_ret: int
        :return:
        """
        if n >= len(self.__inc_ret):
            self.__inc_ret.append(inc_ret)
        elif self.__inc_ret[n] == inc_ret:
            raise RepositoryError("id inchiriere_returnare existent!\n")
        else:
            return self.add_inc_ret_recursiv(inc_ret, n)

    def get_all_inc_ret_repo(self):
        """
        getter pentru toata lista de inchirieri_returnari
        :return:
        """
        return self.__inc_ret

    def cauta_dupa_id_carte(self, id_carte):
        """
        cautam o carte dupa id
        daca se gaseste, atunci o afisam
        altfel, daca nu gasim id-ul, se arunca eroarea "id inexistent!\n"
        :param id_carte: int
        :return:
        """
        ok = True
        for _carte in self.__inc_ret:
            if _carte.get_id_carte() == id_carte:
                return _carte
        if ok:
            raise RepositoryError("id inexistent!")

    def cauta_dupa_id_client(self, id_client):
        """
        cautam clientii dupa id
        daca getter-ul id-ului clientului este egal cu id_client pe care il cautam, atunci se va afisa clientul
        altfel, daca nu exista id-ul, se va arunca eroarea "id inexistent!\n"
        :param id_client: int
        :return:
        """
        ok = True
        for _clients in self.__inc_ret:
            if _clients.get_id_client() == id_client:
                return _clients
        if ok:
            raise RepositoryError("id inexistent!\n")

    def cauta_dupa_id(self, id_inc_ret):
        """
        cautam dupa id o inchiriere_returnare
        daca nu se gaseste, atunci se va arunca eroarea "id inexistent!\n"
        :param id_inc_ret: int
        :return:
        """
        ok = True
        for _inc_ret in self.__inc_ret:
            if _inc_ret.get_id_inc_ret() == id_inc_ret:
                return _inc_ret
        if ok:
            raise RepositoryError("id inexistent!\n")

    def sterge_inc_ret_dupa_id(self, user_input):
        """
        functie care sterge
        :param user_input: int
        :return:
        """
        allir = self.__inc_ret
        allir[:] = [_inc_ret for _inc_ret in allir if not _inc_ret.get_id_inc_ret() == user_input]# or _inc_ret.get_id_client_inc_ret() == user_input]
        return allir

    def modificare_inc_ret(self, option1, option2):
        """
        modificam inchirierile_returnarile din lista in functie de input-ul de la user : option1
        option1 reprezinta id-ul inchirierii_returnarii din lista pe care urmeaza sa il updatam
        :param option2: int
        :param option1: int
        :return:
        """
        allir = self.__inc_ret
        ok = False
        for _inc_ret in allir:
            if _inc_ret.get_id_inc_ret() == option1:
                ok = True
                _inc_ret.set_durata(option2)
        if ok:
            return allir
        else:
            raise RepositoryError("inexistent!\n")


class FileRepoIncRet(RepoIncRet):
    def __init__(self, filePath):
        RepoIncRet.__init__(self)
        self.__filePath = filePath

    def __read_all_from_file(self):
        self._inc_ret = []
        with open(self.__filePath, "r") as f:
            lines = f.readlines()
            contor_linii = 1
            for line in lines:
                line.strip()  # curat linia, elimin spatiile
                if len(line) > 0:
                    if contor_linii % 4 == 1:
                        id_inc_ret = int(line)
                    elif contor_linii % 4 == 2:
                        id_carte = int(line)
                    elif contor_linii % 4 == 3:
                        id_client = int(line)
                    elif contor_linii % 4 == 0:
                        durata = int(line)
                        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
                        self._inc_ret.append(inc_ret)
                        #print(self._inc_ret)
                        print(inc_ret)
                contor_linii += 1

    def __append_to_file(self, inc_ret):
        """
        adaugam in fisier o inchiriere/returnare
        :param inc_ret: obiect de tip inc_ret
        :return:
        """
        with open(self.__filePath, "a") as f:
            f.write(str(inc_ret.get_id_inc_ret()) + "\n" + str(inc_ret.get_id_carte()) + "\n" + str(inc_ret.get_id_client()) + "\n" + str(inc_ret.get_durata()) + "\n")

    def adauga_inc_ret_repo(self, inc_ret):
        """
        adaugam in fisier o inchiriere/returnare
        :param inc_ret: obiect de tip inc_ret9
        :return:
        """
        self.__read_all_from_file()
        RepoIncRet.adauga_inc_ret_repo(self, inc_ret)
        self.__append_to_file(inc_ret)

    def cauta_dupa_id_client(self, id_client):
        """
        cautam in fisier dupa id un client
        :param id_client: int
        :return:
        """
        self.__read_all_from_file()
        return RepoIncRet.cauta_dupa_id_client(self, id_client)

    def get_all_inc_ret_repo(self):
        """
        getter pentru toate inc_ret
        :return:
        """
        self.__read_all_from_file()
        return RepoIncRet.get_all_inc_ret_repo(self)

    def __len__(self):
        """
        suprascriem len-ul
        :return:
        """
        self.__read_all_from_file()
        return RepoIncRet.__len__(self)

    def write_all_to_file(self):
        with open(self.__filePath, "w") as f:
            for ir in self._inc_ret:
                f.write(str(ir.get_id_inc_ret()) + "\n" + str(ir.get_id_carte_inc_ret()) + "\n" + str(ir.get_id_client_inc_ret()) + "\n" + str(ir.get_durata()) + "\n")

    def modificare_inc_ret(self, option1, option2):
        self.__read_all_from_file()
        RepoIncRet.modificare_inc_ret(self, option1, option2)
        self.write_all_to_file()

    def sterge_inc_ret_dupa_id(self, user_input):
        self.__read_all_from_file()
        RepoIncRet.sterge_inc_ret_dupa_id(self, user_input)
        self.write_all_to_file()




