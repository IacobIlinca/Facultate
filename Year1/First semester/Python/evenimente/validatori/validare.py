from erori.exceptii import ValidationError
class ValidareEveniment():

    def valideaza(self,eveniment):
        errors = ""
        campuri = eveniment.get_data().split(".")
        if len(campuri) == 3:
            zi = campuri[0]
            luna = campuri[1]
            an = campuri[2]
            if int(zi)<1 or int(zi)>31:
                errors+="zi invalida"
            if int(luna)<1 or int(luna)>12:
                errors+="luna invalida"
            if int(an)<0:
                errors+="an invalid"

        else:
            errors+="format data invalid!"

        campuri = eveniment.get_ora().split(":")
        ora = campuri[0]
        minute = campuri[1]
        if len(campuri)==2:
            if int(ora)<0 or int(ora)>23:
                errors+="ora invalida"
            if int(minute)<0 or int(minute)>60:
                errors+="minut invalid"
        else:
            errors+="format ora invalid"

        if eveniment.get_descriere() == "":
            errors+="descriere invalida"

        if len(errors)>0:
            raise ValidationError(errors)