from utils import get_date_month_digit
import pandas as pd

class App():
    def __init__(self) -> None:
        self.data = []
        self.valid_data = []
        self.invalid_data = []

    def format_note(self, matiers) -> dict:
        notes = {
            # "FRANCAIS" : {},
            # "ANGLAIS" : {},
            # "MATH" : {},
            # "SVT" : {},
            # "PC" : {},
            # "HG" : {}
        }
        matiers = matiers.replace('"', "")
        if matiers[-1] != "]":
            matiers += "]"
        matiers = matiers.split("#")
        for matier in matiers :
            nom_matier = ""
            notes_matieres = ""
            for car in matier:
                if car != "[":
                    nom_matier += car
                else :
                    notes_matieres =  matier.replace(nom_matier, "")
                    notes_matieres =  notes_matieres.replace("[", "")
                    notes_matieres =  notes_matieres.replace("]", "")
                    break
            notes_matieres = notes_matieres.replace(" ", "")
            notes_matieres = notes_matieres.split(":")
            notes_devoir = notes_matieres[0]
            notes_devoir = notes_devoir.split("|")
            sum_note_devoir = 0
            for note in notes_devoir :
                note = note.replace(",", ".")
                sum_note_devoir = sum_note_devoir + float(note)
            moyenne_devoir = sum_note_devoir / len(notes_devoir)
            note_exam = 0
            if len(notes_matieres) == 2 :
                note_exam = notes_matieres[1]
            moyenne = (moyenne_devoir + 2 * float(note_exam) ) / 3
                
            nom_matier = nom_matier.strip()
            nom_matier = nom_matier.replace('"', "")
            nom_matier = nom_matier.replace('Science_Physique', "PC")
            nom_matier = nom_matier.replace('Français', "Francais")
            nom_matier = nom_matier.replace('rançais', "Francais")
            notes[nom_matier.upper()] = {}
            notes[nom_matier.upper()]["devoir"] = sum_note_devoir
            notes[nom_matier.upper()]["exam"] = float(note_exam)
            notes[nom_matier.upper()]["moyenne"] = moyenne
            
            
        return notes

    def get_data(self):
        try :
            with open("data/data.csv", "+r") as file:
                for line in file :
                    line = line.split(",")
                    try :
                        notes = self.format_note(line[6])
                    except Exception :
                        notes = {}
                    new_data = {
                        "Code" : line[0],
                        "Numero" : line[1],
                        "Nom" : line[2],
                        "Prenom":line[3],
                        "Date_naissane" : line[4],
                        "Classe" : line[5],
                        "Notes" : notes
                    }
                    self.data.append(new_data)
            del self.data[0]
            # df = pd.DataFrame(self.data)
            # print(df)
        except FileNotFoundError :
            print("Impossible de trouver les donnes")



    def data_to_json(self, data):
        import json
        try :
            with open("data/data.json", "w") as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError :
            print("Impossible de trouver les donnes")
            return False
        return True

    def is_number_valid(self,number) :
        carracters_speciaux = [".", "&", "!", "@", "$", "%", "^", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", '"', "<", ">", ",", "?", "/", " "]
        have_digit = False
        if not str(number).isupper() :
            return False
        if len(number) != 7:
            return False
        for i in range(10):
            for car in str(number) :
                if car == str(i) :
                    have_digit = True
                    break
        for car in str(number) :
            if car in carracters_speciaux :
                return False
        if have_digit ==  False :
            return False
        return True

    def is_first_name_valid(self, first_name):
        if len(str(first_name)) < 3 :
            return False
        if  str(first_name[0]).isdigit() :
            return False
        lettre_in_first_name = []
        for car in str(first_name) :
            if not car.isdigit() :
                lettre_in_first_name.append(car)
        if len(lettre_in_first_name) < 3:
            return False
        return True

    def is_last_name_valid(self, last_name):
        if len(str(last_name)) < 2 :
            return False
        if  str(last_name[0]).isdigit() :
            return False
        lettre_in_last_name = []
        for car in str(last_name) :
            if not car.isdigit() :
                lettre_in_last_name.append(car)
        if len(lettre_in_last_name) < 2:
            return False
        return True
    
    def split_date(self, date: str) -> list:
        date.strip()
        date = date.replace("-", "/")
        date = date.replace(":", "/")
        date = date.replace(",", "/")
        date = date.replace(".", "/")
        date = date.replace("|", "/")
        date = date.replace("_", "/")
        date = date.replace(" ", "/")
        date = date.split('/')
        return date


    def is_date_valid(self, date : str) -> bool:
        date_month_digit = get_date_month_digit()
        date = self.split_date(date)
        # print(date)
        if len(date) != 3:
            return False
        
        jour, mois ,annee = date
        
        if not jour.isdigit() or not annee.isdigit():
            return False
        
        if mois.isdigit() :
            if int(mois) > 12:
                return False
        elif mois.lower() not in date_month_digit.keys() :
            return False
        if int(jour) > 30:
            return False
        return True

    def format_date(self, date):
        date_month_digit = get_date_month_digit()
        splited_date_list =self.split_date(date)
        
        

        if len(splited_date_list[0]) == 1:
            splited_date_list[0] = "0" + splited_date_list[0]
        if len(splited_date_list[2]) == 4 :
            splited_date_list[2] = splited_date_list[2][-2:]

        for key in date_month_digit.keys():
            month = splited_date_list[1]
            digit_month = date_month_digit[key]
            if key == month.lower():
                splited_date_list[1] = digit_month
                
        if len(splited_date_list[1]) == 1:
            splited_date_list[1] = "0" + splited_date_list[1]
            

        if int(splited_date_list[1]) > 12 and int(splited_date_list[0]) < 31 :
            splited_date_list[0], splited_date_list[1] = splited_date_list[1], splited_date_list[0]

        jour, mois,annee = splited_date_list
        date = str(jour) + "/" + str(mois) + "/" + str(annee)
        return date

    def is_class_valid(self, classe):
        classe = classe.strip()
        grades = ["6", "5", "3"]
        lettres = ["A","B", "C", "D"]
        if len(classe) < 3 :
            return False
        if classe[0] not in grades:
            return False
        if classe[-1] not in lettres:
            return False
        return True
    
    def format_classe(self, classe):
        classe = classe.strip()
        to_replace = ["ieme", "eme", "ème", "em"]
        for car in to_replace:
            classe = classe.replace(car, "e")
        classe = classe.replace(" ", "")
        return classe

    def set_invalid_and_valid(self):
        cont_num_val = 0
        cont_num_inval = 0
        self.get_data()
        for element in self.data :
            is_first_name_valide = self.is_first_name_valid(element['Prenom'])
            is_last_name_valid = self.is_last_name_valid(element['Nom'])
            is_num_valid = self.is_number_valid(element['Numero'])
            is_date_valid = self.is_date_valid(element['Date_naissane'])
            is_class_valid = self.is_class_valid(element["Classe"])
            print()
            print("============debut==============")
            print(is_first_name_valide)
            print(is_last_name_valid)
            print(is_num_valid)
            print(is_date_valid)
            print(is_class_valid)
            print("=============fin===============")
            print()
            if is_first_name_valide and is_last_name_valid and is_date_valid and is_num_valid and is_class_valid:
                formated_date = self.format_date(element['Date_naissane'])
                formated_classe = self.format_classe(element["Classe"])
                element['Date_naissane'] = formated_date
                element["Classe"] = formated_classe
                
                self.valid_data.append(element)
                cont_num_val += 1
            else :
                self.invalid_data.append(element)
                cont_num_inval +=1
        print(f"-----------> {cont_num_val} valides" )
        print(f"-----------> {len(self.valid_data)} valides" )
        print(f"-----------> {cont_num_inval} invalides" )
        print(f"-----------> {len(self.invalid_data)} invalides" )
        print(f"-----------> {len(self.data)} au total" )
        print(f"-----------> {len(self.valid_data) + len(self.invalid_data)} au total" )
        # print(self.valid_data)
        # print()
        # print(self.invalid_data)
        
        