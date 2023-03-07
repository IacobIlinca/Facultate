from exceptii.erori import ValidationError
class ValidEmisiune:

    def valideaza(self,emisiune):
        err = ""
        if emisiune.get_nume() == "":
            err += "nume invalid!"
        if emisiune.get_tip() == "":
            err += "tip invalid!"
        if emisiune.get_durata()<0:
            err += "durata invalida!"
        if emisiune.get_descriere() == "":
            err += "descriere invalida!"

        if len(err)>0:
            raise ValidationError(err)