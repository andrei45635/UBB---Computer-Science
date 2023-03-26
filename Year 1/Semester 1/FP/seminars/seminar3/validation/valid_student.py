from domain.student import get_id_stud, get_nume, get_val
from exceptions.erori import ValidError


def valideaza_student(student):
    err = ""
    if get_id_stud(student) < 0:
        err += "student id invalid!\n"
    if get_nume(student) == "":
        err += "nume student invalid!\n"
    if get_val(student) < 0:
        err += "valoare student gresita!\n"
    if len(err) > 0:
        raise ValidError(err)