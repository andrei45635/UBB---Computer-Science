from lab7_9.exceptions.repository_exception import RepositoryException
from lab7_9.exceptions.validator_exception import ValidatorException
from lab7_9.utils.sorting_algorithms import bubble_sort, shell_sort


class Console(object):
    def __init__(self, srv_stud, srv_sub, srv_grade):
        self._srv_stud = srv_stud
        self._srv_sub = srv_sub
        self._srv_grade = srv_grade

    def add_student(self):
        try:
            stud_id = int(input("Input the student ID: "))
        except ValueError:
            print("Please input a number.")
            return
        stud_name = input("Input the student's name: ")
        self._srv_stud.add_student(stud_id, stud_name)
        print("Successfully added the student.")

    def find_student_by_id(self):
        try:
            stud_id = int(input("Input the student's ID: "))
        except ValueError:
            print("Please input a number.")
            return

        try:
            print(self._srv_stud.find_stud_by_id(stud_id))
        except RepositoryException as re:
            print("Error: " + str(re))

    def delete_student(self):
        if self._srv_stud.size() == 0:
            print("You haven't saved any students yet!")
        else:
            try:
                stud_id = int(input("Input the ID of the student you want to remove: "))
            except ValueError:
                print("Please input a number.")
                return
            self._srv_stud.delete_student(stud_id)

    def print_all_students(self):
        students = self._srv_stud.get_all_studs()
        if len(students) == 0:
            print("You haven't saved any students yet!")
        else:
            for _stud in students:
                print(_stud)

    def modify_student(self):
        try:
            stud_id = int(input("Input the student's ID: "))
        except ValueError:
            print("Please input a number.")
            return
        new_stud_name = input("Change the student's name: ")
        self._srv_stud.modify_student(stud_id, new_stud_name)

    def add_subject(self):
        try:
            sub_id = int(input("Input the subject's ID: "))
        except ValueError:
            print("Please input a number.")
            return
        sub_name = input("Input the subject's name: ")
        sub_prof = input("Input the subject's professor: ")
        self._srv_sub.add_subject(sub_id, sub_name, sub_prof)
        print("Successfully added the subject!")

    def find_subject_by_id(self):
        try:
            sub_id = int(input("Input the ID of the subject you're looking for: "))
        except ValueError:
            print("Please input a number.")
            return
        try:
            print(self._srv_sub.find_sub_by_id(sub_id))
        except RepositoryException as re:
            print("Error: " + str(re))

    def delete_subject(self):
        if self._srv_sub.size() == 0:
            print("You haven't saved any subjects yet!")
        else:
            try:
                sub_id = int(input("Input the subject's ID: "))
            except ValueError:
                print("Please input a number.")
                return
            self._srv_sub.delete_subject(sub_id)

    def print_all_subjects(self):
        subjects = self._srv_sub.get_all_subjects()
        if len(subjects) == 0:
            print("You haven't saved any subjects yet!")
        else:
            for _sub in subjects:
                print(_sub)

    def modify_subject(self):
        try:
            sub_id = int(input("Input the subject's ID: "))
        except ValueError:
            print("Please input a number.")
            return
        try:
            new_sub_name = input("Change the subject's name: ")
        except ValueError:
            print("Please input a string.")
            return
        try:
            new_sub_prof = input("Change the subject's professor: ")
        except ValueError:
            print("Please input a string.")
            return
        self._srv_sub.modify_subject(sub_id, new_sub_name, new_sub_prof)

    def print_all_grades(self):
        grades = self._srv_grade.get_all_grades()
        if len(grades) == 0:
            print("You haven't saved any grades yet!")
        else:
            for _grade in grades:
                print(_grade)

    def add_grade(self):
        try:
            grade_id = int(input("Input the grade's ID: "))
        except ValueError:
            print("Please input a number.")
            return
        try:
            stud_id = int(input("Input the student's ID: "))
        except ValueError:
            print("Please input a number.")
            return
        try:
            sub_id = int(input("Input the subject's ID: "))
        except ValueError:
            print("Please input a number.")
            return
        try:
            mark = int(input("Input the mark: "))
        except ValueError:
            print("Please input a number.")
            return
        self._srv_grade.add_grade(grade_id, stud_id, sub_id, mark)
        print("Successfully added the grade!")

    def find_grade_by_id(self):
        try:
            grade_id = int(input("Input the ID of the grade you're looking for: "))
        except ValueError:
            print("Please input a number.")
            return
        try:
            print(self._srv_grade.find_grade_by_id(grade_id))
        except RepositoryException as re:
            print("Error: " + str(re))

    def delete_grade(self):
        if self._srv_grade.size() == 0:
            print("You haven't saved any grades yet!")
        else:
            try:
                grade_id = int(input("Input the grade's ID: "))
            except ValueError:
                print("Please input a number.")
                return
            self._srv_grade.delete_grade(grade_id)

    def modify_grade(self):
        try:
            grade_id = int(input("Input the grade's ID: "))
        except ValueError:
            print("Please input a number.")
            return
        try:
            new_mark = input("Change the mark: ")
        except ValueError:
            print("Please input a number.")
            return
        self._srv_grade.modify_grade(grade_id, new_mark)

    def generate_random_subjects(self):
        try:
            amount = int(input("Input the number of subjects you want to generate: "))
        except ValueError:
            print("Please input a number.")
            return
        self._srv_sub.generate_random_subjects(amount)

    def all_students_with_grades_alphabetically(self):
        sub_name = input("Input the subject you want to sort by: ")
        dtos = self._srv_grade.get_students_with_grades_alphabetically(sub_name)
        for _dto in dtos:
            print(_dto)

    def all_students_with_grades_by_marks(self):
        sub_name = input("Input the subject you want to sort by: ")
        dtos = self._srv_grade.get_students_with_grades_by_marks(sub_name)
        for _dto in dtos:
            print(_dto)

    def top_twenty_students(self):
        dtos = self._srv_grade.top_twenty_students()
        for _dto in dtos:
            print(_dto)

    def top_three_subjects(self):
        dtos = self._srv_grade.top_three_subjects()
        for _dto in dtos:
            print(_dto)

    def print_grade_by_id_recursively(self):
        try:
            grade_id = int(input("Input the ID: "))
        except ValueError:
            print("Invalid number!")
            return
        try:
            print(self._srv_grade.find_grade_by_id_recursively(grade_id, 0))
        except RepositoryException as re:
            print("Error: " + str(re))

    def delete_grade_recursively(self):
        try:
            grade_id = int(input("Input the ID: "))
        except ValueError:
            print("Invalid number!")
            return
        try:
            print(self._srv_grade.delete_grade_recursively(grade_id, 0))
        except RepositoryException as re:
            print("Error: " + str(re))
        print("Successfully deleted a grade recursively")

    def sorting_grades_bubble(self):
        user_input = input("Introduceti cheia dupa care doriti sa cautati: ")
        self._srv_grade.grades_bubble_sort(user_input)

    def sorting_grades_shell(self):
        user_input = input("Introduceti cheia dupa care doriti sa cautati: ")
        self._srv_grade.grades_shell_sort(user_input)

    def show_menu(self):
        print("--------------------------- UNIVERSITY APPLICATION ---------------------------\n")
        print("0/1. exit = exit the program")
        print("2. add_student = add student to the list")
        print("3. add_subject = add subject to the list")
        print("4. add_grade = add a grade")
        print("5. print_students = print the list of students")
        print("6. print_subjects = print the list of subjects")
        print("7. print_grades = print the list of grades")
        print("8. delete_students = delete students from the list by ID")
        print("9. delete_subjects = delete subjects from the list by ID")
        print("10. delete_grade = delete a grade")
        print("11. search_students_by_id = display the student searched by ID")
        print("12. search_subjects_by_id = display the subject searched by ID")
        print("13. search_grades_by_id = display the grade searched by ID")
        print("14. modify_student = modify a student")
        print("15. modify_subject = modify a subject")
        print("16. modify_grade = modify a grade")
        print("17. generate_random_subjects = generate random subjects")
        print("18. all_students_with_grades_alphabetically = all the students with their grades sorted by name")
        print("19. all_students_with_grades_by_marks = all the students with their grades sorted by their average")
        print("20. top_twenty_students = top twenty students ordered by their average grade")
        print("21. top_three_subjects = top three subjects with the most grades")
        print("22. print_grade_by_id_recursively = recursively finds the grade by a given id")
        print("23. delete_grade_recursively = recursively delete a grade")
        print("24. bubble_sort")
        print("25. shell_sort")

    def run(self):
        while True:
            self.show_menu()
            cmd = int(input(">>>"))
            if cmd == 0:
                return
            if cmd == " ":
                continue
            elif cmd == 1:
                return
            elif cmd == 2:
                try:
                    self.add_student()
                except ValidatorException as ve:
                    print("Error when validating the student: " + str(ve))
                except RepositoryException as re:
                    print("Error: " + str(re))
            elif cmd == 3:
                try:
                    self.add_subject()
                except ValidatorException as ve:
                    print("Error when validating the subject: " + str(ve))
                except RepositoryException as re:
                    print("Error: " + str(re))
            elif cmd == 4:
                try:
                    self.add_grade()
                except ValidatorException as ve:
                    print("Error when validating the grade: " + str(ve))
                except RepositoryException as re:
                    print("Error: " + str(re))
            elif cmd == 5:
                self.print_all_students()
            elif cmd == 6:
                self.print_all_subjects()
            elif cmd == 7:
                self.print_all_grades()
            elif cmd == 8:
                self.delete_student()
            elif cmd == 9:
                self.delete_subject()
            elif cmd == 10:
                self.delete_grade()
            elif cmd == 11:
                self.find_student_by_id()
            elif cmd == 12:
                self.find_subject_by_id()
            elif cmd == 13:
                self.find_grade_by_id()
            elif cmd == 14:
                self.modify_student()
            elif cmd == 15:
                self.modify_subject()
            elif cmd == 16:
                self.modify_grade()
            elif cmd == 17:
                self.generate_random_subjects()
            elif cmd == 18:
                self.all_students_with_grades_alphabetically()
            elif cmd == 19:
                self.all_students_with_grades_by_marks()
            elif cmd == 20:
                self.top_twenty_students()
            elif cmd == 21:
                self.top_three_subjects()
            elif cmd == 22:
                self.print_grade_by_id_recursively()
            elif cmd == 23:
                self.delete_grade_recursively()
            elif cmd == 24:
                self.sorting_grades_bubble()
            elif cmd == 25:
                self.sorting_grades_shell()
            else:
                print("Invalid command!")
