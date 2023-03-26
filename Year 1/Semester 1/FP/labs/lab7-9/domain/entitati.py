class Carte(object):
    def __init__(self, id_carte, titlu, desc, autor):
        self.__id_carte = id_carte
        self.__titlu = titlu
        self.__desc = desc
        self.__autor = autor

    def get_id_carte(self):
        return self.__id_carte

    def get_titlu(self):
        return self.__titlu

    def get_desc(self):
        return self.__desc

    def get_autor(self):
        return self.__autor

    def set_desc(self, value):
        self.__desc = value

    def __eq__(self, other):
        """
        suprascriem egalitatea pentru a verifica id-ul cartii
        :param other: obiect
        :return:
        """
        return self.__id_carte == other.__id_carte

    def __str__(self):
        """
        suprascriem functia str() ca sa trecem la forma pe care o dorim pentru carte in output
        :return:
        """
        return "[" + str(self.__id_carte) + "]"  + " " + str(self.__titlu) + " descriere: " + str(self.__desc)  + " de " + str(self.__autor)


class Client(object):
    def __init__(self, id_client, nume, cnp):
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp

    def get_id_client(self):
        return self.__id_client

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def set_nume(self, value):
        self.__nume = value

    def __str__(self):
        """
        suprascriem functia str() ca sa trecem la forma pe care o dorim pentru client in output
        :return:
        """
        return "[" + str(self.__id_client) + "]"  + " nume: " + str(self.__nume)  + " CNP: " + str(self.__cnp)


class IncRet(object):
    def __init__(self, id_inc_ret, id_carte, id_client, durata):
        self.__id_inc_ret = id_inc_ret
        self.__id_carte = id_carte
        self.__id_client = id_client
        self.__durata = durata

    def get_id_inc_ret(self):
        return self.__id_inc_ret

    def get_id_carte_inc_ret(self):
        return self.__id_carte

    def get_id_client_inc_ret(self):
        return self.__id_client

    def get_durata(self):
        return self.__durata

    def set_durata(self, value):
        self.__durata = value

    def __eq__(self, other):
        return self.__id_inc_ret == other.__id_inc_ret

    def __str__(self):
        return "ID inchiriere [" + str(self.__id_inc_ret) + "]: Cartea cu ID-ul [" + str(
            self.__id_carte) + "] a fost inchiriata de clientul cu ID-ul [" + str(
            self.__id_client) + "] pentru o durata de [" + str(self.__durata) + "] zile"
