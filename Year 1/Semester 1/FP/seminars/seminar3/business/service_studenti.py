from domain.student import creeaza_student
from infrastructure.repo_student import adauga_student_lista
from validation.valid_student import valideaza_student


def srv_adauga_lista(l,id_stud,nume,val):
    student = creeaza_student(id_stud,nume,val)
    adauga_student_lista(l,student)
    valideaza_student(student)