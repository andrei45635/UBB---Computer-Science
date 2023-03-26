from erori.exceptii import ValidationError


class ValidatorIngredient(object):

    def valideaza(self, ing):
        errors = ""
        if ing.get_id_ing() < 0:
            errors += "id invalid!\n"
        if ing.get_nume() == "":
            errors += "nume invalid!\n"
        if ing.get_pret_unitate() < 0:
            errors += "cantitate invalida!\n"
        if len(errors) > 0:
            raise ValidationError(errors)


class ValidatorReteta(object):
    pass
