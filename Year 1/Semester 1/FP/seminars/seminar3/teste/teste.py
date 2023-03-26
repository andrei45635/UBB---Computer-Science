from domain.student import creeaza_student, get_id_stud, get_nume, get_val
from validation.valid_student import valideaza_student
from exceptions.erori import ValidError, RepoError
from infrastructure.repo_student import adauga_student_lista
from business.service_studenti import srv_adauga_lista

def test_creeaza_student():
    id_stud = 23
    nume = "Jordan"
    val = 9000.1
    student = creeaza_student(id_stud, nume, val)
    assert (get_id_stud(student) == id_stud)
    assert (get_nume(student) == nume)
    assert (abs(get_val(student) - val) < 0.0001)


def test_valideaza_student():
    id_stud = 23
    nume = "Jordan"
    val = 9000.1
    student = creeaza_student(id_stud, nume, val)
    valideaza_student(student)
    id_stud_rau = -23
    nume_rau = ""
    val_rau = -9001
    student_id_rau = creeaza_student(id_stud_rau, nume, val)
    student_rau = creeaza_student(id_stud_rau,nume_rau,val_rau)
    try:
        valideaza_student(student_id_rau)
        assert False
    except ValidError as ve:
        assert (str(ve) == "student id invalid!\n")
    try:
        valideaza_student(student_rau)
        assert False
    except ValidError as ve:
        assert (str(ve) == "student id invalid!\nnume student invalid!\nvaloare student gresita!\n")

def test_adauga_student_lista():
    id_stud = 23
    nume = "Jordan"
    val = 9000.1
    student = creeaza_student(id_stud, nume, val)
    l = []
    adauga_student_lista(l,student)
    assert len(l) == 1
    assert (get_id_stud(student) == get_id_stud(l[0]))
    assert (get_nume(student) == get_nume(l[0]))
    assert (abs(get_val(student) - get_val(l[0])) < 0.0001)
    student_same_id = creeaza_student(id_stud, "Gigi", 347.78)
    try:
        adauga_student_lista(l,student_same_id)
        assert False
    except RepoError as re:
        assert(str(re) == "student existent!\n")


def test_srv_adauga_lista():
    l = []
    id_stud = 23
    nume = "Jordan"
    val = 9000.1
    srv_adauga_lista(l,id_stud,nume, val)

def run_teste():
    print("beginning teste...")
    test_creeaza_student()
    test_valideaza_student()
    test_adauga_student_lista()
    test_srv_adauga_lista()
    print("finished teste")
