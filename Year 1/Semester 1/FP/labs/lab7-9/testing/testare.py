from domain.entitati import Carte, Client, IncRet
from validare.validation import ValidatorCarte, ValidatorClient, ValidatorIncRet
from erori.exceptii import ValidationError, RepositoryError
from infrastructure.repository import RepoCarti, RepoClienti, RepoIncRet, FileRepoCarti
from business.servicii import ServiceCarte, ServiceClient, ServiceIncRet
import unittest

class TestingPyUnit(unittest.TestCase):
    def setUp(self):
        pass
    """
    def test_creeaza_repo_vid(self):
        filePath = "C:\FP\lab7-9-master\testing\test_carti.txt"
        with open(filePath, "w") as f:
            f.write("")
        try:
            repo = FileRepoCarti(filePath)
        except Exception as ex:
            print(ex)
            return
        assert (repo.__len__() == 0)
        assert (len(repo) == 0)
        return repo
    """
    def test_create_carte(self):
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        self.assertEqual(carte.get_id_carte(), id_carte)
        self.assertEqual(carte.get_desc(), desc)
        self.assertEqual(carte.get_titlu(), titlu)
        self.assertEqual(carte.get_autor(), autor)

    def test_valid_carte(self):
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        valid = ValidatorCarte()
        valid.valideaza(carte)
        inv_id_carte = -24
        inv_titlu = " "
        inv_desc = 1241
        inv_autor = " "
        carte_gresita = Carte(inv_id_carte, titlu, desc, autor)
        try:
            valid.valideaza(carte_gresita)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")
        inv_carte = Carte(inv_id_carte, inv_titlu, inv_desc, inv_autor)
        try:
            valid.valideaza(inv_carte)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\ntitlu invalid!\ndescriere invalida!\nautor invalid!\n")

    def test_add_repo_carte(self):
        repo = RepoCarti()
        assert (repo.__len__() == 0)
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica"
        carte = Carte(id_carte, titlu, desc, autor)
        repo.adauga_carte_repo(carte)
        self.assertEqual(repo.__len__(), 1)
        carte_gasita = repo.cauta_dupa_id(id_carte)
        self.assertEqual(str(carte_gasita), "[24] George descriere: Becali de Gica")
        self.assertEqual(carte_gasita.get_id_carte(), id_carte)
        self.assertEqual(carte_gasita.get_desc(), desc)
        self.assertEqual(carte_gasita.get_titlu(), titlu)
        #self.assertEqual(carte_gasita.get_autor, autor)

    def test_add_carte_srv(self):
        valid = ValidatorCarte()
        repo = RepoCarti()
        srv = ServiceCarte(valid, repo)
        self.assertEqual(srv.get_nr_carti(), 0)
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        srv.adauga_carte(id_carte, titlu, desc, autor)
        self.assertEqual(srv.get_nr_carti(), 1)
        alt_titlu = "Gigi"
        alt_desc = "Bibi"
        alt_autor = "Bratan"
        with self.assertRaises(RepositoryError) as re:
            srv.adauga_carte(id_carte, alt_titlu, alt_desc, alt_autor)
        exceptii = re.exception
        self.assertEqual(exceptii,re.exception)
        inv_id_carte = -24
        inv_titlu = " "
        inv_desc = 1241
        inv_autor = " "
        with self.assertRaises(ValidationError) as ve:
            srv.adauga_carte(inv_id_carte, inv_titlu, inv_desc, inv_autor)
        exceptia = ve.exception
        self.assertEqual(exceptia,ve.exception)

    def test_search_by_id(self):
        valid = ValidatorCarte()
        repo = RepoCarti()
        srv = ServiceCarte(valid, repo)
        self.assertEqual(srv.get_nr_carti(), 0)
        id_carte = 24
        titlu_1 = "George"
        desc_1 = "Becali"
        autor_1 = "Gica Becali"
        srv.adauga_carte(id_carte, titlu_1, desc_1, autor_1)
        id_carte_2 = 25
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        srv.adauga_carte(id_carte_2, titlu_2, desc_2, autor_2)
        self.assertEqual(srv.get_nr_carti(), 2)
        srv.cauta_carte_dupa_id(25)
        self.assertEqual(str(srv.cauta_carte_dupa_id(25)), "[25] Gicu descriere: Groparu de Gicutu Gropica")

    def test_delete_carte_repo(self):
        repo = RepoCarti()
        self.assertEqual(repo.__len__(), 0)
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo.adauga_carte_repo(carte)
        id_carte_2 = 25
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        carte_2 = Carte(id_carte_2, titlu_2, desc_2, autor_2)
        repo.adauga_carte_repo(carte_2)
        self.assertEqual(repo.__len__(), 2)
        repo.sterge_carte(24)
        self.assertEqual(repo.__len__(), 1)

    def test_delete_carte_srv(self):
        valid = ValidatorCarte()
        repo = RepoCarti()
        srv = ServiceCarte(valid, repo)
        self.assertEqual(srv.get_nr_carti(), 0)
        id_carte = 24
        titlu_1 = "George"
        desc_1 = "Becali"
        autor_1 = "Gica Becali"
        srv.adauga_carte(id_carte, titlu_1, desc_1, autor_1)
        id_carte_2 = 25
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        srv.adauga_carte(id_carte_2, titlu_2, desc_2, autor_2)
        self.assertEqual(srv.get_nr_carti(), 2)
        srv.stergere_carti(24)
        self.assertEqual(srv.get_nr_carti(), 1)

    def test_modify_carte_repo(self):
        repo = RepoCarti()
        self.assertEqual(repo.__len__(), 0)
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo.adauga_carte_repo(carte)
        id_carte_2 = 23
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        carte_2 = Carte(id_carte_2, titlu_2, desc_2, autor_2)
        repo.adauga_carte_repo(carte_2)
        self.assertEqual(repo.__len__(), 2)
        repo.modificare_carte(23, "Cimitir")
        self.assertEqual(repo.__len__(), 2)

    def test_modify_carte_srv(self):
        valid = ValidatorCarte()
        repo = RepoCarti()
        srv = ServiceCarte(valid, repo)
        self.assertEqual(srv.get_nr_carti(), 0)
        id_carte = 24
        titlu_1 = "George"
        desc_1 = "Becali"
        autor_1 = "Gica Becali"
        srv.adauga_carte(id_carte, titlu_1, desc_1, autor_1)
        id_carte_2 = 25
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        srv.adauga_carte(id_carte_2, titlu_2, desc_2, autor_2)
        self.assertEqual(srv.get_nr_carti(), 2)
        srv.modifica_carte(25, "Cimitir")
        self.assertEqual(srv.get_nr_carti(), 2)

    def test_create_client(self):
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        self.assertEqual(client.get_id_client(), id_client)
        self.assertEqual(client.get_nume(), nume)
        self.assertEqual(client.get_cnp(), cnp)
        alt_nume = "DJ Vasile"
        alt_cnp = 1512412
        alt_client = Client(id_client, alt_nume, alt_cnp)
        self.assertEqual(client.get_id_client(), alt_client.get_id_client())
        self.assertEqual(str(client), "[24] nume: Gicu Groparu CNP: 213412")

    def test_validate_client(self):
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        valid = ValidatorClient()
        valid.valideaza(client)
        inv_id_client = -24
        inv_nume = 2421
        inv_cnp = -21412
        inv_client = Client(inv_id_client, inv_nume, inv_cnp)
        try:
            valid.valideaza(inv_client)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\ncnp invalid!\n")
        alt_id_client = 25
        alt_nume = "DJ Vasile"
        alt_cnp = 1241241
        alt_client = Client(inv_id_client, alt_nume, alt_cnp)
        try:
            valid.valideaza(alt_client)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")
        alt_client_2 = Client(alt_id_client, alt_nume, inv_cnp)
        try:
            valid.valideaza(alt_client_2)
        except ValidationError as ve:
            assert (str(ve) == "cnp invalid!\n")

    def test_add_client_repo(self):
        repo = RepoClienti()
        self.assertEqual(repo.__len__(), 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo.adauga_client_repo(client)
        self.assertEqual(repo.__len__(), 1)
        client_gasit = repo.cauta_dupa_id_client(id_client)
        self.assertEqual(client_gasit.get_id_client(), id_client)
        self.assertEqual(client_gasit.get_nume(), nume)
        self.assertEqual(client_gasit.get_cnp(), cnp)

    def test_add_client_srv(self):
        valid = ValidatorClient()
        repo = RepoClienti()
        srv = ServiceClient(valid, repo)
        self.assertEqual(srv.get_nr_clienti(), 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        srv.adauga_client(id_client, nume, cnp)
        self.assertEqual(srv.get_nr_clienti(), 1)
        alt_nume = "Gica Becali"
        alt_cnp = 14512431
        with self.assertRaises(RepositoryError) as re:
            srv.adauga_client(id_client, alt_nume, alt_cnp)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)
        with self.assertRaises(RepositoryError) as re:
            srv.adauga_client(id_client, alt_nume, cnp)
        exceptionss = re.exception
        self.assertEqual(exceptionss, re.exception)
        inv_id_client = -24
        inv_nume = 2421
        inv_cnp = -21412
        with self.assertRaises(ValidationError) as ve:
            srv.adauga_client(inv_id_client, inv_nume, inv_cnp)
        excepts = ve.exception
        self.assertEqual(excepts, ve.exception)

    def test_search_client_id(self):
        valid = ValidatorClient()
        repo = RepoClienti()
        srv = ServiceClient(valid, repo)
        self.assertEqual(srv.get_nr_clienti(), 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        srv.adauga_client(id_client, nume, cnp)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        srv.adauga_client(id_client_2, nume_2, cnp_2)
        self.assertEqual(srv.get_nr_clienti(), 2)
        srv.cauta_clienti_dupa_id(24)
        self.assertEqual(str(srv.cauta_clienti_dupa_id(24)), "[24] nume: Gicu Groparu CNP: 213412")

    def test_delete_clienti_repo(self):
        repo = RepoClienti()
        self.assertEqual(repo.__len__(), 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo.adauga_client_repo(client)
        self.assertEqual(repo.__len__(), 1)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        client_2 = Client(id_client_2, nume_2, cnp_2)
        repo.adauga_client_repo(client_2)
        self.assertEqual(repo.__len__(), 2)
        repo.stergere_clienti(24)
        self.assertEqual(repo.__len__(), 1)

    def test_delete_clienti_srv(self):
        valid = ValidatorClient()
        repo = RepoClienti()
        srv = ServiceClient(valid, repo)
        self.assertEqual(srv.get_nr_clienti(), 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        srv.adauga_client(id_client, nume, cnp)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        srv.adauga_client(id_client_2, nume_2, cnp_2)
        self.assertEqual(srv.get_nr_clienti(), 2)
        srv.sterge_clienti(24)
        self.assertEqual(srv.get_nr_clienti(), 1)

    def test_modify_clienti_repo(self):
        repo = RepoClienti()
        self.assertEqual(repo.__len__(), 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo.adauga_client_repo(client)
        self.assertEqual(repo.__len__(), 1)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        client_2 = Client(id_client_2, nume_2, cnp_2)
        repo.adauga_client_repo(client_2)
        self.assertEqual(repo.__len__(), 2)
        repo.modificare_client(25, "Pipilica")
        self.assertEqual(repo.__len__(), 2)

    def test_modify_client_srv(self):
        valid = ValidatorClient()
        repo = RepoClienti()
        srv = ServiceClient(valid, repo)
        self.assertEqual(srv.get_nr_clienti(), 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        srv.adauga_client(id_client, nume, cnp)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        srv.adauga_client(id_client_2, nume_2, cnp_2)
        self.assertEqual(srv.get_nr_clienti(), 2)
        srv.modifica_client(25, "Pipilica")
        self.assertEqual(srv.get_nr_clienti(), 2)

    def test_create_inc_ret(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 24
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        self.assertEqual(inc_ret.get_id_inc_ret(), id_inc_ret)
        self.assertEqual(inc_ret.get_id_carte_inc_ret(), id_carte)
        self.assertEqual(inc_ret.get_id_client_inc_ret(), id_client)
        self.assertEqual(inc_ret.get_durata(), durata)
        alt_id_carte = 20
        alt_id_client = 91
        alta_durata = 10
        alta_inc_ret = IncRet(id_inc_ret, alt_id_carte, alt_id_client, alta_durata)
        self.assertEqual(inc_ret, alta_inc_ret)

    def test_validate_inc_ret(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 24
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid = ValidatorIncRet()
        valid.valideaza(inc_ret)
        id_inc_ret_inv = -24
        durata_inv = -45
        inv_id_carte = -24
        inv_id_client = -24
        inc_ret_inv = IncRet(id_inc_ret_inv, inv_id_carte, inv_id_client, durata_inv)
        try:
            valid.valideaza(inc_ret_inv)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id inchiriere_returnare invalid!\nid carte invalid!\nid client invalid!\ndurata invalida!\n")

    def test_add_inc_ret_repo(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 24
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        repo = RepoIncRet()
        repo.adauga_inc_ret_repo(inc_ret)
        self.assertEqual(repo.__len__(), 1)
        inc_ret_gasita = repo.cauta_dupa_id(id_inc_ret)
        self.assertEqual(inc_ret_gasita.get_id_inc_ret(),id_inc_ret)
        self.assertEqual(inc_ret_gasita.get_id_carte_inc_ret(),id_carte)
        self.assertEqual(inc_ret_gasita.get_id_client_inc_ret(), id_client)
        self.assertEqual(inc_ret_gasita.get_durata(),durata)

    def test_add_inc_ret_srv(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        self.assertEqual(srv.get_nr_inc_ret(), 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        self.assertEqual(srv.get_nr_inc_ret(), 1)

    def test_delete_inc_ret_repo_by_id(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 25
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        repo = RepoIncRet()
        repo.adauga_inc_ret_repo(inc_ret)
        self.assertEqual(repo.__len__(), 1)
        repo.sterge_inc_ret_dupa_id(28)
        self.assertEqual(repo.__len__(), 0)

    def test_delete_inc_ret_srv_by_id(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        self.assertEqual(srv.get_nr_inc_ret(), 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        self.assertEqual(srv.get_nr_inc_ret(), 1)
        srv.sterge_inc_ret(28)
        self.assertEqual(srv.get_nr_inc_ret(), 0)

    def test_modify_inc_ret_repo(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 25
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        repo = RepoIncRet()
        repo.adauga_inc_ret_repo(inc_ret)
        self.assertEqual(repo.__len__(), 1)
        repo.modificare_inc_ret(28, 10)
        self.assertEqual(repo.__len__(), 1)

    def test_modify_inc_ret_srv(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        self.assertEqual(srv.get_nr_inc_ret(), 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        self.assertEqual(srv.get_nr_inc_ret(), 1)
        srv.modifica_inc_ret(28, 10)
        self.assertEqual(srv.get_nr_inc_ret(), 1)

    def test_get_all_inchirieri_carti(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        self.assertEqual(srv.get_nr_inc_ret(), 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        self.assertEqual(srv.get_nr_inc_ret(), 1)
        self.assertEqual(len(srv.get_all_inc_ret_carti_inchirieri()), 1)

    def test_get_inchirieri_clienti(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        self.assertEqual(srv.get_nr_inc_ret(), 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        self.assertEqual(srv.get_nr_inc_ret(), 1)
        self.assertEqual(len(srv.get_all_inc_ret_clienti_inchirieri()), 1)

    def test_get_top_clienti(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        self.assertEqual(srv.get_nr_inc_ret(), 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        self.assertEqual(srv.get_nr_inc_ret(), 1)
        self.assertEqual(len(srv.get_top_20_clienti()), 1)


if __name__ == '__main__':
    unittest.main()


class Teste(object):
    def __test_creeaza_repo_vid(self):
        filePath = "testing/test_carti.txt"
        with open(filePath, "w") as f:
            f.write("")
        try:
            repo = FileRepoCarti(filePath)
        except Exception as ex:
            print(ex)
            return
        assert (repo.__len__() == 0)
        assert (len(repo) == 0)
        return repo

    def __test_creeaza_carte(self):
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        assert (carte.get_id_carte() == id_carte)
        assert (carte.get_titlu() == titlu)
        assert (carte.get_desc() == desc)
        assert (carte.get_autor() == autor)
        alt_titlu = "Gigi"
        alt_desc = "Bibi"
        alt_autor = "Bratan"
        alta_carte = Carte(id_carte, alt_titlu, alt_desc, alt_autor)
        assert (carte == alta_carte)
        assert (carte.__eq__(alta_carte))
        #assert (str(carte) == "[24], George, descriere: Becali, de Gica Becali")

    def __test_valideaza_carte(self):
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        valid = ValidatorCarte()
        valid.valideaza(carte)
        inv_id_carte = -24
        inv_titlu = " "
        inv_desc = 1241
        inv_autor = " "
        carte_gresita = Carte(inv_id_carte, titlu, desc, autor)
        try:
            valid.valideaza(carte_gresita)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")
        inv_carte = Carte(inv_id_carte, inv_titlu, inv_desc, inv_autor)
        try:
            valid.valideaza(inv_carte)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\ntitlu invalid!\ndescriere invalida!\nautor invalid!\n")

    def __test_adauga_carte_repo(self):
        repo = self.__test_creeaza_repo_vid()
        assert (repo.__len__() == 0)
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica"
        carte = Carte(id_carte, titlu, desc, autor)
        repo.adauga_carte_repo(carte)
        assert (repo.__len__() == 1)
        carte_gasita = repo.cauta_dupa_id(id_carte)
        #assert (str(carte_gasita) == "[24], George, descriere: Becali, de Gica")
        #assert (carte_gasita.get_id_carte() == id_carte)
        #assert (carte_gasita.get_titlu() == titlu)
        #assert (carte_gasita.get_desc() == desc)
        #assert (carte_gasita.get_autor() == autor)

    def __test_adauga_carte_srv(self):
        valid = ValidatorCarte()
        repo = RepoCarti()
        srv = ServiceCarte(valid, repo)
        assert (srv.get_nr_carti() == 0)
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        srv.adauga_carte(id_carte, titlu, desc, autor)
        assert (srv.get_nr_carti() == 1)
        alt_titlu = "Gigi"
        alt_desc = "Bibi"
        alt_autor = "Bratan"
        try:
            srv.adauga_carte(id_carte, alt_titlu, alt_desc, alt_autor)
            assert False
        except RepositoryError as re:
            assert (str(re) == "id existent!\n")
        inv_id_carte = -24
        inv_titlu = " "
        inv_desc = 1241
        inv_autor = " "
        try:
            srv.adauga_carte(inv_id_carte, inv_titlu, inv_desc, inv_autor)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\ntitlu invalid!\ndescriere invalida!\nautor invalid!\n")

    def __test_cauta_carti_dupa_id(self):
        valid = ValidatorCarte()
        repo = RepoCarti()
        srv = ServiceCarte(valid, repo)
        assert (srv.get_nr_carti() == 0)
        id_carte = 24
        titlu_1 = "George"
        desc_1 = "Becali"
        autor_1 = "Gica Becali"
        srv.adauga_carte(id_carte, titlu_1, desc_1, autor_1)
        id_carte_2 = 25
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        srv.adauga_carte(id_carte_2, titlu_2, desc_2, autor_2)
        assert (srv.get_nr_carti() == 2)
        srv.cauta_carte_dupa_id(25)
        #assert (str(srv.cauta_carte_dupa_id(25)) == "[25], Gicu, descriere: Groparu, de Gicutu Gropica")

    def __test_sterge_carte_repo(self):
        repo = RepoCarti()
        assert (repo.__len__() == 0)
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo.adauga_carte_repo(carte)
        id_carte_2 = 25
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        carte_2 = Carte(id_carte_2, titlu_2, desc_2, autor_2)
        repo.adauga_carte_repo(carte_2)
        assert (repo.__len__() == 2)
        repo.sterge_carte(24)
        assert (repo.__len__() == 1)

    def __test_sterge_carte_srv(self):
        valid = ValidatorCarte()
        repo = RepoCarti()
        srv = ServiceCarte(valid, repo)
        assert (srv.get_nr_carti() == 0)
        id_carte = 24
        titlu_1 = "George"
        desc_1 = "Becali"
        autor_1 = "Gica Becali"
        srv.adauga_carte(id_carte, titlu_1, desc_1, autor_1)
        id_carte_2 = 25
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        srv.adauga_carte(id_carte_2, titlu_2, desc_2, autor_2)
        assert (srv.get_nr_carti() == 2)
        srv.stergere_carti(24)
        assert (srv.get_nr_carti() == 1)

    def __test_modificare_carte_repo(self):
        repo = RepoCarti()
        assert (repo.__len__() == 0)
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo.adauga_carte_repo(carte)
        id_carte_2 = 23
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        carte_2 = Carte(id_carte_2, titlu_2, desc_2, autor_2)
        repo.adauga_carte_repo(carte_2)
        assert (repo.__len__() == 2)
        repo.modificare_carte(23, "Cimitir")
        assert (repo.__len__() == 2)

    def __test_modificare_carte_srv(self):
        valid = ValidatorCarte()
        repo = RepoCarti()
        srv = ServiceCarte(valid, repo)
        assert (srv.get_nr_carti() == 0)
        id_carte = 24
        titlu_1 = "George"
        desc_1 = "Becali"
        autor_1 = "Gica Becali"
        srv.adauga_carte(id_carte, titlu_1, desc_1, autor_1)
        id_carte_2 = 25
        titlu_2 = "Gicu"
        desc_2 = "Groparu"
        autor_2 = "Gicutu Gropica"
        srv.adauga_carte(id_carte_2, titlu_2, desc_2, autor_2)
        assert (srv.get_nr_carti() == 2)
        srv.modifica_carte(25, "Cimitir")
        assert (srv.get_nr_carti() == 2)

    def __test_creeaza_client(self):
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        assert (client.get_id_client() == id_client)
        assert (client.get_nume() == nume)
        assert (client.get_cnp() == cnp)
        alt_nume = "DJ Vasile"
        alt_cnp = 1512412
        alt_client = Client(id_client, alt_nume, alt_cnp)
        assert (client.get_id_client() == alt_client.get_id_client())
        #assert (str(client) == "[24], nume: Gicu Groparu, CNP: 213412")

    def __test_valideaza_client(self):
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        valid = ValidatorClient()
        valid.valideaza(client)
        inv_id_client = -24
        inv_nume = 2421
        inv_cnp = -21412
        inv_client = Client(inv_id_client, inv_nume, inv_cnp)
        try:
            valid.valideaza(inv_client)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\ncnp invalid!\n")
        alt_id_client = 25
        alt_nume = "DJ Vasile"
        alt_cnp = 1241241
        alt_client = Client(inv_id_client, alt_nume, alt_cnp)
        try:
            valid.valideaza(alt_client)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")
        alt_client_2 = Client(alt_id_client, alt_nume, inv_cnp)
        try:
            valid.valideaza(alt_client_2)
        except ValidationError as ve:
            assert (str(ve) == "cnp invalid!\n")

    def __test_adauga_client_repo(self):
        repo = RepoClienti()
        assert (repo.__len__() == 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo.adauga_client_repo(client)
        assert (repo.__len__() == 1)
        client_gasit = repo.cauta_dupa_id_client(id_client)
        assert (client_gasit.get_id_client() == id_client)
        assert (client_gasit.get_nume() == nume)
        assert (client_gasit.get_cnp() == cnp)
        all = repo.get_all_clients()
        assert (all[0].get_id_client() == id_client)
        assert (all[0].get_nume() == nume)
        assert (all[0].get_cnp() == cnp)

    def __test_adauga_client_srv(self):
        valid = ValidatorClient()
        repo = RepoClienti()
        srv = ServiceClient(valid, repo)
        assert (srv.get_nr_clienti() == 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        srv.adauga_client(id_client, nume, cnp)
        assert (srv.get_nr_clienti() == 1)
        alt_nume = "Gica Becali"
        alt_cnp = 14512431
        try:
            srv.adauga_client(id_client, alt_nume, alt_cnp)
        except RepositoryError as re:
            assert (str(re) == "id existent!\n")
        try:
            srv.adauga_client(id_client, alt_nume, cnp)
        except RepositoryError as re:
            assert (str(re) == "cnp existent!\nid existent!\n")
        inv_id_client = -24
        inv_nume = 2421
        inv_cnp = -21412
        try:
            srv.adauga_client(inv_id_client, inv_nume, inv_cnp)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\ncnp invalid!\n")

    def __test_cauta_clienti_dupa_id(self):
        valid = ValidatorClient()
        repo = RepoClienti()
        srv = ServiceClient(valid, repo)
        assert (srv.get_nr_clienti() == 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        srv.adauga_client(id_client, nume, cnp)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        srv.adauga_client(id_client_2, nume_2, cnp_2)
        assert (srv.get_nr_clienti() == 2)
        srv.cauta_clienti_dupa_id(24)
        #assert (str(srv.cauta_clienti_dupa_id(24)) == "[24], nume: Gicu Groparu, CNP: 213412")

    def __test_stergere_clienti_repo(self):
        repo = RepoClienti()
        assert (repo.__len__() == 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo.adauga_client_repo(client)
        assert (repo.__len__() == 1)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        client_2 = Client(id_client_2, nume_2, cnp_2)
        repo.adauga_client_repo(client_2)
        assert (repo.__len__() == 2)
        repo.stergere_clienti(24)
        assert (repo.__len__() == 1)

    def __test_stergere_clienti_srv(self):
        valid = ValidatorClient()
        repo = RepoClienti()
        srv = ServiceClient(valid, repo)
        assert (srv.get_nr_clienti() == 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        srv.adauga_client(id_client, nume, cnp)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        srv.adauga_client(id_client_2, nume_2, cnp_2)
        assert (srv.get_nr_clienti() == 2)
        srv.sterge_clienti(24)
        assert (srv.get_nr_clienti() == 1)

    def __test_modificare_client_repo(self):
        repo = RepoClienti()
        assert (repo.__len__() == 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo.adauga_client_repo(client)
        assert (repo.__len__() == 1)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        client_2 = Client(id_client_2, nume_2, cnp_2)
        repo.adauga_client_repo(client_2)
        assert (repo.__len__() == 2)
        repo.modificare_client(25, "Pipilica")
        assert (repo.__len__() == 2)

    def __test_modificare_client_srv(self):
        valid = ValidatorClient()
        repo = RepoClienti()
        srv = ServiceClient(valid, repo)
        assert (srv.get_nr_clienti() == 0)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        srv.adauga_client(id_client, nume, cnp)
        id_client_2 = 25
        nume_2 = "Pipi Titi"
        cnp_2 = 112411
        srv.adauga_client(id_client_2, nume_2, cnp_2)
        assert (srv.get_nr_clienti() == 2)
        srv.modifica_client(25, "Pipilica")
        assert (srv.get_nr_clienti() == 2)

    def __test_creeaza_inc_ret(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 24
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        assert (inc_ret.get_id_inc_ret() == id_inc_ret)
        assert (inc_ret.get_id_carte_inc_ret() == id_carte)
        assert (inc_ret.get_id_client_inc_ret() == id_client)
        assert (inc_ret.get_durata() == durata)
        alt_id_carte = 20
        alt_id_client = 91
        alta_durata = 10
        alta_inc_ret = IncRet(id_inc_ret, alt_id_carte, alt_id_client, alta_durata)
        assert (inc_ret == alta_inc_ret)

    def __test_valideaza_inc_ret(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 24
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid = ValidatorIncRet()
        valid.valideaza(inc_ret)
        id_inc_ret_inv = -24
        durata_inv = -45
        inv_id_carte = -24
        inv_id_client = -24
        inc_ret_inv = IncRet(id_inc_ret_inv, inv_id_carte, inv_id_client, durata_inv)
        try:
            valid.valideaza(inc_ret_inv)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id inchiriere_returnare invalid!\nid carte invalid!\nid client invalid!\ndurata invalida!\n")

    def __test_adauga_inc_ret_repo(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 24
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        repo = RepoIncRet()
        repo.adauga_inc_ret_repo(inc_ret)
        assert (repo.__len__() == 1)
        inc_ret_gasita = repo.cauta_dupa_id(id_inc_ret)
        assert (inc_ret_gasita.get_id_inc_ret() == id_inc_ret)
        assert (inc_ret_gasita.get_id_carte_inc_ret() == id_carte)
        assert (inc_ret_gasita.get_id_client_inc_ret() == id_client)
        assert (inc_ret_gasita.get_durata() == durata)
        all = repo.get_all_inc_ret_repo()
        assert (all[0].get_id_inc_ret() == id_inc_ret)
        assert (all[0].get_id_carte_inc_ret() == id_carte)
        assert (all[0].get_id_client_inc_ret() == id_client)
        assert (all[0].get_durata() == durata)

    def __test_adauga_inc_ret_srv(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        assert (srv.get_nr_inc_ret() == 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        assert (srv.get_nr_inc_ret() == 1)

    def __test_sterge_dupa_id_inc_ret_repo(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        id_client = 25
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        repo = RepoIncRet()
        repo.adauga_inc_ret_repo(inc_ret)
        assert (repo.__len__() == 1)
        repo.sterge_inc_ret_dupa_id(28)
        assert (repo.__len__() == 0)

    def __test_sterge_dupa_id_inc_ret_srv(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        assert (srv.get_nr_inc_ret() == 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        assert (srv.get_nr_inc_ret() == 1)
        srv.sterge_inc_ret(28)
        assert (srv.get_nr_inc_ret() == 0)

    def __test_mod_inc_ret_repo(self):
        id_inc_ret = 28
        durata = 7
        id_carte = 24
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        id_client = 25
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        repo = RepoIncRet()
        repo.adauga_inc_ret_repo(inc_ret)
        assert (repo.__len__() == 1)
        repo.modificare_inc_ret(28, 10)
        assert (repo.__len__() == 1)

    def __test_mod_inc_ret_srv(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        assert (srv.get_nr_inc_ret() == 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        carte_i = repo_carti.cauta_dupa_id(id_carte)
        client_i = repo_clienti.cauta_dupa_id_client(id_client)
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        assert (srv.get_nr_inc_ret() == 1)
        srv.modifica_inc_ret(28, 10)
        assert (srv.get_nr_inc_ret() == 1)

    def __test_get_all_nr_inchirieri_carti(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        assert (srv.get_nr_inc_ret() == 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        assert (srv.get_nr_inc_ret() == 1)
        assert(len(srv.get_all_inc_ret_carti_inchirieri()) == 1)

    def __test_get_nr_inchirieri_client(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        assert (srv.get_nr_inc_ret() == 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        assert (srv.get_nr_inc_ret() == 1)
        assert (len(srv.get_all_inc_ret_clienti_inchirieri()) == 1)

    def __test_get_top_clienti(self):
        valid = ValidatorIncRet()
        repo_inc_ret = RepoIncRet()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv = ServiceIncRet(valid, repo_inc_ret, repo_carti, repo_clienti)
        assert (srv.get_nr_inc_ret() == 0)
        id_carte = 29
        titlu = "George"
        desc = "Becali"
        autor = "Gica Becali"
        carte = Carte(id_carte, titlu, desc, autor)
        repo_carti.adauga_carte_repo(carte)
        id_client = 24
        nume = "Gicu Groparu"
        cnp = 213412
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client_repo(client)
        id_inc_ret = 28
        durata = 7
        inc_ret = IncRet(id_inc_ret, id_carte, id_client, durata)
        valid.valideaza(inc_ret)
        srv.adauga_inc_ret(id_inc_ret, id_carte, id_client, durata)
        assert (srv.get_nr_inc_ret() == 1)
        assert (len(srv.get_top_20_clienti()) == 1)

    def run_all_tests(self):
        print("incepere testare...")
        self.__test_creeaza_carte()
        self.__test_valideaza_carte()
        self.__test_adauga_carte_repo()
        self.__test_adauga_carte_srv()
        self.__test_cauta_carti_dupa_id()
        self.__test_creeaza_client()
        self.__test_valideaza_client()
        self.__test_adauga_client_repo()
        self.__test_adauga_client_srv()
        self.__test_cauta_clienti_dupa_id()
        self.__test_stergere_clienti_repo()
        self.__test_stergere_clienti_srv()
        self.__test_sterge_carte_repo()
        self.__test_sterge_carte_srv()
        self.__test_modificare_carte_repo()
        self.__test_modificare_carte_srv()
        self.__test_modificare_client_repo()
        self.__test_modificare_client_srv()
        self.__test_creeaza_inc_ret()
        self.__test_valideaza_inc_ret()
        self.__test_adauga_inc_ret_repo()
        self.__test_adauga_inc_ret_srv()
        self.__test_sterge_dupa_id_inc_ret_repo()
        self.__test_sterge_dupa_id_inc_ret_srv()
        self.__test_mod_inc_ret_repo()
        self.__test_mod_inc_ret_srv()
        self.__test_get_all_nr_inchirieri_carti()
        self.__test_get_nr_inchirieri_client()
        self.__test_get_top_clienti()
        print("sfarsit testare...")
