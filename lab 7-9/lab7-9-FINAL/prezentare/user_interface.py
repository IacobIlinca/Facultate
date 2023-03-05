from erori.exceptii import RepositoryError, ValidationError, ValidationException, StudentNotFoundException, DisciplinaNotFoundException, StudentAlreadyAssignedException
class Consola (object) :

    def __init__(self, srv_studenti, srv_discipline, srv_note):
        self.__srv_studenti = srv_studenti
        self.__srv_discipline = srv_discipline
        self.__srv_note = srv_note

    def __ui_print_meniu(self):
        print(">>>")
        print("Actiunile pe care utilizatorul le poate alege sunt:\n")

        print("Adauga un nou student in lista: add_student")
        print("Sterege un student din lista dupa id: sterge_student")
        print("Cauta un student in lista dupa id: cauta_student")
        print("Modificarea numelui unui student cu id dat: modificare_nume_student")
        print("Genereaza X studenti random: generate_studenti X\n")

        print("Adauga o noua disciplina in lista: add_disciplina")
        print("Sterege o disciplina din lista dupa id: sterge_disciplina")
        print("Cauta o disciplina in lista dupa id: cauta_disciplina")
        print("Modificarea numelui unui profesor de la o disciplina cu id dat: modificare_prof_disciplina")
        print("Genereaza X discipline random: generate_discipline X")

        print("Adauga o noua nota unui student la o disciplina: add_nota")
        print("Sterge o nota: sterge_nota")
        print("Cauta o nota dupa id: cauta_nota")
        print("Modificarea valorii unei note: update_nota")

        print("Lista de studenți și notele lor la o disciplină dată, ordonat alfabetic după nume: sort_alfabetic")
        print("lista de studenți și notele lor la o disciplină dată, ordonat dupa nota: sort_nota")
        print ("Primi 20% din studenți ordonat dupa media notelor la toate disciplinele (nume și notă): 20%")
        print("Primele 3 discipline cu cele mai multe note(nume_disciplină,număr_note): top_3")
        print("Comparare compusa:prima data dupa nume, apoi dupa profesor: cmp_noua")


    def __ui_adauga_stud (self):
        try:
            id_stud = int (input("id student:"))
        except ValueError:
            print ("id numeric invalid!")
            return
        nume = input ("nume:")
        self.__srv_studenti.adauga_student(id_stud, nume)
        print("Student adaugat cu succes!")

    def __ui_print_studenti(self):
        self.__srv_studenti.get_all_studenti()

    def __ui_print_note(self):
        self.__srv_note.get_all_note()

    def __ui_adauga_disc (self):
        try:
            id_disc = int (input("id disciplina:"))
        except ValueError:
            print ("id numeric invalid!")
            return
        nume = input ("nume:")
        profesor = input ("profesor:")
        self.__srv_discipline.adauga_disciplina(id_disc, nume, profesor)
        print("Disciplina adaugata cu succes!")

    def __ui_print_discipline(self):
        self.__srv_discipline.get_all_discipline()

    def __ui_cautare_stud (self):
        try:
            id_stud = int (input("id student cautat:"))
        except ValueError:
            print ("id numeric invalid!")
            return
        stud = self.__srv_studenti.cautare_student(id_stud)
        print("Studentul cautat este:")
        return stud

    def __ui_cautare_disc(self):
        try:
            id_disc = int (input("id disciplina cautata:"))
        except ValueError:
            print ("id numeric invalid!")
            return
        disc = self.__srv_discipline.cautare_disciplina(id_disc)
        print("Disciplina cautata este:")
        return disc

    def __ui_modifica_stud (self):
        try:
            id_stud = int (input("id-ul student a carui nume se doreste a fi modificat:"))
        except ValueError:
            print ("id numeric invalid!")
            return
        nume= input("noul nume este:")
        self.__srv_studenti.modifica_student(id_stud, nume)
        print("Numele studentului dat a fost modificat cu succes!")

    def __ui_modifica_disc(self):
        try:
            id_disc = int(input("id-ul disciplinei a carui profesor se doreste a fi modificat:"))
        except ValueError:
            print("id numeric invalid!")
            return
        profesor = input("numele noului profesor este:")
        self.__srv_discipline.modifica_disciplina(id_disc, profesor)
        print("Numele profesorului disciplinei date a fost modificat cu succes!")

    def __ui_sterge_stud (self):
        try:
            id_stud = int (input("id-ul studentului ce se doreste a fi sters:"))
        except ValueError:
            print ("id numeric invalid!")
            return
        n = None
        self.__srv_studenti.sterge_student(id_stud,n)
        print("Studentul a fost sters cu succes!")

    def __ui_sterge_disc (self):
        try:
            id_disc = int (input("id-ul disciplinei ce se doreste a fi stearsa:"))
        except ValueError:
            print ("id numeric invalid!")
            return
        n = None
        self.__srv_discipline.sterge_disciplina(id_disc, n)
        print("Disciplina a fost stearsa cu succes!")

    def __ui_generate_random_students (self):
        x = int (input("Numarul de studenti generati random dorit:"))
        self.__srv_studenti.generate_random_student (x)

    def __ui_add_nota(self):
        #adauga o nota
        try:
            id_nota = int(input("Introduceti id-ul notei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            id_stud = int(input("Introduceti id-ul studentului: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            id_disc = int(input("Introduceti id-ul disciplinei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            valoare = float(input("Introduceti valoarea notei: "))
        except ValueError:
            print("\nvaloarea notei trebuie sa fie un numar real\n")
            return
        try:
            self.__srv_note.adauga_nota(id_nota, id_stud, id_disc, valoare)
            print("\nNota adaugata cu succes!!!\n")
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __ui_sterge_nota(self):
        try:
            idNota = int(input("Introduceti id-ul notei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            self.__srv_note.sterge_nota(idNota)
            print("\nNota stearsa cu succes!!!\n")
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __ui_cauta_nota_dupa_id(self):
        try:
            idNota = int(input("Introduceti id-ul notei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            nota = self.__srv_note.cauta_nota_dupa_id(idNota)
            print(str(nota))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))


    def __ui_update_nota(self):
        try:
            id_nota = int(input("Introduceti id-ul notei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            valoare = float(input("Introduceti noua valoare a notei: "))
        except ValueError:
            print("\nvaloarea notei trebuie sa fie un numar real\n")
            return
        try:
            self.__srv_note.update_nota(id_nota, valoare)
            print("\nNota modificata cu succes\n")
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __ui_studenti_ordonati_alfabetic(self):
        try:
            id_disc = int(input("Introduceti id-ul disciplinei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        studenti_sorted = self.__srv_note.studenti_alfabetic(id_disc)
        for stud in studenti_sorted:
            print(stud.get_nume())

    def __ui_get_note_la_o_disciplina_alfabetic(self):
        try:
            id_disciplina = int(input("Introduceti id-ul disciplinei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            note_studenti = self.__srv_note.get_note_la_o_disciplina_alfabetic(id_disciplina)
            print(str(note_studenti))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __ui_get__note_la_o_disciplina_dupa_nota(self):
        try:
            id_disciplina = int(input("Introduceti id-ul disciplinei: "))
        except ValueError:
            print("\nId-ul trebuie sa fie un numar intreg\n")
            return
        try:
            note_studenti = self.__srv_note.get_note_la_o_disciplina_dupa_nota(id_disciplina)
            print(str(note_studenti))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __ui_get_20_studenti_nota(self):
        try:
            note_generale = self.__srv_note.get_20_studenti_nota()
            for student in note_generale:
                print(str(student))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

    def __ui_primele_3_disc(self):
        try:
            disciplina_nr_note = self.__srv_note.get_discipline_cele_mai_multe_note()
            #print(str(disciplina_nr_note))
        except RepositoryError as re:
            print("\nrepository error: " + str(re))
        except ValidationError as ve:
            print("\nvalidation error: " + str(ve))

        for el in disciplina_nr_note:
            print(el)

    def __ui_print_note_compus(self):
        #Afiseaza notele
        not_list = self.__srv_note.get_all()
        if len(not_list) == 0:
            print("Nu exista notari. ")
        else:
            print("Lista de notari este: ")
            for el in not_list:
                print(" Studentul ", el.get_id_student(), "are la disciplina", el.get_id_disciplina(), 'nota',
                      el.get_valoare(), 'cu id-ul', el.get_id_nota())

    def __ui_print_note_file(self):
        note = self.__srv_note.get_all_note_file()
        for date_disc in note:
            print(date_disc)
            # print(date_disc[0]+"\n")
            # for student in date_disc[1]:
            #     print("\t"+str(student))

    def __ui_comparare_noua(self):
        # note = self.__srv_note.get_all()
        note = self.__srv_note.comparare_noua_srv()
        # for nota in note:
        #     print(str(nota))
        print(str(note))


    def __ui_tura2_comp_noua(self):
        disc = self.__srv_discipline.tura2_comp_noua()
        for d in disc:
            print(str(d))

    def run (self):
        while True:
            self.__ui_print_meniu()
            operatie = input(">>>\nOptiunea dumneavoastra este:")
            cmd = operatie.split(" ")
            if cmd[0] == "exit":
                return
            if cmd[0] == "":
                continue
            if cmd[0] == "add_student":
                try:
                    self.__ui_adauga_stud()
                    print ("Actualii studenti sunt:")
                    self.__ui_print_studenti()
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("repository error:\n" + str(re))
            elif cmd[0] == "print_studenti":
                self.__ui_print_studenti()
            elif cmd[0] == "add_disciplina":
                try:
                    self.__ui_adauga_disc()
                    print("Actualele discipline sunt:")
                    self.__ui_print_discipline()
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("repository error:\n" + str(re))
            elif cmd[0] == "cauta_student":
                try:
                    print(str(self.__ui_cautare_stud()))
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("Studentul cu id-ul dat nu exista->" + str(re))
            elif cmd[0] == "cauta_disciplina":
                try:
                    print(str(self.__ui_cautare_disc()))
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("Disciplina cu id-ul dat nu exista->" + str(re))
            elif cmd[0] == "modificare_nume_student":
                try:
                    self.__ui_modifica_stud()
                    print("Actualii studenti sunt:")
                    self.__ui_print_studenti()
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("Studentul cu id-ul dat nu exista->" + str(re))
            elif cmd[0] == "modificare_prof_disciplina":
                try:
                    self.__ui_modifica_disc()
                    print("Actualele discipline sunt:")
                    self.__ui_print_discipline()
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("Disciplina cu id-ul dat nu exista->" + str(re))
            elif cmd[0] == "sterge_student":
                try:
                    self.__ui_sterge_stud()
                    print("Actualii studenti sunt:")
                    self.__ui_print_studenti()
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("Studentul cu id-ul dat nu exista->" + str(re))
            elif cmd[0] == "sterge_disciplina":
                try:
                    self.__ui_sterge_disc()
                    print("Actualele discipline sunt:")
                    self.__ui_print_discipline()
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("Disciplina cu id-ul dat nu exista->" + str(re))
            elif cmd[0] == "generate_studenti":
                self.__srv_studenti.generate_random_student(int(cmd[1]))
                #self.__ui_generate_random_students(cmd[1])
                print("Actualii studenti sunt:")
                self.__ui_print_studenti()
            elif cmd[0] == "generate_discipline":
                self.__srv_discipline.generate_random_disciplina(int(cmd[1]))
                print("Actualele discipline sunt:")
                self.__ui_print_discipline()
            elif cmd[0] == "print_discipline":
                self.__ui_print_discipline()

            elif cmd[0] == "add_nota":
                self.__ui_add_nota()
                #self.__ui_print_note_compus()
            elif cmd[0] == "sterge_nota":
                self.__ui_sterge_nota()
                self.__ui_print_note_compus()
            elif cmd[0] == "update_nota":
                self.__ui_update_nota()
                self.__ui_print_note_compus()
            elif cmd[0] == "cauta_nota":
                self.__ui_cauta_nota_dupa_id()
            elif cmd[0] == "statistica1":
                self.__ui_studenti_ordonati_alfabetic()
            elif cmd[0] == "sort_alfabetic":
                self.__ui_get_note_la_o_disciplina_alfabetic()
            elif cmd[0] == "sort_nota":
                self.__ui_get__note_la_o_disciplina_dupa_nota()
            elif cmd[0] == "20%":
                self.__ui_get_20_studenti_nota()
            elif cmd[0] == "top_3":
                self.__ui_primele_3_disc()
            elif cmd[0] == 'print_note':
                self.__ui_print_note_compus()
            elif cmd[0] == "print_note_file":
                self.__ui_print_note_file()
            elif cmd[0] == "comp_noua_rea":
                self.__ui_comparare_noua()
            elif cmd[0] == "cmp_noua":
                self.__ui_tura2_comp_noua()
            else:
                print("comanda invalida!")