from lab7_9.exceptions.repository_exception import RepositoryException


class StudentRepo(object):
    def __init__(self):
        self._students = []

    def __len__(self):
        return len(self._students)

    def get_all_students(self):
        """
        Gets all the students
        :return: List of students
        """
        return self._students

    def find_by_id(self, stud_id):
        """
        Returns the student with the given id
        :param stud_id: integer
        :return: Student or error if a student with the given id doesn't exist
        """
        not_found = True
        for _stud in self._students:
            if _stud.get_student_id() == stud_id:
                return _stud
        if not_found:
            raise RepositoryException("Student doesn't exist!\n")

    def add_student(self, student):
        """
        Validates a student object and adds it to the repo
        :param student: Student
        :return: Error thrown if the student already exists
        """
        for _student in self._students:
            if _student.get_student_id() == student.get_student_id():
                raise RepositoryException("Student already exists!\n")
        self._students.append(student)

    def delete_student(self, stud_id):
        """
        Removes a student that matches the given id
        :param stud_id: integer
        :return: List with the student deleted
        """
        all_studs = self._students
        all_studs[:] = [_stud for _stud in self._students if not _stud.get_student_id() == stud_id]
        return all_studs

    def modify_student(self, stud_id, stud_name):
        """
        Modifies a student's name
        :param stud_id: integer
        :param stud_name: string
        :return: Error if the student doesn't exist
        """
        not_found = True
        for _stud in self._students:
            if _stud.get_student_id() == stud_id:
                not_found = False
                _stud.set_student_name(stud_name)
        if not_found:
            raise RepositoryException("Student doesn't exist!\n")

