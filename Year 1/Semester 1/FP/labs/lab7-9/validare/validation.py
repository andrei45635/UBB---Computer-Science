from erori.exceptii import ValidationError


class ValidatorCarte(object):
    """
    validator pentru obiectul Carte
    -daca id-ul cartii este negativ, atunci arunca eroarea "id invalid!\n"
    -daca titlul cartii este vid, atunci arunca eroarea "titlu invalid!\n"
    -daca descrierea si autorul sunt vide si/sau sunt numerice, atunci arunca erorile
    -                                                          "descriere invalida!\n" si "autor invalid!\n"
    """

    def valideaza(self, carte):
        err = ""
        if carte.get_id_carte() < 0:
            err += "id invalid!\n"
        if carte.get_titlu() == " ":
            err += "titlu invalid!\n"
        if carte.get_desc() == " " or str(carte.get_desc()).isnumeric():
            err += "descriere invalida!\n"
        if carte.get_autor() == " " or str(carte.get_autor()).isnumeric():
            err += "autor invalid!\n"
        if len(err) > 0:
            raise ValidationError(err)


class ValidatorClient(object):
    """
     validator pentru obiectul Client
    -daca id-ul clientului este negativ, atunci arunca eroarea "id invalid!\n"
    -daca numele clientului este vid si/sau este numeric, atunci arunca eroarea "nume invalid!\n"
    -daca cnp-ul clientului este negativ, atunci arunca eroarea "cnp invalid!\n"
    """

    def valideaza(self, client):
        errs = ""
        if client.get_id_client() < 0:
            errs += "id invalid!\n"
        if client.get_nume() == " " or str(client.get_nume()).isnumeric():
            errs += "nume invalid!\n"
        if client.get_cnp() < 0:
            errs += "cnp invalid!\n"
        if len(errs) > 0:
            raise ValidationError(errs)


class ValidatorIncRet(object):
    def valideaza(self, inc_ret):
        errors = ""
        if inc_ret.get_id_inc_ret() < 0:
            errors += "id inchiriere_returnare invalid!\n"
        if inc_ret.get_id_carte_inc_ret() < 0:
            errors += "id carte invalid!\n"
        if inc_ret.get_id_client_inc_ret() < 0:
            errors += "id client invalid!\n"
        if inc_ret.get_durata() < 0:
            errors += "durata invalida!\n"
        if len(errors) > 0:
            raise ValidationError(errors)

    def valideaza_dto(self, inc_ret):
        errors = ""
        if inc_ret.get_id_inc_ret() < 0:
            errors += "id inchiriere_returnare invalid!\n"
        if inc_ret.get_id_carte() < 0:
            errors += "id carte invalid!\n"
        if inc_ret.get_id_client() < 0:
            errors += "id client invalid!\n"
        if inc_ret.get_durata() < 0:
            errors += "durata invalida!\n"
        if len(errors) > 0:
            raise ValidationError(errors)