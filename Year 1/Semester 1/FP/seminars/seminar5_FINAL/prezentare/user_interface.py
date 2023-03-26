from erori.exceptii import RepositoryError,ValidationError


class Consola(object):

    def __init__(self,srv_ingrediente,srv_retete):
        self.__srv_ingrediente = srv_ingrediente
        self.__srv_retete = srv_retete

    def __ui_adauga_ing(self):
        try:
            id_ing = int(input("id ingredient: "))
        except ValueError:
            print("id numeric invalid!")
            return
        nume = input("nume: ")
        try:
            pret_unitate = float(input("pret_unitate: "))
        except ValueError:
            print("date numerice invalide!")
            return
        self.__srv_ingrediente.adauga_ingredient(id_ing, nume, pret_unitate)
        print("ingredient adaugat cu succes!")

    def __ui_print_ingrediente(self):
        ingrediente = self.__srv_ingrediente.get_all_ingrediente()
        for _ingredient in ingrediente:
            print(_ingredient)

    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return
            if cmd == " ":
                continue
            if cmd == "add_ing":
                try:
                    self.__ui_adauga_ing()
                except ValidationError as ve:
                    print("validation error:\n" + str(ve))
                except RepositoryError as re:
                    print("repository error:\n" + str(re))
            elif cmd == "print_ings":
                self.__ui_print_ingrediente()
            else:
                print("comanda invalida!")