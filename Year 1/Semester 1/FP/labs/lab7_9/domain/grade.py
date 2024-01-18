class Grade(object):
    def __init__(self, grade_id, stud_id, sub_id, mark):
        self.__grade_id = grade_id
        self.__stud_id = stud_id
        self.__sub_id = sub_id
        self.__mark = mark

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

    def __str__(self):
        return f"Grade ID: {self.__grade_id}, Student ID: {self.__stud_id}, Subject ID: {self.__sub_id}, Mark: {self.__mark}"
