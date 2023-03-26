from erori.exceptii import RepositoryError


class RepoIngrediente(object):

    def __init__(self):
        self.__ingrediente = []

    def __len__(self):
        return len(self.__ingrediente)

    def adauga_ingredient(self, ing):
        for _ing in self.__ingrediente:
            if _ing == ing:
                raise RepositoryError("id existent!\n")
        self.__ingrediente.append(ing)

    def cauta_id(self, id_ing):
        ok = True
        for _ing in self.__ingrediente:
            if _ing.get_id_ing() == id_ing:
                return _ing
        if ok:
            raise RepositoryError("id inexistent!\n")

    def get_all_ingredients(self):
        return self.__ingrediente[:]


class RepoRetete(object):

    def __init__(self):
        self.__retete = []
        
class FileRepoIngrediente(RepoIngrediente):
    def __init__(self,file_path):
        RepoIngrediente.__ingrediente = []


class RepoIngredienteReteta(object):
    def __init__(self):
        self.__ing_ret = []