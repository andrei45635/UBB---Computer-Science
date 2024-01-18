from lab7_9.domain.subject import Subject
from lab7_9.exceptions.repository_exception import RepositoryException
from lab7_9.repo.subject_repo import SubjectRepo


class SubjectFileRepo(SubjectRepo):
    def __init__(self, filepath):
        SubjectRepo.__init__(self)
        self.__filepath = filepath

    def read_from_file(self):
        """
        Reads subjects from a file
        :return:
        """
        self._subjects = []
        with open(self.__filepath, "r") as f:
            lines = f.read()
            lines_arr = [lines]
            for line in lines_arr:
                for sub in line.splitlines():
                    sub_id = sub.split(",")[0]
                    sub_name = sub.split(",")[1]
                    sub_prof = sub.split(",")[2]
                    subject = Subject(sub_id, sub_name, sub_prof)
                    self._subjects.append(subject)

    def append_to_file(self, subject):
        """
        Writes a subject to a file
        :param subject: Subject
        :return:
        """
        with open(self.__filepath, "a") as f:
            f.write(str(subject.get_subject_id()) + "," + str(subject.get_subject_name()) + "," + str(
                subject.get_subject_prof()) + "\n")

    def write_all_to_file(self):
        """
        Writes a list of subjects to the file
        :return:
        """
        with open(self.__filepath, "w") as f:
            for subject in self._subjects:
                f.write(str(subject.get_subject_id()) + "," + str(subject.get_subject_name()) + "," + str(
                    subject.get_subject_prof()) + "\n")

    def add_subject(self, subject):
        """
        Overriden method from SubjectRepo
        Adds a student
        :param subject: Subject
        :return:
        """
        self.read_from_file()
        SubjectRepo.add_subject(self, subject)
        self.append_to_file(subject)

    def find_by_id(self, sub_id):
        """
        Overridden method from SubjectRepo
        Finds a subject given an id
        :param sub_id: integer
        :return:
        """
        self.read_from_file()
        try:
            return SubjectRepo.find_by_id(self, sub_id)
        except RepositoryException:
            raise RepositoryException("Subject already exists!\n\n")

    def get_all_subjects(self):
        """
        Gettter for all the subjects
        :return:
        """
        self.read_from_file()
        return SubjectRepo.get_all_subjects(self)

    def __len__(self):
        """
        Overrides __len__
        :return:
        """
        self.read_from_file()
        return SubjectRepo.__len__(self)

    def modify_subject(self, option1, option2, option3):
        """
        Overridden method from SubjectRepo
        Modifies a subject
        :param option1: integer, subject's ID
        :param option2: string, subject's Name
        :param option3: string, subject's Professor
        :return:
        """
        self.read_from_file()
        SubjectRepo.modify_subject(self, option1, option2, option3)
        self.write_all_to_file()

    def delete_subject(self, user_input):
        """
        Overridden method from SubjectRepo
        Removes a subject
        :param user_input: integer, subject's ID
        :return:
        """
        self.read_from_file()
        SubjectRepo.delete_subject(self, user_input)
        self.write_all_to_file()
