from erori.exceptii import ValidationError, ValidationException
class ValidatorStudent(object):
    def valideaza(self, stud):
        errors = ""
        if stud.get_id_stud()<0:
            errors += "id invalid!\n"
        if stud.get_nume() == "" :
            errors += "nume invalid!\n"
        if len(errors) >0:
            raise ValidationError(errors)


class ValidatorDisciplina(object):
    def valideaza(self, disc):
        errors = ""
        if disc.get_id_disc() < 0:
            errors += "id invalid!\n"
        if disc.get_nume == "":
            errors += "nume invalid!\n"
        if disc.get_profesor == "":
            errors += "profesor invalid!\n"
        if len(errors) > 0:
            raise ValidationError(errors)

class ValidatorNota():
    def validate(self, nota):
        errors = []
        if int(nota.get_valoare()) < 0 or int(nota.get_valoare()) > 10:
            errors.append("Nota nu este valida.")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValidationException(errors)
            # raise ValidationException