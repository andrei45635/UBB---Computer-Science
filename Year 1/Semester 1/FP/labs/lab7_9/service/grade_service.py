from lab7_9.domain.grade import Grade
from lab7_9.domain.grade_dto import GradeDTO, StudentGradesDTO, StudentAveragesDTO, PopularSubjectsDTO
from lab7_9.utils.sorting_algorithms import bubble_sort, shell_sort


class GradeService(object):
    def __init__(self, valid_grade, grade_repo, stud_repo, sub_repo):
        self._valid_grade = valid_grade
        self._grade_repo = grade_repo
        self._stud_repo = stud_repo
        self._sub_repo = sub_repo

    def size(self):
        """
        Returns the number of grades
        :return: integer
        """
        return len(self._grade_repo)

    def get_all_grades(self):
        """
        Returns all grades
        :return:
        """
        return self._grade_repo.get_all_grades()

    def find_grade_by_id(self, grade_id):
        """
        Returns the grade with the given id
        :param grade_id: integer
        :return: Grade if found, error otherwise
        """
        return self._grade_repo.find_by_id(grade_id)

    def add_grade(self, grade_id, stud_id, sub_id, mark):
        """
        Adds a grade
        :param grade_id: integer, unique
        :param stud_id: integer, unique
        :param sub_id: integer, unique
        :param mark: integer, non-null and <= 10
        :return:
        """
        grade = Grade(grade_id, stud_id, sub_id, mark)
        self._valid_grade.validate(grade)
        self._grade_repo.add_grade(grade)

    def delete_grade(self, grade_id):
        """
        Deletes a grade
        :param grade_id: integer
        :return:
        """
        return self._grade_repo.delete_grade(grade_id)

    def modify_grade(self, grade_id, mark):
        """
        Modifies a grade
        :param grade_id: integer
        :param mark: mark that's going to be modified
        :return:
        """
        self._grade_repo.modify_grade(grade_id, mark)

    def get_students_with_grades_alphabetically(self, sub_name):
        """
        Returns a list of all the students and their respective grades, sorted by their names
        :return: list of students and their grades
        """
        grades = self._grade_repo.get_all_grades()
        grade_dtos = {}
        for _grade in grades:
            student = self._stud_repo.find_by_id(_grade.get_stud_id())
            subject = self._sub_repo.find_by_id(_grade.get_sub_id())
            if subject.get_subject_name() == sub_name:
                grade_dto = GradeDTO(_grade.get_grade_id(), _grade.get_stud_id(), _grade.get_sub_id(), _grade.get_mark())
                grade_dto.set_stud(student)
                grade_dto.set_sub(subject)
                if student.get_student_id() not in grade_dtos:
                    grade_dtos[student.get_student_id()] = []
                grade_dtos[student.get_student_id()].append(grade_dto)
        sorted_result = []
        g_dtos = []
        for _g in grade_dtos.items():
            stud_id = _g[0]
            student = self._stud_repo.find_by_id(stud_id)
            marks = _g[1]
            grade_dto = StudentGradesDTO(student.get_student_name(), marks)
            g_dtos.append(grade_dto)
        sorted_dtos = sorted(g_dtos, key=lambda item: (item.get_student_name().split(' ')[-1]))
        for _sorted in sorted_dtos:
            sorted_result.append(_sorted)
        return sorted_result

    def get_students_with_grades_by_marks(self, sub_name):
        """
        Returns a list of all the students and their respective grades, sorted by their grades
        :return: list of students and their grades
        """
        grades = self._grade_repo.get_all_grades()
        grade_dtos = {}
        for _grade in grades:
            student = self._stud_repo.find_by_id(_grade.get_stud_id())
            subject = self._sub_repo.find_by_id(_grade.get_sub_id())
            if subject.get_subject_name() == sub_name:
                grade_dto = GradeDTO(_grade.get_grade_id(), _grade.get_stud_id(), _grade.get_sub_id(), _grade.get_mark())
                grade_dto.set_stud(student)
                grade_dto.set_sub(subject)
                if student.get_student_id() not in grade_dtos:
                    grade_dtos[student.get_student_id()] = []
                grade_dtos[student.get_student_id()].append(grade_dto)
        sorted_result = []
        g_dtos = []
        for _g in grade_dtos.items():
            stud_id = _g[0]
            student = self._stud_repo.find_by_id(stud_id)
            marks = _g[1]
            grade_dto = StudentGradesDTO(student.get_student_name(), marks)
            g_dtos.append(grade_dto)
        sorted_dtos = sorted(g_dtos, key=lambda item: (sum(item.get_marks() / len(item.get_marks()))))
        for _sorted in sorted_dtos:
            sorted_result.append(_sorted)
        return sorted_result

    def top_twenty_students(self):
        """
        Get the top 20% of students with the highest average
        :return:
        """
        grades = self._grade_repo.get_all_grades()
        grade_dtos = {}
        for _grade in grades:
            student = self._stud_repo.find_by_id(_grade.get_stud_id())
            subject = self._sub_repo.find_by_id(_grade.get_sub_id())
            grade_dto = GradeDTO(_grade.get_grade_id(), _grade.get_stud_id(), _grade.get_sub_id(), _grade.get_mark())
            grade_dto.set_stud(student)
            grade_dto.set_sub(subject)
            if student.get_student_id() not in grade_dtos:
                grade_dtos[student.get_student_id()] = []
            grade_dtos[student.get_student_id()].append(grade_dto)
        mm = []
        students = []
        for _g in grade_dtos.items():
            stud_id = _g[0]
            student = self._stud_repo.find_by_id(stud_id)
            students.append(student.get_student_name())
            marks = _g[1]
            mm.append(marks)
        averages = []
        for _m, student_name in zip(mm, students):
            summ = 0
            for m in _m:
                summ += int(m.get_mark())
            avg = summ / len(_m)
            averages_dtos = StudentAveragesDTO(student_name, avg)
            averages.append(averages_dtos)
        sorted_avgs = sorted(averages, key=lambda a: a.get_average(), reverse=True)
        res = sorted_avgs[:int(len(sorted_avgs) * 0.2)]
        return res

    def top_three_subjects(self):
        """
        Gets the top 3 subjects with the most grades
        :return:
        """
        grades = self._grade_repo.get_all_grades()
        grade_dtos = {}
        for _grade in grades:
            student = self._stud_repo.find_by_id(_grade.get_stud_id())
            subject = self._sub_repo.find_by_id(_grade.get_sub_id())
            grade_dto = GradeDTO(_grade.get_grade_id(), _grade.get_stud_id(), _grade.get_sub_id(), _grade.get_mark())
            grade_dto.set_stud(student)
            grade_dto.set_sub(subject)
            if subject.get_subject_id() not in grade_dtos:
                grade_dtos[subject.get_subject_id()] = []
            grade_dtos[subject.get_subject_id()].append(grade_dto)
        mm = []
        subjects = []
        for _g in grade_dtos.items():
            sub_id = _g[0]
            marks = _g[1]
            subject = self._sub_repo.find_by_id(sub_id)
            subjects.append(subject.get_subject_name())
            mm.append(marks)
        top_subjects = []
        for _m, sub_name in zip(mm, subjects):
            top_subject = PopularSubjectsDTO(sub_name, _m)
            top_subjects.append(top_subject)
        sorted_subjects = sorted(top_subjects, key=lambda s:len(s.get_marks()), reverse=True)
        res = sorted_subjects[:3]
        return res

    def delete_grade_recursively(self, grade_id, i):
        self._grade_repo.repo_delete_grade_recursively(grade_id, i)

    def find_grade_by_id_recursively(self, grade_id, i):
        return self._grade_repo.repo_find_by_id_recursively(grade_id, i)

    def grades_bubble_sort(self, user_input):
        all_grades = self._grade_repo.get_all_grades()
        bubble_sort(all_grades, key=lambda _grade: _grade.get_grade_id(), reverse=False, cmp=lambda a, b, r=False: a < b if r is False else a > b)
        if user_input == "id":
            for _grade in all_grades:
                print(_grade.get_grade_id())
        elif user_input == "subject":
            for _grade in all_grades:
                print(_grade.get_sub_id())
        elif user_input == "student":
            for _grade in all_grades:
                print(_grade.get_stud_id())
        elif user_input == "mark":
            for _grade in all_grades:
                print(_grade.get_mark())
        elif user_input == "all":
            for _grade in all_grades:
                print(_grade)

    def grades_shell_sort(self, user_input):
        all_grades = self._grade_repo.get_all_grades()
        shell_sort(all_grades, key=lambda _grade: _grade.get_grade_id(), reverse=False, cmp=lambda a, b, r=False: a < b if r is False else a > b)
        if user_input == "id":
            for _grade in all_grades:
                print(_grade.get_grade_id())
        elif user_input == "subject":
            for _grade in all_grades:
                print(_grade.get_sub_id())
        elif user_input == "student":
            for _grade in all_grades:
                print(_grade.get_stud_id())
        elif user_input == "mark":
            for _grade in all_grades:
                print(_grade.get_mark())
        elif user_input == "all":
            for _grade in all_grades:
                print(_grade)
