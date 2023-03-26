from domain.entitati import Caine


class Teste(object):

    def __run_creeaza_caine_tests(self):
        id_caine = 25
        nume = "Dufi"
        greutate = 23.45
        caine = Caine(id_caine,nume,greutate)
        Caine.get_id_caine(caine)
        assert(caine.get_id_caine()==id_caine)

    def run_all_tests(self):
        print("start teste ai die pula mea...")
        self.__run_creeaza_caine_tests()
        print("finish teste ai die pula mea...")
