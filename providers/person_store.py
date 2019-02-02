import abc

class PersonStore(abc.ABC):
    @abc.abstractmethod
    def save_person_list(self, personList):
        pass