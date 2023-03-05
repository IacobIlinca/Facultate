class ValidationError(Exception):
    pass

class ValidationException(ValidationError):
    def __init__(self, msgs):
        #msgs: lista de mesaje de eroare
        self.__err_msgs = msgs

    def getMessages(self):
        return self.__err_msgs

    def __str__(self):
        return 'Validation Exception: ' + str(self.__err_msgs)


class RepositoryError(Exception):
    pass

class StudentAlreadyAssignedException(RepositoryError):
    def __init__(self):
        RepositoryError.__init__(self, "Nota existenta pentru student si disciplina date.")


class StudentNotFoundException(RepositoryError):
    def __init__(self):
        RepositoryError.__init__(self, "Studentul nu a fost gasit. ")

class DisciplinaNotFoundException(RepositoryError):
    def __init__(self):
        RepositoryError.__init__(self, "Disciplina nu a fost gasita. ")
