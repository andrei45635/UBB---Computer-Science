def creeaza_student(id_stud, nume, val):
    return [id_stud, nume, val]


def get_id_stud(student):
    return student[0]


def get_nume(student):
    return student[1]


def get_val(student):
    return student[2]


def egali_studenti(s0,s1):
    return get_id_stud(s0) == get_id_stud(s1)


def to_str_stud(student):
    return str(student[0] + ":" + student[1] + ":" + student[2])
