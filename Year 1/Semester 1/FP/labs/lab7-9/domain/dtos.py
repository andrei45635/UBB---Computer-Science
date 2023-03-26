class IncRetDTO(object):
    def __init__(self, id_inc_ret, id_carte, id_client, durata):
        self.__nr_inchirieri = 1
        self.__nr_inchirieri_client = 1
        self.__id_inc_ret = id_inc_ret
        self.__id_carte = id_carte
        self.__carte = None
        self.__id_client = id_client
        self.__client = None
        self.__durata = durata

    def get_id_inc_ret(self):
        return self.__id_inc_ret

    def get_id_carte(self):
        return self.__id_carte

    def set_id_carte(self, value):
        self.__id_carte = value

    def get_carte(self):
        return self.__carte

    def set_carte(self, value):
        self.__carte = value

    def get_id_client(self):
        return self.__id_client

    def get_client(self):
        return self.__client

    def set_client(self, value):
        self.__client = value

    def get_durata(self):
        return self.__durata

    def set_durata(self, value):
        self.__durata = value

    def add_inchirieri(self):
        """
        de fiecare data cand se inchiriaza o carte, incrementam cu 1
        :return:
        """
        self.__nr_inchirieri += 1

    def add_inchirieri_client(self):
        """
        de fiecare data cand se inchiriaza o carte, incrementam cu 1
        :return:
        """
        self.__nr_inchirieri_client += 1

    def get_nr_inchirieri(self):
        return self.__nr_inchirieri

    def get_nr_inchirieri_client(self):
        return self.__nr_inchirieri_client

    def __str__(self):
        return str(self.__carte.get_titlu()) + "[" + str(self.get_nr_inchirieri()) + "]" + "\n"


class IncRetDTO2(IncRetDTO):
    def __init__(self, id_inc_ret, id_carte, id_client, durata):
        IncRetDTO.__init__(self, id_inc_ret, id_carte, id_client, durata)

    def __str__(self):
        return str(self.__client.get_nume()) + "[" + str(self.get_nr_inchirieri_client()) + "\n"


class IncRetDTO3(object):
    def __init__(self, autor, listacarti):
        self.__autor = autor
        self.__listacarti = listacarti

    def __str__(self):
        aut = ""
        aut += self.__autor + ":\n"
        for autor in self.__listacarti:
            aut += "\t" + str(autor) + "\n"
        return str(aut)


class RetIncDTOs(object):
    def __init__(self, nume, listaclienti):
        self.__nume = nume
        self.__listaclienti = listaclienti

    def __str__(self):
        st = ""
        st += self.__nume + ":\n"
        for client in self.__listaclienti:
            st += "\t" + str(client) + "\n"
        return st


class IncRetDTOs(object):
    def __init__(self, titlu, listacarti):
        self.__titlu = titlu
        self.__listacarti = listacarti

    def __str__(self):
        st = ""
        #st += str(self.__titlu) + ":\n"
        for carte in self.__listacarti:
            st += "\t" + str(carte) +"\n"
        return str(st)


class CartiDTO(object):
    def __init__(self, id_carte, desc, titlu, autor):
        self.__id_carte = id_carte
        self.__carte = None
        self.__desc = desc
        self.__titlu = titlu
        self.__autor = autor

    def get_id_carte(self):
        return self.__id_carte

    def get_carte(self):
        return self.__carte

    def get_desc(self):
        return self.__desc

    def get_titlu(self):
        return self.__titlu

    def get_autor(self):
        return self.__autor

    def set_carte(self, value):
        self.__carte = value


class ClientiDTO(object):
    def __init__(self, id_client, nume, cnp):
        self.__id_client = id_client
        self.__client = None
        self.__nume = nume
        self.__cnp = cnp

    def get_id_client(self):
        return self.__id_client

    def get_client(self):
        return self.__client

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def set_client(self, value):
        self.__client = value


