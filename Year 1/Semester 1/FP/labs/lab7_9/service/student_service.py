from lab7_9.domain.student import Student


class StudentService(object):
    def __init__(self, valid_stud, stud_repo):
        self._valid_stud = valid_stud
        self._stud_repo = stud_repo

    def size(self):
        """
        Returns the number of students
        :return: integer
        """
        return len(self._stud_repo)

    def get_all_studs(self):
        """
        Returns all students
        :return:
        """
        return self._stud_repo.get_all_students()

    def find_stud_by_id(self, stud_id):
        """
        Returns the student with the given id
        :param stud_id: integer
        :return: Student if found, error otherwise
        """
        return self._stud_repo.find_by_id(stud_id)

    def add_student(self, stud_id, stud_name):
        """
        Adds a student
        :param stud_id: integer, unique
        :param stud_name: string, non-null
        :return:
        """
        student = Student(stud_id, stud_name)
        self._valid_stud.validate(student)
        self._stud_repo.add_student(student)

    def delete_student(self, stud_id):
        """
        Deletes a student
        :param stud_id: integer
        :return:
        """
        return self._stud_repo.delete_student(stud_id)

    def modify_student(self, stud_id, stud_name):
        """
        Modifies a student
        :param stud_id: integer
        :param stud_name: name that's going to be modified
        :return:
        """
        self._stud_repo.modify_student(stud_id, stud_name)

