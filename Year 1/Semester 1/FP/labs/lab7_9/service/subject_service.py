import random

from lab7_9.domain.subject import Subject
from lab7_9.utils.random_generation import generare_aleator_int, generare_aleator_string


class SubjectService(object):
    def __init__(self, valid_sub, sub_repo):
        self._valid_sub = valid_sub
        self._sub_repo = sub_repo

    def size(self):
        """
        Returns the number of subjects
        :return: integer
        """
        return len(self._sub_repo)

    def get_all_subjects(self):
        """
        Returns all subjects
        :return:
        """
        return self._sub_repo.get_all_subjects()

    def find_sub_by_id(self, sub_id):
        """
        Returns the subject with the given id
        :param sub_id: integer
        :return: Subject if found, error otherwise
        """
        return self._sub_repo.find_by_id(sub_id)

    def add_subject(self, sub_id, sub_name, sub_prof):
        """
        Adds a subject
        :param sub_id: integer, unique
        :param sub_name: string, non-null
        :param sub_prof: string, non-null
        :return:
        """
        subject = Subject(sub_id, sub_name, sub_prof)
        self._valid_sub.validate(subject)
        self._sub_repo.add_subject(subject)

    def delete_subject(self, sub_id):
        """
        Deletes a subject
        :param sub_id: integer
        :return:
        """
        return self._sub_repo.delete_subject(sub_id)

    def modify_subject(self, sub_id, sub_name, sub_prof):
        """
        Modifies a subject
        :param sub_id: integer
        :param sub_name: name that's going to be modified
        :param sub_prof: professor that's going to be modified
        :return:
        """
        self._sub_repo.modify_subject(sub_id, sub_name, sub_prof)

    def generate_random_subjects(self, n):
        """
        Genereaza discipline random
        :return:
        """
        for _ in range(n):
            _subject = Subject(int(generare_aleator_int(n)), generare_aleator_string(random.randrange(3, 25)),
                               generare_aleator_string(random.randrange(3, 27)))

            self._valid_sub.validate(_subject)
            self._sub_repo.add_subject(_subject)

