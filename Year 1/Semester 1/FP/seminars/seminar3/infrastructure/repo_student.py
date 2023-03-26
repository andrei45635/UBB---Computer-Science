from exceptions.erori import RepoError
from domain.student import egali_studenti


def adauga_student_lista(l,student):
    for _student in l:
        if egali_studenti(_student,student):
            raise RepoError("student existent!\n")
    l.append(student)