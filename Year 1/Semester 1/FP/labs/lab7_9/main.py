from lab7_9.file_repo.grade_file_repo import GradeFileRepo
from lab7_9.file_repo.student_file_repo import StudentFileRepo
from lab7_9.file_repo.subject_file_repo import SubjectFileRepo
from lab7_9.repo.grade_repo import GradeRepo
from lab7_9.repo.student_repo import StudentRepo
from lab7_9.repo.subject_repo import SubjectRepo
from lab7_9.service.grade_service import GradeService
from lab7_9.service.student_service import StudentService
from lab7_9.service.subject_service import SubjectService
from lab7_9.test.test import TestPyUnit
from lab7_9.ui.ui import Console
from lab7_9.validators.grade_validator import GradeValidator
from lab7_9.validators.student_validator import StudentValidator
from lab7_9.validators.subject_validator import SubjectValidator


def declarations(valid_stud, repo_stud, valid_sub, repo_sub, valid_grade, repo_grade):
    srv_stud = StudentService(valid_stud, repo_stud)
    srv_sub = SubjectService(valid_sub, repo_sub)
    srv_grade = GradeService(valid_grade, repo_grade, repo_stud, repo_sub)

    test = TestPyUnit()
    test.run_all_tests()

    ui = Console(srv_stud, srv_sub, srv_grade)
    ui.run()


if __name__ == '__main__':
    valid_stud = StudentValidator()
    valid_sub = SubjectValidator()
    valid_grade = GradeValidator()

    type_of_repo = int(input("Input the type of repo you need (0 for memory, 1 for file): "))
    if type_of_repo == 0:
        repo_stud = StudentRepo()
        repo_sub = SubjectRepo()
        repo_grade = GradeRepo()
        declarations(valid_stud, repo_stud, valid_sub, repo_sub, valid_grade, repo_grade)
    elif type_of_repo == 1:
        repo_stud = StudentFileRepo("C:\\Users\\GIGABYTE\\OneDrive\\Desktop\\Facultate\\Semestrul 1 - Recuperare\\FP\\lab3\\lab7_9\\resources\\students.txt")
        repo_sub = SubjectFileRepo("C:\\Users\\GIGABYTE\\OneDrive\\Desktop\\Facultate\\Semestrul 1 - Recuperare\\FP\\lab3\\lab7_9\\resources\\subjects.txt")
        repo_grade = GradeFileRepo("C:\\Users\\GIGABYTE\\OneDrive\\Desktop\\Facultate\\Semestrul 1 - Recuperare\\FP\\lab3\\lab7_9\\resources\\grades.txt")
        declarations(valid_stud, repo_stud, valid_sub, repo_sub, valid_grade, repo_grade)
