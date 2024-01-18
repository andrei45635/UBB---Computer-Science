from lab7_9.exceptions.validator_exception import ValidatorException


class GradeValidator(object):
    """
    Validator pentru obiectul Grade
    - Dacă ID-ul studentului este negativ, aruncă eroarea "Invalid student ID!"
    - Dacă ID-ul disciplinei este negativ, aruncă eroarea "Invalid subject ID!"
    - Dacă ID-ul notei este negativ, aruncă eroarea "Invalid grade ID!"
    - Dacă nota este negativă sau mai mare ca 10, aruncă eroarea "Invalid mark!"
    """
    @staticmethod
    def validate(grade):
        err = ""
        if grade.get_grade_id() < 0:
            err += "Invalid grade ID!\n"
        if grade.get_sub_id() < 0:
            err += "Invalid subject ID!\n"
        if grade.get_stud_id() < 0:
            err += "Invalid student ID!\n"
        if grade.get_mark() < 0 or grade.get_mark() > 10:
            err += "Invalid mark!\n"
        if len(err) > 0:
            raise ValidatorException(err)
