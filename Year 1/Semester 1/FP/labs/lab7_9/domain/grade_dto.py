class GradeDTO(object):
    def __init__(self, grade_id, stud_id, sub_id, mark):
        self.__grade_id = grade_id
        self.__stud_id = stud_id
        self.__sub_id = sub_id
        self.__mark = mark
        self.__stud = None
        self.__sub = None

    def get_grade_id(self):
        return self.__grade_id

    def get_stud_id(self):
        return self.__stud_id

    def get_sub_id(self):
        return self.__sub_id

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        self.__mark = mark

    def get_sub(self):
        return self.__sub

    def set_sub(self, new_sub):
        self.__sub = new_sub

    def get_stud(self):
        return self.__stud

    def set_stud(self, new_stud):
        self.__stud = new_stud

    def __str__(self):
        return str(self.get_mark())


class StudentGradesDTO(object):
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_student_name(self):
        return self.__name

    def get_marks(self):
        grades = []
        for _m in self.__marks:
            grades.append(int(_m.get_mark()))
        return grades

    def __str__(self):
        st = str(self.__name) + ":"
        for mark in self.__marks:
            st += str(mark) + " "
        return str(st)


class StudentAveragesDTO(object):
    def __init__(self, name, average):
        self.__name = name
        self.__average = average

    def get_average(self):
        return self.__average

    def __str__(self):
        st = str(self.__name) + ":" + str(self.__average)
        return str(st)


class PopularSubjectsDTO(object):
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def __str__(self):
        st = str(self.__name) + ": "
        for m in self.__marks:
            st += str(m) + " "
        return st


