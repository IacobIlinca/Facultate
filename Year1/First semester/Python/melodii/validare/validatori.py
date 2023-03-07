from exceptii.erori import ValidationError
class ValidMelodie:
    def valideaza(self,melodie):
        err = ""
        genuri = ["Rock", "Pop", "Jazz", "Altele"]
        if melodie.get_titlu() == "":
            err += "titlu invalid!"
        if melodie.get_artist() == "":
            err +=  "artist invalid!"
        if melodie.get_gen() not in genuri:
            err += "gen invalid!"
        campuri = melodie.get_data().split(".")
        if len(campuri)==3:
            zi = campuri[0]
            luna = campuri[1]
            an = campuri[2]
            if int(zi)<1 or int(zi)>31:
                err += "zi invalida!"
            if int(luna)<1 or int(luna)>12:
                err += "luna invalida!"
            if int(an)<0:
                err += "an invalid!"
        else:
            err += "data invalida!"
        if len(err)>0:
            raise ValidationError(err)