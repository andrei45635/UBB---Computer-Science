from lab7_9.domain.student import Student
from lab7_9.exceptions.repository_exception import RepositoryException
from lab7_9.repo.student_repo import StudentRepo


class StudentFileRepo(StudentRepo):
    def __init__(self, filepath):
        StudentRepo.__init__(self)
        self.__filepath = filepath

    def read_from_file(self):
        """
        Reads students from a file
        :return:
        """
        self._students = []
        with open(self.__filepath, "r") as f:
            lines = f.read()
            lines_arr = [lines]
            for line in lines_arr:
                for stud in line.splitlines():
                    stud_id = stud.split(",")[0]
                    stud_name = stud.split(",")[1]
                    student = Student(stud_id, stud_name)
                    self._students.append(student)

    def append_to_file(self, student):
        """
        Writes a student to a file
        :param student: Student
        :return:
        """
        with open(self.__filepath, "a") as f:
            f.write(str(student.get_student_id()) + "," + str(student.get_student_name()) + "\n")

    def write_all_to_file(self):
        """
        Writes a list of students to the file
        :return:
        """
        with open(self.__filepath, "w") as f:
            for student in self._students:
                f.write(str(student.get_student_id()) + "," + str(student.get_student_name()) + "\n")

    def add_student(self, student):
        """
        Overriden method from StudentRepo
        Adds a student
        :param student: Student
        :return:
        """
        self.read_from_file()
        StudentRepo.add_student(self, student)
        self.append_to_file(student)

    def find_by_id(self, stud_id):
        """
        Overridden method from StudentRepo
        Finds a student given an id
        :param stud_id: integer
        :return:
        """
        self.read_from_file()
        try:
            return StudentRepo.find_by_id(self, stud_id)
        except RepositoryException:
            raise RepositoryException("Student already exists!\n")

    def get_all_students(self):
        """
        Gettter for all the students
        :return:
        """
        self.read_from_file()
        return StudentRepo.get_all_students(self)

    def __len__(self):
        """
        Overrides __len__
        :return:
        """
        self.read_from_file()
        return StudentRepo.__len__(self)

    def modify_student(self, option1, option2):
        """
        Overridden method from StudentRepo
        Modifies a student
        :param option1: integer, student's ID
        :param option2: string, student's Name
        :return:
        """
        self.read_from_file()
        StudentRepo.modify_student(self, option1, option2)
        self.write_all_to_file()

    def delete_student(self, user_input):
        """
        Overridden method from StudentRepo
        Removes a student
        :param user_input: integer, student's ID
        :return:
        """
        self.read_from_file()
        StudentRepo.delete_student(self, user_input)
        self.write_all_to_file()
