class Student(object):
    def __init__(self, stud_id, stud_name):
        self.__stud_id = stud_id
        self.__stud_name = stud_name

    def get_student_id(self):
        return self.__stud_id

    def get_student_name(self):
        return self.__stud_name

    def set_student_name(self, new_name):
        self.__stud_name = new_name

    def __eq__(self, other):
        return self.__stud_id == other.__stud_id and self.__stud_name == other.__stud_name

    def __str__(self):
        return f"Student ID: {self.__stud_id}, Student Name: {self.__stud_name}"
