from lab7_9.exceptions.repository_exception import RepositoryException


class GradeRepo(object):
    def __init__(self):
        self._grades = []

    def __len__(self):
        return len(self._grades)

    def get_all_grades(self):
        """
        Gets all the grades
        :return: List of grades
        """
        return self._grades

    def find_by_id(self, grade_id):
        """
        Returns the grade with the given id
        :param grade_id: integer
        :return: Grade or error if a subject with the given id doesn't exist

        Complexitatea functiei este O(n)
        Caz favorabili primul element este cel cautat, se executa un singur pas, T(n) = 1 ce gpartine de 0(1)
        Caz defadvorabil: nu exista filmul cautat in lista, se executa n pasi, T(n) = n ce apartine de O(n)
        Caz mediu: for poate fi executat de 1,2,3,...,n ori(aceeasi probabilitate), deci T(n) = (n+1)/2 ce apartine de O(n)
        """
        not_found = True
        for _grade in self._grades:
            if _grade.get_grade_id() == grade_id:
                return _grade
        if not_found:
            raise RepositoryException("Grade doesn't exist!\n")

    def add_grade(self, grade):
        """
        Validates a grade object and adds it to the repo
        :param grade: Grade
        :return: Error thrown if the grade already exists
        """
        for _grade in self._grades:
            if _grade.get_grade_id() == grade.get_grade_id():
                raise RepositoryException("Grade already exists!\n")
        self._grades.append(grade)

    def delete_grade(self, grade_id):
        """
        Removes a subject that matches the given id
        :param grade_id: integer
        :return: List with the grade deleted
        """
        all_grades = self._grades
        all_grades[:] = [_gr for _gr in self._grades if not _gr.get_grade_id() == grade_id]
        return all_grades

    def modify_grade(self, grade_id, mark):
        """
        Modifies a grades's mark
        :param grade_id: integer
        :param mark: integer
        :return: Error if the grade doesn't exist
        """
        not_found = True
        for _grade in self._grades:
            if _grade.get_grade_id() == grade_id:
                not_found = False
                _grade.set_mark(mark)
        if not_found:
            raise RepositoryException("Grade doesn't exist!\n")

    def find_by_id_recursively(self, grade_id, n):
        """
        Recursively finds the id of a grade
        :param grade_id: int
        :param n: int
        :return: id of the grade
        """
        if n >= len(self._grades):
            raise RepositoryException("Couldn't find the grade\n")
        if int(self._grades[n - 1].get_grade_id()) == grade_id:
            return self._grades[n - 1]
        return self.find_by_id_recursively(grade_id, n + 1)

    def delete_grade_recursively(self, grade_id, i):
        """
        Recursively deletes a grade
        :param grade_id: int
        :param i: int
        :return: -
        """
        if i >= len(self._grades):
            raise RepositoryException("Couldn't find the grade\n")
        if int(self._grades[i].get_grade_id()) == grade_id:
            del self._grades[i]
            return True
        return self.delete_grade_recursively(grade_id, i + 1)
