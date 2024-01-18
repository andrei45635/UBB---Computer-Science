from lab7_9.exceptions.validator_exception import ValidatorException


class StudentValidator(object):
    """
    Validator pentru obiectul Student
    - Dacă ID-ul studentului este negativ, aruncă eroarea "Invalid student ID!"
    - Dacă numele studentului este vid sau conține caractere numerice, aruncă eroarea "Invalid student name!"
    """
    @staticmethod
    def validate(student):
        err = ""
        if student.get_student_id() < 0:
            err += "Invalid student ID!\n"
        if str(student.get_student_name()).isnumeric() or student.get_student_name() == " " or len(student.get_student_name()) == 0:
            err += "Invalid student name!\n"
        if len(err) > 0:
            raise ValidatorException(err)
