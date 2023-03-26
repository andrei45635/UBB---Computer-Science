from domain.entitati import Ingredient


class ServiceIngrediente(object):
    def __init__(self, validator_ingredient, repo_ingredient):
        self.__validator_ingredient = validator_ingredient
        self.__repo_ingrediente = repo_ingredient

    def get_nr_ingrediente(self):
        return len(self.__repo_ingrediente)

    def adauga_ingredient(self, id_ing, nume, cantitate):
        ingredient = Ingredient(id_ing, nume, cantitate)
        self.__validator_ingredient.valideaza(ingredient)
        self.__repo_ingrediente.adauga_ingredient(ingredient)

    def get_all_ingrediente(self):
        return self.__repo_ingrediente.get_all_ingredients()


class ServiceRetete(object):
    def __init__(self, validator_reteta, repo_reteta):
        self.__validator_retete = validator_reteta
        self.__repo_retete = repo_reteta
