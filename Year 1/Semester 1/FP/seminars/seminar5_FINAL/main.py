from prezentare.user_interface import Consola
from business.servicii import ServiceIngrediente, ServiceRetete
from validare.validatori import ValidatorIngredient, ValidatorReteta
from infrastructure.repository import RepoIngrediente, RepoRetete
from testing.teste import Teste

if __name__ == '__main__':
    validator_ingredient = ValidatorIngredient()
    validator_reteta = ValidatorReteta()
    validator_ingrediente_reteta = ValidatorIngredienteReteta()
    
    repo_ingrediente = RepoIngrediente()
    repo_retete = RepoRetete()
    repo_ingrediente_reteta = RepoIngredienteReteta()

    srv_ingrediente = ServiceIngrediente(validator_ingredient,repo_ingrediente)
    srv_retete = ServiceRetete(validator_reteta,repo_retete)
    srv_ingrediente_reteta = ServiceIngredienteReteta(validator_ingrediente_reteta,repo_ingrediente,repo_retete,repo_ingrediente_reteta)

    ui = Consola(srv_ingrediente, srv_retete,srv_ingrediente_reteta)

    teste = Teste()
    teste.run_all_tests()

    ui.run()