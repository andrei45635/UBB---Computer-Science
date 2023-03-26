class Ingredient(object):
    def __init__(self, id_ing, nume, pret_unitate):
        self.__id_ing = id_ing
        self.__nume = nume
        self.__pret_unitate = pret_unitate

    def get_id_ing(self):
        return self.__id_ing

    def get_nume(self):
        return self.__nume

    def get_pret_unitate(self):
        return self.__pret_unitate

    def set_nume(self, value):
        self.__nume = value

    def set_pret_unitate(self, value):
        self.__pret_unitate = value

    def __eq__(self, other):
        return self.__id_ing == other.__id_ing

    def __str__(self):
        return "["+str(self.__id_ing)+"]" + self.__nume+"->"+str(self.__pret_unitate)

class Reteta(object):
    pass 