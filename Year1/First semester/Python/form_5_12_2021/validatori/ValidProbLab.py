from erori.exceptii import ValidationError
class Validator_problema_lab():

    def valideaza(self, prob):
        err=""
        if prob.get_nr_lab() <=0:
            err += "id numeric invalid!"
        if prob.get_descriere() == "":
            err += "descriere invalida!"
        if prob.get_deadline() <1 or prob.get_deadline()>31:
            err += "deadline invalid!"
        if len(err)>0:
            raise ValidationError(err)
