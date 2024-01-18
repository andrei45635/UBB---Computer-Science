from lab7_9.domain.grade import Grade
from lab7_9.exceptions.repository_exception import RepositoryException
from lab7_9.repo.grade_repo import GradeRepo


class GradeFileRepo(GradeRepo):
    def __init__(self, filepath):
        GradeRepo.__init__(self)
        self.__filepath = filepath

    def read_from_file(self):
        """
        Reads grades from a file
        :return:
        """
        self._grades = []
        with open(self.__filepath, "r") as f:
            lines = f.read()
            lines_arr = [lines]
            for line in lines_arr:
                for grade in line.splitlines():
                    grade_id = grade.split(",")[0]
                    grade_stud_id = grade.split(",")[1]
                    grade_sub_id = grade.split(",")[2]
                    grade_mark = grade.split(",")[3]
                    grade = Grade(grade_id, grade_stud_id, grade_sub_id, grade_mark)
                    self._grades.append(grade)

    def append_to_file(self, grade):
        """
        Writes a grade to a file
        :param grade: Grade
        :return:
        """
        with open(self.__filepath, "a") as f:
            f.write(
                str(grade.get_grade_id()) + "," + str(grade.get_stud_id()) + "," + str(grade.get_sub_id()) + "," + str(
                    grade.get_mark()) + "\n")

    def write_all_to_file(self):
        """
        Writes a list of grades to the file
        :return:
        """
        with open(self.__filepath, "w") as f:
            for grade in self._grades:
                f.write(str(grade.get_grade_id()) + "," + str(grade.get_stud_id()) + "," + str(
                    grade.get_sub_id()) + "," + str(grade.get_mark()) + "\n")

    def add_grade(self, grade):
        """
        Overriden method from GradeRepo
        Adds a grade
        :param grade: Grade
        :return:
        """
        self.read_from_file()
        GradeRepo.add_grade(self, grade)
        self.append_to_file(grade)

    def find_by_id(self, grade_id):
        """
        Overridden method from GradeRepo
        Finds a grade given an id
        :param grade_id: integer
        :return:
        """
        self.read_from_file()
        try:
            return GradeRepo.find_by_id(self, grade_id)
        except RepositoryException:
            raise RepositoryException("Grade already exists!\n")

    def get_all_grades(self):
        """
        Gettter for all the grades
        :return:
        """
        self.read_from_file()
        return GradeRepo.get_all_grades(self)

    def __len__(self):
        """
        Overrides __len__
        :return:
        """
        self.read_from_file()
        return GradeRepo.__len__(self)

    def modify_grade(self, option1, option2):
        """
        Overridden method from GradeRepo
        Modifies a grade
        :param option1: integer, grade's ID
        :param option2: integer, mark
        :return:
        """
        self.read_from_file()
        GradeRepo.modify_grade(self, option1, option2)
        self.write_all_to_file()

    def delete_grade(self, user_input):
        """
        Overridden method from GradeRepo
        Removes a grade
        :param user_input: integer, grade's ID
        :return:
        """
        self.read_from_file()
        GradeRepo.delete_grade(self, user_input)
        self.write_all_to_file()

    def repo_find_by_id_recursively(self, id_carte, n):
        self.read_from_file()
        try:
            return GradeRepo.find_by_id_recursively(self, id_carte, n)
        except RepositoryException as re:
            raise RepositoryException("Couldn't find the grade\n")

    def repo_delete_grade_recursively(self, grade_id, i):
        self.read_from_file()
        try:
            GradeRepo.delete_grade_recursively(self, grade_id, i)
        except RepositoryException as re:
            raise RepositoryException("Couldn't find the grade\n")
        self.write_all_to_file()
