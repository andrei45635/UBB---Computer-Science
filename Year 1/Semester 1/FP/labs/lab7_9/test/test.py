import unittest

from lab7_9.domain.grade import Grade
from lab7_9.domain.student import Student
from lab7_9.domain.subject import Subject
from lab7_9.exceptions.repository_exception import RepositoryException
from lab7_9.exceptions.validator_exception import ValidatorException
from lab7_9.file_repo.student_file_repo import StudentFileRepo
from lab7_9.repo.grade_repo import GradeRepo
from lab7_9.repo.student_repo import StudentRepo
from lab7_9.repo.subject_repo import SubjectRepo
from lab7_9.service.grade_service import GradeService
from lab7_9.service.student_service import StudentService
from lab7_9.service.subject_service import SubjectService
from lab7_9.validators.grade_validator import GradeValidator
from lab7_9.validators.student_validator import StudentValidator
from lab7_9.validators.subject_validator import SubjectValidator


class TestPyUnit(unittest.TestCase):
    def setUp(self):
        pass

    def __test_create_empty_repo(self):
        filePath = "C:\\Users\\GIGABYTE\\OneDrive\\Desktop\\Facultate\\Semestrul 1 - Recuperare\\FP\\lab3\\lab7_9\\test\\test_students.txt"
        with open(filePath, "w") as f:
            f.write("")
        try:
            repo = StudentFileRepo(filePath)
        except Exception as ex:
            print(ex)
            return
        assert (repo.__len__() == 0)
        assert (len(repo) == 0)
        return repo

    def test_create_student(self):
        stud_id = 1
        stud_name = "Festa Robert"
        stud = Student(stud_id, stud_name)
        self.assertEqual(stud.get_student_id(), stud_id)
        self.assertEqual(stud.get_student_name(), stud_name)

    def test_create_subject(self):
        sub_id = 1
        sub_name = "Vidya"
        sub_prof = "Andrei Munteanu"
        subject = Subject(sub_id, sub_name, sub_prof)
        self.assertEqual(subject.get_subject_id(), sub_id)
        self.assertEqual(subject.get_subject_name(), sub_name)
        self.assertEqual(subject.get_subject_prof(), sub_prof)

    def test_create_grade(self):
        stud_id = 1
        sub_id = 1
        grade_id = 1
        mark = 9
        grade = Grade(grade_id, stud_id, sub_id, mark)
        self.assertEqual(grade.get_grade_id(), grade_id)
        self.assertEqual(grade.get_stud_id(), stud_id)
        self.assertEqual(grade.get_sub_id(), sub_id)
        self.assertEqual(grade.get_mark(), mark)

    def test_validate_student(self):
        stud_id = 1
        stud_name = "Festa Robert"
        student = Student(stud_id, stud_name)
        StudentValidator.validate(student)

        invalid_stud_id = -1
        invalid_stud_name = 123
        invalid_student = Student(invalid_stud_id, invalid_stud_name)

        try:
            StudentValidator.validate(invalid_student)
            assert False
        except ValidatorException as ve:
            self.assertEqual(str(ve), "Invalid student ID!\nInvalid student name!\n")

    def test_validate_subject(self):
        subject_id = 1
        subject_name = "Vidya"
        subject_prof = "Andrei Munteanu"
        subject = Subject(subject_id, subject_name, subject_prof)
        SubjectValidator.validate(subject)

        invalid_subject_id = -101
        invalid_subject_name = " "
        invalid_subject_prof = 123
        invalid_subject = Subject(invalid_subject_id, invalid_subject_name, invalid_subject_prof)

        try:
            SubjectValidator.validate(invalid_subject)
            assert False
        except ValidatorException as ve:
            self.assertEqual(str(ve), "Invalid subject ID!\nInvalid subject name!\nInvalid subject professor!\n")

    def test_validate_grade(self):
        grade_id = 1
        sub_id = 1
        stud_id = 1
        mark = 9
        grade = Grade(grade_id, stud_id, sub_id, mark)
        GradeValidator.validate(grade)

        invalid_grade_id = -1
        invalid_subject_id = -1
        invalid_stud_id = -1
        invalid_mark = 123
        invalid_grade = Grade(invalid_grade_id, invalid_stud_id, invalid_subject_id, invalid_mark)

        try:
            GradeValidator.validate(invalid_grade)
            assert False
        except ValidatorException as ve:
            self.assertEqual(str(ve), "Invalid grade ID!\nInvalid subject ID!\nInvalid student ID!\nInvalid mark!\n")

    def test_add_student_repo(self):
        repo = StudentRepo()
        assert(repo.__len__() == 0)
        stud_id = 1
        stud_name = "Festa Robert"
        student = Student(stud_id, stud_name)
        StudentValidator.validate(student)
        repo.add_student(student)
        self.assertEqual(repo.__len__(), 1)
        found_student = repo.find_by_id(stud_id)
        self.assertEqual(found_student.get_student_id(), stud_id)
        self.assertEqual(found_student.get_student_name(), stud_name)
        alt_name = "Nic Soldab"
        same_stud = Student(stud_id, alt_name)
        with self.assertRaises(RepositoryException) as re:
            repo.add_student(same_stud)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_delete_student_repo(self):
        repo = StudentRepo()
        self.assertEqual(repo.__len__(), 0)
        stud_id = 24
        stud_name = "Festa Robert"
        stud = Student(stud_id, stud_name)
        repo.add_student(stud)
        stud_id_2 = 25
        stud_name_2 = "Nic Soldab"
        stud_2 = Student(stud_id_2, stud_name_2)
        repo.add_student(stud_2)
        self.assertEqual(repo.__len__(), 2)
        repo.delete_student(24)
        self.assertEqual(repo.__len__(), 1)

    def test_modify_student_repo(self):
        repo = StudentRepo()
        self.assertEqual(repo.__len__(), 0)
        stud_id = 24
        stud_name = "Festa Robert"
        stud = Student(stud_id, stud_name)
        repo.add_student(stud)
        stud_id_2 = 25
        stud_name_2 = "Nic Soldab"
        stud_2 = Student(stud_id_2, stud_name_2)
        repo.add_student(stud_2)
        self.assertEqual(repo.__len__(), 2)
        repo.modify_student(24, "Festar Robert")
        self.assertEqual(repo.__len__(), 2)
        with self.assertRaises(RepositoryException) as re:
            repo.modify_student(28, "Soldabster")
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_find_by_id(self):
        valid = StudentValidator()
        repo = StudentRepo()
        srv = StudentService(valid, repo)
        self.assertEqual(srv.size(), 0)
        stud_id = 1
        stud_name = "Festa Robert"
        srv.add_student(stud_id, stud_name)
        stud_id_2 = 25
        stud_name_2 = "Nic Soldab"
        srv.add_student(stud_id_2, stud_name_2)
        self.assertEqual(srv.size(), 2)
        self.assertEqual(srv.size(), 2)
        srv.modify_student(25, "Nic Soldabster")
        self.assertEqual(srv.size(), 2)
        srv.find_stud_by_id(25)
        self.assertEqual(str(srv.find_stud_by_id(25)), "Student ID: 25, Student Name: Nic Soldabster")

    def test_add_student_service(self):
        valid = StudentValidator()
        repo = StudentRepo()
        srv = StudentService(valid, repo)
        self.assertEqual(srv.size(), 0)
        stud_id = 1
        stud_name = "Festa Robert"
        srv.add_student(stud_id, stud_name)
        self.assertEqual(srv.size(), 1)
        alt_name = "Nicolae Soldab"
        with self.assertRaises(RepositoryException) as re:
            srv.add_student(stud_id, alt_name)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)
        inv_stud_id = -24
        inv_name = " "
        with self.assertRaises(ValidatorException) as ve:
            srv.add_student(inv_stud_id, inv_name)
        exception = ve.exception
        self.assertEqual(exception, ve.exception)

    def test_delete_student_service(self):
        valid = StudentValidator()
        repo = StudentRepo()
        srv = StudentService(valid, repo)
        self.assertEqual(srv.size(), 0)
        stud_id = 1
        stud_name = "Festa Robert"
        srv.add_student(stud_id, stud_name)
        stud_id_2 = 25
        stud_name_2 = "Nic Soldab"
        srv.add_student(stud_id_2, stud_name_2)
        self.assertEqual(srv.size(), 2)
        srv.delete_student(1)
        self.assertEqual(srv.size(), 1)

    def test_modify_student_service(self):
        valid = StudentValidator()
        repo = StudentRepo()
        srv = StudentService(valid, repo)
        self.assertEqual(srv.size(), 0)
        stud_id = 1
        stud_name = "Festa Robert"
        srv.add_student(stud_id, stud_name)
        stud_id_2 = 25
        stud_name_2 = "Nic Soldab"
        srv.add_student(stud_id_2, stud_name_2)
        self.assertEqual(srv.size(), 2)
        self.assertEqual(srv.size(), 2)
        srv.modify_student(25, "Nic Soldabster")
        self.assertEqual(srv.size(), 2)
        with self.assertRaises(RepositoryException) as re:
            srv.modify_student(28, "Soldabster")
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_add_subject_repo(self):
        repo = SubjectRepo()
        assert (repo.__len__() == 0)
        sub_id = 1
        sub_name = "Vidya"
        sub_prof = "Andrei Munteanu"
        subject = Subject(sub_id, sub_name, sub_prof)
        SubjectValidator.validate(subject)
        repo.add_subject(subject)
        self.assertEqual(repo.__len__(), 1)
        found_subject = repo.find_by_id(sub_id)
        self.assertEqual(found_subject.get_subject_id(), sub_id)
        self.assertEqual(found_subject.get_subject_name(), sub_name)
        self.assertEqual(found_subject.get_subject_prof(), sub_prof)
        alt_name = "/v/"
        same_sub = Subject(sub_id, alt_name, sub_prof)
        with self.assertRaises(RepositoryException) as re:
            repo.add_subject(same_sub)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_add_subject_service(self):
        valid = SubjectValidator()
        repo = SubjectRepo()
        srv = SubjectService(valid, repo)
        self.assertEqual(srv.size(), 0)
        sub_id = 1
        sub_name = "Vidya"
        sub_prof = "Andrei Munteanu"
        srv.add_subject(sub_id, sub_name, sub_prof)
        self.assertEqual(srv.size(), 1)
        alt_name = "/v/"
        with self.assertRaises(RepositoryException) as re:
            srv.add_subject(sub_id, alt_name, sub_prof)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)
        inv_sub_id = -24
        inv_name = " "
        inv_prof = 125
        with self.assertRaises(ValidatorException) as ve:
            srv.add_subject(inv_sub_id, inv_name, inv_prof)
        exception = ve.exception
        self.assertEqual(exception, ve.exception)

    def test_delete_subject_repo(self):
        repo = SubjectRepo()
        self.assertEqual(repo.__len__(), 0)
        sub_id = 1
        sub_name = "Vidya"
        sub_prof = "Andrei Munteanu"
        subject = Subject(sub_id, sub_name, sub_prof)
        repo.add_subject(subject)
        sub_id_2 = 2
        sub_name_2 = "Stil"
        sub_prof_2 = "Nicolae Soldab"
        subject = Subject(sub_id_2, sub_name_2, sub_prof_2)
        repo.add_subject(subject)
        self.assertEqual(repo.__len__(), 2)
        repo.delete_subject(2)
        self.assertEqual(repo.__len__(), 1)

    def test_delete_subject_service(self):
        valid = SubjectValidator()
        repo = SubjectRepo()
        srv = SubjectService(valid, repo)
        self.assertEqual(srv.size(), 0)
        sub_id = 1
        sub_name = "Vidya"
        sub_prof = "Andrei Munteanu"
        srv.add_subject(sub_id, sub_name, sub_prof)
        self.assertEqual(srv.size(), 1)
        sub_id_2 = 2
        sub_name_2 = "Stil"
        sub_prof_2 = "Nicolae Soldab"
        srv.add_subject(sub_id_2, sub_name_2, sub_prof_2)
        self.assertEqual(srv.size(), 2)
        srv.delete_subject(1)
        self.assertEqual(srv.size(), 1)

    def test_modify_subject_repo(self):
        repo = SubjectRepo()
        self.assertEqual(repo.__len__(), 0)
        sub_id = 1
        sub_name = "Vidya"
        sub_prof = "Andrei Munteanu"
        subject = Subject(sub_id, sub_name, sub_prof)
        repo.add_subject(subject)
        sub_id_2 = 2
        sub_name_2 = "Stil"
        sub_prof_2 = "Nicolae Soldab"
        subject = Subject(sub_id_2, sub_name_2, sub_prof_2)
        repo.add_subject(subject)
        self.assertEqual(repo.__len__(), 2)
        repo.modify_subject(1, "/v/", "Andrei Munte")
        self.assertEqual(repo.__len__(), 2)
        with self.assertRaises(RepositoryException) as re:
            repo.modify_subject(28, "Soldabster", "Soldabino")
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_modify_subject_service(self):
        valid = SubjectValidator()
        repo = SubjectRepo()
        srv = SubjectService(valid, repo)
        self.assertEqual(srv.size(), 0)
        sub_id = 1
        sub_name = "Vidya"
        sub_prof = "Andrei Munteanu"
        srv.add_subject(sub_id, sub_name, sub_prof)
        self.assertEqual(srv.size(), 1)
        sub_id_2 = 2
        sub_name_2 = "Stil"
        sub_prof_2 = "Nicolae Soldab"
        srv.add_subject(sub_id_2, sub_name_2, sub_prof_2)
        self.assertEqual(srv.size(), 2)
        srv.modify_subject(2, "Smecherie", "Festar Soldab")
        self.assertEqual(srv.size(), 2)
        with self.assertRaises(RepositoryException) as re:
            srv.modify_subject(28, "Soldabster", "Soldabino")
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_find_subject_by_id(self):
        valid = SubjectValidator()
        repo = SubjectRepo()
        srv = SubjectService(valid, repo)
        self.assertEqual(srv.size(), 0)
        sub_id = 1
        sub_name = "Vidya"
        sub_prof = "Andrei Munteanu"
        srv.add_subject(sub_id, sub_name, sub_prof)
        self.assertEqual(srv.size(), 1)
        sub_id_2 = 2
        sub_name_2 = "Stil"
        sub_prof_2 = "Nicolae Soldab"
        srv.add_subject(sub_id_2, sub_name_2, sub_prof_2)
        self.assertEqual(str(srv.find_sub_by_id(2)), "Subject ID: 2, Subject Name: Stil, Professor: Nicolae Soldab")

    def test_add_grade_repo(self):
        repo = GradeRepo()
        assert (repo.__len__() == 0)
        grade_id = 1
        stud_id = 1
        sub_id = 1
        mark = 9
        grade = Grade(grade_id, stud_id, sub_id, mark)
        GradeValidator.validate(grade)
        repo.add_grade(grade)
        self.assertEqual(repo.__len__(), 1)
        found_grade = repo.find_by_id(grade_id)
        self.assertEqual(found_grade.get_grade_id(), grade_id)
        self.assertEqual(found_grade.get_stud_id(), stud_id)
        self.assertEqual(found_grade.get_sub_id(), sub_id)
        self.assertEqual(found_grade.get_mark(), mark)
        alt_mark = 7
        same_grade = Grade(grade_id, stud_id, sub_id, alt_mark)
        with self.assertRaises(RepositoryException) as re:
            repo.add_grade(same_grade)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_delete_grade_repo(self):
        repo = GradeRepo()
        self.assertEqual(repo.__len__(), 0)
        grade_id = 1
        stud_id = 24
        sub_id = 1
        mark = 9
        grade = Grade(grade_id, stud_id, sub_id, mark)
        repo.add_grade(grade)
        grade_id_2 = 2
        stud_id_2 = 25
        sub_id_2 = 2
        mark_2 = 10
        grade_2 = Grade(grade_id_2, stud_id_2, sub_id_2, mark_2)
        repo.add_grade(grade_2)
        self.assertEqual(repo.__len__(), 2)
        repo.delete_grade(2)
        self.assertEqual(repo.__len__(), 1)

    def test_modify_grade_repo(self):
        repo = GradeRepo()
        self.assertEqual(repo.__len__(), 0)
        grade_id = 1
        stud_id = 24
        sub_id = 1
        mark = 9
        grade = Grade(grade_id, stud_id, sub_id, mark)
        repo.add_grade(grade)
        grade_id_2 = 2
        stud_id_2 = 25
        sub_id_2 = 2
        mark_2 = 10
        grade_2 = Grade(grade_id_2, stud_id_2, sub_id_2, mark_2)
        repo.add_grade(grade_2)
        self.assertEqual(repo.__len__(), 2)
        repo.modify_grade(1, 10)
        self.assertEqual(repo.__len__(), 2)
        with self.assertRaises(RepositoryException) as re:
            repo.modify_grade(28, 9)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_add_grade_service(self):
        valid = GradeValidator()
        repo = GradeRepo()
        repo_stud = StudentRepo()
        repo_sub = SubjectRepo()
        srv = GradeService(valid, repo, repo_stud, repo_sub)
        self.assertEqual(srv.size(), 0)
        grade_id = 1
        stud_id = 1
        sub_id = 1
        mark = 9
        srv.add_grade(grade_id, stud_id, sub_id, mark)
        self.assertEqual(srv.size(), 1)
        alt_mark = 9
        with self.assertRaises(RepositoryException) as re:
            srv.add_grade(grade_id, stud_id, sub_id, alt_mark)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)
        inv_grade_id = -1
        inv_stud_id = -2
        inv_sub_id = -24
        inv_mark = 1234
        with self.assertRaises(ValidatorException) as ve:
            srv.add_grade(inv_grade_id, inv_stud_id, inv_sub_id, inv_mark)
        exception = ve.exception
        self.assertEqual(exception, ve.exception)

    def test_delete_grade_service(self):
        valid = GradeValidator()
        repo = GradeRepo()
        repo_stud = StudentRepo()
        repo_sub = SubjectRepo()
        srv = GradeService(valid, repo, repo_stud, repo_sub)
        self.assertEqual(srv.size(), 0)
        grade_id = 1
        stud_id = 1
        sub_id = 1
        mark = 9
        srv.add_grade(grade_id, stud_id, sub_id, mark)
        self.assertEqual(srv.size(), 1)
        grade_id_2 = 2
        stud_id_2 = 2
        sub_id_2 = 2
        mark_2 = 9
        srv.add_grade(grade_id_2, stud_id_2, sub_id_2, mark_2)
        self.assertEqual(srv.size(), 2)
        srv.delete_grade(1)
        self.assertEqual(srv.size(), 1)

    def test_modify_grade_service(self):
        valid = GradeValidator()
        repo = GradeRepo()
        repo_stud = StudentRepo()
        repo_sub = SubjectRepo()
        srv = GradeService(valid, repo, repo_stud, repo_sub)
        self.assertEqual(srv.size(), 0)
        grade_id = 1
        stud_id = 1
        sub_id = 1
        mark = 9
        srv.add_grade(grade_id, stud_id, sub_id, mark)
        self.assertEqual(srv.size(), 1)
        grade_id_2 = 2
        stud_id_2 = 2
        sub_id_2 = 2
        mark_2 = 9
        srv.add_grade(grade_id_2, stud_id_2, sub_id_2, mark_2)
        self.assertEqual(srv.size(), 2)
        srv.modify_grade(2, 8)
        self.assertEqual(srv.size(), 2)
        with self.assertRaises(RepositoryException) as re:
            srv.modify_grade(28, 5)
        exceptions = re.exception
        self.assertEqual(exceptions, re.exception)

    def test_find_grade_by_id_service(self):
        valid = GradeValidator()
        repo = GradeRepo()
        repo_stud = StudentRepo()
        repo_sub = SubjectRepo()
        srv = GradeService(valid, repo, repo_stud, repo_sub)
        self.assertEqual(srv.size(), 0)
        grade_id = 1
        stud_id = 1
        sub_id = 1
        mark = 9
        srv.add_grade(grade_id, stud_id, sub_id, mark)
        self.assertEqual(srv.size(), 1)
        grade_id_2 = 2
        stud_id_2 = 2
        sub_id_2 = 2
        mark_2 = 9
        srv.add_grade(grade_id_2, stud_id_2, sub_id_2, mark_2)
        self.assertEqual(srv.size(), 2)
        self.assertEqual(str(srv.find_grade_by_id(2)), "Grade ID: 2, Student ID: 2, Subject ID: 2, Mark: 9")

    def test_add_student_file_repo(self):
        repo = self.__test_create_empty_repo()
        assert (repo.__len__() == 0)
        stud_id = 1
        stud_name = "Festa Robert"
        student = Student(stud_id, stud_name)
        repo.add_student(student)
        assert (repo.__len__() == 1)

    def test_sorted_by_name(self):
        stud_repo = StudentRepo()
        sub_repo = SubjectRepo()
        grade_repo = GradeRepo()
        srv_grade = GradeService(GradeValidator(), grade_repo, stud_repo, sub_repo)
        stud1 = Student(1, "Festar")
        stud2 = Student(2, "Nic")
        stud3 = Student(3, "Munte")
        stud_repo.add_student(stud1)
        stud_repo.add_student(stud2)
        stud_repo.add_student(stud3)
        sub1 = Subject(1, "Vidya", "Nyesteban")
        sub_repo.add_subject(sub1)
        grade1 = Grade(1, 1, 1, 10)
        grade2 = Grade(2, 1, 1, 8)
        grade3 = Grade(3, 1, 1, 7)
        grade4 = Grade(4, 2, 1, 10)
        grade5 = Grade(5, 3, 1, 9)
        grade6 = Grade(6, 2, 1, 10)
        grade_repo.add_grade(grade1)
        grade_repo.add_grade(grade2)
        grade_repo.add_grade(grade3)
        grade_repo.add_grade(grade4)
        grade_repo.add_grade(grade5)
        grade_repo.add_grade(grade6)
        res = srv_grade.get_students_with_grades_alphabetically("Vidya")
        assert(res.__len__() == 3)
        assert(res[0].get_student_name() == "Festar")

    def test_sorted_by_average(self):
        stud_repo = StudentRepo()
        sub_repo = SubjectRepo()
        grade_repo = GradeRepo()
        srv_grade = GradeService(GradeValidator(), grade_repo, stud_repo, sub_repo)
        stud1 = Student(1, "Festar")
        stud2 = Student(2, "Nic")
        stud3 = Student(3, "Munte")
        stud_repo.add_student(stud1)
        stud_repo.add_student(stud2)
        stud_repo.add_student(stud3)
        sub1 = Subject(1, "Vidya", "Nyesteban")
        sub_repo.add_subject(sub1)
        grade1 = Grade(1, 1, 1, 10)
        grade2 = Grade(2, 1, 1, 8)
        grade3 = Grade(3, 1, 1, 7)
        grade4 = Grade(4, 2, 1, 10)
        grade5 = Grade(5, 3, 1, 9)
        grade6 = Grade(6, 2, 1, 10)
        grade_repo.add_grade(grade1)
        grade_repo.add_grade(grade2)
        grade_repo.add_grade(grade3)
        grade_repo.add_grade(grade4)
        grade_repo.add_grade(grade5)
        grade_repo.add_grade(grade6)
        res = srv_grade.get_students_with_grades_by_marks("Vidya")
        assert(res.__len__() == 3)
        assert(res[0].get_student_name() == "Festar")

    def test_top_twenty(self):
        stud_repo = StudentRepo()
        sub_repo = SubjectRepo()
        grade_repo = GradeRepo()
        srv_grade = GradeService(GradeValidator(), grade_repo, stud_repo, sub_repo)
        stud1 = Student(1, "Festar")
        stud2 = Student(2, "Nic")
        stud3 = Student(3, "Munte")
        stud_repo.add_student(stud1)
        stud_repo.add_student(stud2)
        stud_repo.add_student(stud3)
        sub1 = Subject(1, "Vidya", "Nyesteban")
        sub_repo.add_subject(sub1)
        grade1 = Grade(1, 1, 1, 10)
        grade2 = Grade(2, 1, 1, 8)
        grade3 = Grade(3, 1, 1, 7)
        grade4 = Grade(4, 2, 1, 10)
        grade5 = Grade(5, 3, 1, 9)
        grade6 = Grade(6, 2, 1, 10)
        grade_repo.add_grade(grade1)
        grade_repo.add_grade(grade2)
        grade_repo.add_grade(grade3)
        grade_repo.add_grade(grade4)
        grade_repo.add_grade(grade5)
        grade_repo.add_grade(grade6)
        res = srv_grade.top_twenty_students()
        assert(res.__len__() == 0)

    def run_all_tests(self):
        print("Loading...")
        self.test_create_student()
        self.test_validate_student()
        self.test_create_subject()
        self.test_validate_subject()
        self.test_add_student_repo()
        self.test_delete_student_repo()
        self.test_modify_student_repo()
        self.test_add_student_service()
        self.test_delete_student_service()
        self.test_modify_student_service()
        self.test_find_by_id()
        self.test_add_subject_repo()
        self.test_add_subject_service()
        self.test_delete_subject_repo()
        self.test_delete_subject_service()
        self.test_modify_subject_repo()
        self.test_modify_subject_service()
        self.test_find_subject_by_id()
        self.test_create_grade()
        self.test_validate_grade()
        self.test_add_grade_repo()
        self.test_delete_grade_repo()
        self.test_modify_grade_repo()
        self.test_add_grade_service()
        self.test_delete_grade_service()
        self.test_modify_grade_service()
        self.test_find_grade_by_id_service()
        self.test_add_student_file_repo()
        self.test_sorted_by_name()
        self.test_sorted_by_name()
        self.test_top_twenty()
        print("Passed all tests!")
