from lab7_9.exceptions.validator_exception import ValidatorException


class SubjectValidator(object):
    """
     Validator pentru obiectul Subject
    - Dacă ID-ul materiei este negativ, aruncă eroarea "Invalid subject ID!"
    - Dacă numele materiei este vid sau conține numere, aruncă eroarea "Invalid subject name!"
    - Dacă numele profesorului materiei este vid sau conține numere, aruncă eroarea "Invalid subject professor!"
    """
    @staticmethod
    def validate(subject):
        err = ""
        if subject.get_subject_id() < 0:
            err += "Invalid subject ID!\n"
        if str(subject.get_subject_name()).isnumeric() or subject.get_subject_name() == " " or len(subject.get_subject_name()) == 0:
            err += "Invalid subject name!\n"
        if str(subject.get_subject_prof()).isnumeric() or subject.get_subject_prof() == " " or len(subject.get_subject_prof()) == 0:
            err += "Invalid subject professor!\n"
        if len(err) > 0:
            raise ValidatorException(err)
