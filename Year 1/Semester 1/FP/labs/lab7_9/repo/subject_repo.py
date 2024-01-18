from lab7_9.exceptions.repository_exception import RepositoryException


class SubjectRepo(object):
    def __init__(self):
        self._subjects = []

    def __len__(self):
        return len(self._subjects)

    def get_all_subjects(self):
        """
        Gets all the subjects
        :return: List of subjects
        """
        return self._subjects

    def find_by_id(self, sub_id):
        """
        Returns the subject with the given id
        :param sub_id: integer
        :return: Subject or error if a subject with the given id doesn't exist
        """
        not_found = True
        for _sub in self._subjects:
            if _sub.get_subject_id() == sub_id:
                return _sub
        if not_found:
            raise RepositoryException("Subject doesn't exist!\n")

    def add_subject(self, subject):
        """
        Validates a subject object and adds it to the repo
        :param subject: Subject
        :return: Error thrown if the subject already exists
        """
        for _subject in self._subjects:
            if _subject.get_subject_id() == subject.get_subject_id():
                raise RepositoryException("Subject already exists!\n")
        self._subjects.append(subject)

    def delete_subject(self, sub_id):
        """
        Removes a subject that matches the given id
        :param sub_id: integer
        :return: List with the subject deleted
        """
        all_subjects = self._subjects
        all_subjects[:] = [_sub for _sub in self._subjects if not _sub.get_subject_id() == sub_id]
        return all_subjects

    def modify_subject(self, sub_id, sub_name, sub_prof):
        """
        Modifies a subject's name and professor
        :param sub_id: integer
        :param sub_name: string
        :param sub_prof: string
        :return: Error if the subject doesn't exist
        """
        not_found = True
        for _sub in self._subjects:
            if _sub.get_subject_id() == sub_id:
                not_found = False
                _sub.set_subject_name(sub_name)
                _sub.set_subject_prof(sub_prof)
        if not_found:
            raise RepositoryException("Subject doesn't exist!\n")
