from validare.validation import ValidatorCarte, ValidatorClient, ValidatorIncRet
from infrastructure.repository import RepoCarti, RepoClienti, RepoIncRet, FileRepoCarti, FileRepoClienti,FileRepoIncRet
from business.servicii import ServiceCarte, ServiceClient, ServiceIncRet
from prezentare.ui import Consola
from testing.testare import Teste

if __name__ == '__main__':
    valid_carte = ValidatorCarte()
    valid_client = ValidatorClient()
    valid_inc_ret = ValidatorIncRet()

    #repo_carti = RepoCarti()
    repo_carti = FileRepoCarti("carti.txt")
    #repo_clienti = RepoClienti()
    repo_clienti = FileRepoClienti("clienti.txt")
    #repo_inc_ret = RepoIncRet()
    repo_inc_ret = FileRepoIncRet("incret.txt")

    srv_carte = ServiceCarte(valid_carte, repo_carti)
    srv_client = ServiceClient(valid_client, repo_clienti)
    srv_inc_ret = ServiceIncRet(valid_inc_ret, repo_inc_ret, repo_carti, repo_clienti)

    ui = Consola(srv_carte, srv_client, srv_inc_ret)

    teste = Teste()
    teste.run_all_tests()

    ui.run()
