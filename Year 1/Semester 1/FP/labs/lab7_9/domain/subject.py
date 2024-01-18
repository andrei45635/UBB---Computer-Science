class Subject(object):
    def __init__(self, subject_id, subject_name, subject_prof):
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__subject_prof = subject_prof

    def get_subject_id(self):
        return self.__subject_id

    def get_subject_name(self):
        return self.__subject_name

    def get_subject_prof(self):
        return self.__subject_prof

    def set_subject_name(self, new_name):
        self.__subject_name = new_name

    def set_subject_prof(self, new_prof):
        self.__subject_prof = new_prof

    def __eq__(self, other):
        return self.__subject_id == other.__subject_id and self.__subject_name == other.__subject_name and self.__subject_prof == other.__subject_prof

    def __str__(self):
        return f"Subject ID: {self.__subject_id}, Subject Name: {self.__subject_name}, Professor: {self.__subject_prof}"
