from domain.entitati import Ingredient
from business.servicii import ServiceIngrediente
from validare.validatori import ValidatorIngredient
from erori.exceptii import ValidationError, RepositoryError
from infrastructure.repository import RepoIngrediente


def __test_adauga_ingredient_service():
    repo = RepoIngrediente()
    valid = ValidatorIngredient()
    srv = ServiceIngrediente(valid, repo)
    id_ing = 23
    nume = "faina"
    cantitate = 34.56
    assert (srv.get_nr_ingrediente() == 0)
    srv.adauga_ingredient(id_ing, nume, cantitate)
    assert (srv.get_nr_ingrediente() == 1)
    alt_nume = "malai"
    alta_cantitate = 45.78
    try:
        srv.adauga_ingredient(id_ing,alt_nume,alta_cantitate)
        assert False
    except RepositoryError as re:
        assert(str(re) == "id existent!\n")
    inv_id_ing = -23
    inv_nume = ""
    inv_cantitate = -2412
    try:
        srv.adauga_ingredient(inv_id_ing, inv_nume, inv_cantitate)
        assert False
    except ValidationError as ve:
        assert(str(ve) == "id invalid!\nnume invalid!\ncantitate invalida!\n")


class Teste(object):
    def __test_adauga_ingredient_service(self):
        repo = RepoIngrediente()
        valid = ValidatorIngredient()
        srv = ServiceIngrediente(valid, repo)
        id_ing = 23
        nume = "faina"
        cantitate = 34.56
        assert (srv.get_nr_ingrediente() == 0)
        srv.adauga_ingredient(id_ing, nume, cantitate)
        assert (srv.get_nr_ingrediente() == 1)
        alt_nume = "malai"
        alta_cantitate = 45.78
        try:
            srv.adauga_ingredient(id_ing, alt_nume, alta_cantitate)
            assert False
        except RepositoryError as re:
            assert (str(re) == "id existent!\n")
        inv_id_ing = -23
        inv_nume = ""
        inv_cantitate = -2412
        try:
            srv.adauga_ingredient(inv_id_ing, inv_nume, inv_cantitate)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\ncantitate invalida!\n")

    def __test_creeaza_ingredient(self):
        id_ing = 23
        nume = "faina"
        pret_unitate = 34.56
        ing = Ingredient(id_ing, nume, pret_unitate)
        assert (ing.get_id_ing() == id_ing)
        assert (ing.get_nume() == nume)
        assert (abs(ing.get_pret_unitate() - pret_unitate) < 0.0001)
        alt_nume = "malai"
        alta_cantitate = 251.2
        alt_ing = Ingredient(id_ing, alt_nume, alta_cantitate)
        assert (ing == alt_ing)
        assert (ing.__eq__(alt_ing))
        assert (str(ing) == "[23]faina->34.56")
        assert (ing.__str__() == "[23]faina->34.56")

    def __test_valideaza_ingredient(self):
        id_ing = 23
        nume = "faina"
        pret_unitate = 34.56
        ing = Ingredient(id_ing, nume, pret_unitate)
        valid = ValidatorIngredient()
        valid.valideaza(ing)
        inv_id_ing = -23
        inv_nume = ""
        inv_pret_unitate = -2412
        ing_inv_id = Ingredient(inv_id_ing, nume, pret_unitate)
        ing_inv = Ingredient(inv_id_ing, inv_nume, inv_pret_unitate)
        try:
            valid.valideaza(ing_inv_id)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")
        try:
            valid.valideaza(ing_inv)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\ncantitate invalida!\n")

    def __test_adauga_ingredieng_repo(self):
        repo = RepoIngrediente()
        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        id_ing = 23
        nume = "faina"
        cantitate = 34.56
        ing = Ingredient(id_ing, nume, cantitate)
        repo.adauga_ingredient(ing)
        assert (len(repo) == 1)
        ing_gasit = repo.cauta_id(id_ing)
        assert (ing_gasit == ing)
        assert (ing_gasit.get_nume() == nume)
        assert (abs(ing_gasit.get_pret_unitate() - ing.get_pret_unitate() == cantitate) < 0.0001)
        all = repo.get_all_ingredients()
        assert (len(all) == 1)
        assert (all[0] == ing)
        assert (all[0].get_nume() == nume)
        assert (abs(all[0].get_pret_unitate() - ing.get_pret_unitate() == cantitate) < 0.0001)
        id_ing_inexist = 24
        try:
            repo.cauta_id(id_ing_inexist)
            assert False
        except RepositoryError as re:
            assert(str(re) == "id inexistent!\n")
        alt_nume = "malai"
        alta_cantitate = 45.78
        alt_ing_same_id = Ingredient(id_ing, alt_nume, alta_cantitate)
        try:
            repo.adauga_ingredient(alt_ing_same_id)
            assert False
        except RepositoryError as re:
            assert(str(re) == "id existent!\n")

    def run_all_tests(self):
        print("start")
        self.__test_creeaza_ingredient()
        self.__test_valideaza_ingredient()
        self.__test_adauga_ingredieng_repo()
        self.__test_adauga_ingredient_service()
        print("finish")
