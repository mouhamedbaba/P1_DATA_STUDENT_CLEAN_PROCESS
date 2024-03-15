# from utils import get_date_month_digit, display_menu, get_int
# import os
# import csv

class Manage():
#     def __init__(self) -> None:
#         """
#         Constructeur pour initialiser la classe avec des listes vides pour data, valid_data et invalid_data.
#         """
#         self.data = []
#         self.valid_data = []
#         self.invalid_data = []

#     def extract_notes(self, matiers):  ...
    
#     def format_note(self,matiers : str) -> dict:
#         notes = {
#             "FRANCAIS" : {},
#             "ANGLAIS" : {},
#             "MATH" : {},
#             "SVT" : {},
#             "PC" : {},
#             "HG" : {}
#         }
        
#         matiers = matiers.replace('"', "")
#         matiers = matiers.replace(" ", "")
#         if matiers[-1] != "]":
#             matiers += "]"
#         matiers = matiers.split("#")
#         for i in range(len(matiers)) :
#             if matiers[i] == "" or matiers[i] == "]":
#                 del matiers[i]
        
#         moyenne_general = 0
#         for matier in matiers :
#             nom_matier = ""
#             notes_matieres = ""
#             for car in matier:
#                 if car != "[":
#                     nom_matier += car
#                 else :
#                     notes_matieres =  matier.replace(nom_matier, "")
#                     notes_matieres =  notes_matieres.replace("[", "")
#                     notes_matieres =  notes_matieres.replace("]", "")
#                     break
#             notes_matieres = notes_matieres.replace(" ", "")
#             notes_matieres = notes_matieres.split(":")
#             notes_devoir = notes_matieres[0]
#             notes_devoir = notes_devoir.split("|")
#             sum_note_devoir = 0
#             formated_note_devoir = []
#             for note in notes_devoir :
#                 note = note.replace(",", ".")
#                 note = note.replace(" ", "")
#                 if note != "" :
#                     formated_note_devoir.append(float(note))
#                     note = float(note)
#                     sum_note_devoir = sum_note_devoir + note
#             moyenne_devoir = sum_note_devoir / len(notes_devoir)
#             note_exam = 0
#             if len(notes_matieres) == 2 :
#                 note_exam = notes_matieres[1]
#                 # print(note_exam)
#             if note_exam != "" :
#                 note_exam = float(note_exam)
#             moyenne = (moyenne_devoir + 2 * note_exam ) / 3
                
#             nom_matier = nom_matier.strip()
#             nom_matier = nom_matier.replace('"', "")
#             nom_matier = nom_matier.replace('Science_Physique', "PC")
#             nom_matier = nom_matier.replace('FRANÇAIS', "FRANCAIS")
#             nom_matier = nom_matier.replace('ç', "c")
#             nom_matier = nom_matier.replace('cc', "c")
#             if nom_matier == "rancais" :
#                 nom_matier = "FRANCAIS"
#             nom_matier = nom_matier.upper()
#             notes[nom_matier]["devoir"] = formated_note_devoir
#             notes[nom_matier]["exam"] = note_exam
#             notes[nom_matier]["moyenne"] = moyenne
#             moyenne_general += moyenne
#         moyenne_general /= 6
#         notes["moyenne_general"] = moyenne_general
#         return notes

#     def is_note_valide(self, notes: dict) -> bool : 
#         if notes["moyenne_general"] < 1 :
#             return False
#         return True

#     def get_data(self):
#         cont = 0 
#         try :
#             with open("data/data.csv", "+r") as file:
#                 file = csv.reader(file , delimiter=",")
#                 i_id = -1
#                 for line in file :
#                     # line = line.split(",")
#                     try :
#                         # print(line[6])
#                         notes = self.format_note(line[6])
#                     except Exception as e:
#                         # print(cont, "failed ---->" ,{line[6]}, "----->", e)
#                         # print(line[6])
#                         cont += 1
#                         notes = {
#                             "FRANCAIS" : {},
#                             "ANGLAIS" : {},
#                             "MATH" : {},
#                             "SVT" : {},
#                             "PC" : {},
#                             "HG" : {},
#                             "moyenne_general" : 0
#                         }
#                     classe =  self.format_classe(line[5])
#                     try :
#                         date = self.format_date(line[4])
#                     except Exception:
#                         date = line[4]
                    
#                     new_data = {
#                         "id" : i_id,
#                         "Code" : line[0].strip(),
#                         "Numero" : line[1].strip(),
#                         "Nom" : line[2].strip(),
#                         "Prenom":line[3].strip(),
#                         "Date_naissane" : date.strip(),
#                         "Classe" : classe,
#                         "Notes" : notes
#                     }
#                     if line[1] != "":
#                         self.data.append(new_data)
#                         i_id += 1 
#             del self.data[0]
#         except FileNotFoundError :
#             print("Impossible de trouver les donnes")

#     def data_to_json(self, data : list, file_name: str) -> bool:
#         import json
#         try :
#             with open(f"data/{file_name}", "w") as f:
#                 json.dump(data, f, indent=4)
#         except FileNotFoundError :
#             print("Impossible de trouver les donnes")
#             return False
#         return True

#     def is_number_valid(self,number : str) -> bool:
#         carracters_speciaux = [".", "&", "!", "@", "$", "%", "^", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", '"', "<", ">", ",", "?", "/", " "]
#         have_digit = False
#         if not str(number).isupper() :
#             return False
#         if len(number) != 7:
#             return False
#         for i in range(10):
#             for car in str(number) :
#                 if car == str(i) :
#                     have_digit = True
#                     break
#         for car in str(number) :
#             if car in carracters_speciaux :
#                 return False
#         if have_digit ==  False :
#             return False
#         return True

#     def is_first_name_valid(self, first_name : str) -> bool:
#         if len(str(first_name)) < 3 :
#             return False
#         if  str(first_name[0]).isdigit() :
#             return False
#         lettre_in_first_name = []
#         for car in str(first_name) :
#             if not car.isdigit() :
#                 lettre_in_first_name.append(car)
#         if len(lettre_in_first_name) < 3:
#             return False
#         return True

#     def is_last_name_valid(self, last_name : str) -> bool:
#         if len(str(last_name)) < 2 :
#             return False
#         if  str(last_name[0]).isdigit() :
#             return False
#         lettre_in_last_name = []
#         for car in str(last_name) :
#             if not car.isdigit() :
#                 lettre_in_last_name.append(car)
#         if len(lettre_in_last_name) < 2:
#             return False
#         return True
    
#     def split_date(self, date: str) -> list:
#         date.strip()
#         to_replace = ["-", ":", ",", ".", "|", "_", " "]
#         for car in date :
#             if car in to_replace:
#                 date = date.replace(car, "/")
#         date = date.split('/')
#         return date

#     def is_date_valid(self, date : str) -> bool:
#         date_month_digit = get_date_month_digit()
#         date = self.split_date(date)
#         # print(date)
#         if len(date) != 3:
#             return False
        
#         jour, mois ,annee = date
        
#         if not jour.isdigit() or not annee.isdigit():
#             return False
        
#         if mois.isdigit() :
#             if int(mois) > 12:
#                 return False
#         elif mois.lower() not in date_month_digit.keys() :
#             return False
#         if int(jour) > 30:
#             return False
#         return True

#     def format_date(self, date : str) -> str:
#         date_month_digit = get_date_month_digit()
#         splited_date_list =self.split_date(date)


#         if len(splited_date_list[0]) == 1:
#             splited_date_list[0] = "0" + splited_date_list[0]
#         if len(splited_date_list[2]) == 4 :
#             splited_date_list[2] = splited_date_list[2][-2:]

#         for key in date_month_digit.keys():
#             month = splited_date_list[1]
#             digit_month = date_month_digit[key]
#             if key == month.lower():
#                 splited_date_list[1] = digit_month
                
#         if len(splited_date_list[1]) == 1:
#             splited_date_list[1] = "0" + splited_date_list[1]
            

#         if int(splited_date_list[1]) > 12 and int(splited_date_list[0]) < 31 :
#             splited_date_list[0], splited_date_list[1] = splited_date_list[1], splited_date_list[0]

#         jour, mois,annee = splited_date_list
#         date = str(jour) + "/" + str(mois) + "/" + str(annee)
#         return date

#     def is_class_valid(self, classe: str)-> bool:
#         classe = classe.strip()
#         grades = ["6", "5", "3", "4"]
#         lettres = ["A","B", "C", "D"]
#         if len(classe) < 3 :
#             return False
#         if classe[0] not in grades:
#             return False
#         if classe[-1].upper() not in lettres:
#             return False
#         return True

#     def format_classe(self, classe : str) -> str:
#         classe = classe.strip()
#         if len(classe) > 2:
#             s = classe[0]
#             f = classe[-1]
#             classe = s + "ieme" + f
#         return classe

#     def set_invalid_and_valid(self):
#         self.get_data()
#         for element in self.data :
#             element["Invalid_colums"] = self.get_invalid_cols(element)
#             invalid_cols = element["Invalid_colums"]
            
#             if len(invalid_cols) == 0:
#                 formated_date = self.format_date(element['Date_naissane'])
#                 formated_classe = self.format_classe(element["Classe"])
#                 element['Date_naissane'] = formated_date
#                 element["Classe"] = formated_classe
#                 self.valid_data.append(element)
#             else :
#                 self.invalid_data.append(element)
#         self.data_to_json(self.invalid_data, "invalid_data.json")
#         self.data_to_json(self.valid_data, "valid_data.json")
#         self.data_to_json(self.data, "data.json")
#         print()
#         print(f"-----------> {len(self.invalid_data):5} invalides" )
#         print(f"-----------> {len(self.valid_data):5} valides" )
#         print(f"-----------> {len(self.data):5} au total" )

#     def display_menu(self) -> str:
#         menu = {
#             "1" : "Afficher les informations valides",
#             "2" : "Afficher les informations invalides", 
#             "3" : "Rechercher par Numero" ,
#             "4" : "Afficher les 5 premiers" ,
#             "5" : "Ajouter une information",
#             "6" : "Modifier une information",
#             "7" : "Paginer par 5",
#             "8" : "Donner un Nombre pour paginer",
#             "9" : "Netoyer le Terminal",
#             "0" : "Sortir"
#         }
#         display_menu(menu, ul_dec="")
#         print()
#         option = input("Veuillez choisir une option : ")
#         return option

#     def display_note(self, matiere: dict):
#         try :
#             moyenne = matiere["moyenne"]
#             print(f"{moyenne:10.2f}" ,end=" | \t")
#         except Exception:
#             empty = ""
#             print(f"{empty:10}" ,end=" | \t")

#     def display_info(self, data : list):
#         tabs = ["Numero", "Penom", "Nom", "Classe", "Date" , "Francais", "Anglais", "Maths", "PC", "SVT", "HG" , "Moyenne"]
#         if len(data) == 0 :
#             print()
#             print("-"*188)
#             for tab in tabs :
#                 print(f"{tab:10}" ,end=" | \t") 
#             print('')
#             print("-"*188)
#             print("\t\t\t\t \t\t\t\t\t  PAS DE DONNES TROUVE  ",  end="\t\t\t\t\t\t\t\t\t   |")
#             print()
#             print("-"*188)
#             return
#         print()
#         print("-"*188)
#         for tab in tabs :
#             print(f"{tab:10}" ,end=" | \t") 
#         print('')
#         print("-"*188)
#         for element in data:
#             first_name = element["Prenom"]
#             last_name = element["Nom"]
#             numero = element["Numero"]
#             classe = element["Classe"] 
#             date = element["Date_naissane"] 
#             francais = element["Notes"]["FRANCAIS"]
#             angalis = element["Notes"]["ANGLAIS"]
#             maths = element["Notes"]["MATH"]
#             pc = element["Notes"]["PC"]
#             svt = element["Notes"]["SVT"]
#             hg = element["Notes"]["HG"]
#             mg = element["Notes"]["moyenne_general"]
            
#             print(f"{numero:10}" ,end=" | \t")
#             print(f"{first_name:10}" ,end=" | \t")
#             print(f"{last_name:10}" ,end=" | \t")
#             print(f"{classe:10}" ,end=" | \t")
#             print(f"{date:10}" ,end=" | \t")
#             self.display_note(francais)
#             self.display_note(angalis)
#             self.display_note(maths)
#             self.display_note(pc)
#             self.display_note(svt)
#             self.display_note(hg)
#             print(f"{mg:10.2f}" ,end=" | \t")
#             print('')
#             print("-"*188)
#         print()
#         print(f"shape ({len(data)}, {len(tabs)})")
#         print()

    def search_by_num(self, data : list, num : str) -> list:
        # num = input("\nVeuillez saisir le numero de l'etudiant a rechercher : ")
        result = []
        num = num.upper()
        for element in data :
            if num in element["Numero"].upper() or num  in element["Prenom"].upper() or num in element["Nom"].upper():
                result.append(element)
        return result[:10]

#     def calcul_moyenne(self, moyenne_devoir, note_exam, ) -> float:
#         moyenne = (moyenne_devoir + 2 * float(note_exam) ) / 3
#         return moyenne

#     def get_notes(self) -> dict :
#         devoir_francais = get_int("\nMoyenne du devoir en francais (0 si pas de note): ", limit=20, ispositif=True)
#         exam_francais = get_int("\nNote exam du devoir en francais (0 si pas de note): ", limit=20, ispositif=True)
#         devoir_anglais = get_int("\nMoyenne du devoir en anglais (0 si pas de note): ", limit=20, ispositif=True)
#         exam_anglais = get_int("\nNote exam du devoir en anglais (0 si pas de note): ", limit=20, ispositif=True)
#         devoir_maths = get_int("\nMoyenne du devoir en maths (0 si pas de note): ", limit=20, ispositif=True)
#         exam_maths = get_int("\nNote exam du devoir en maths (0 si pas de note): ", limit=20, ispositif=True)
#         devoir_svt = get_int("\nMoyenne du devoir en svt (0 si pas de note): ", limit=20, ispositif=True)
#         exam_svt = get_int("\nNote exam du devoir en svt (0 si pas de note): ", limit=20, ispositif=True)
#         devoir_pc = get_int("\nMoyenne du devoir en pc (0 si pas de note): ", limit=20, ispositif=True)
#         exam_pc = get_int("\nNote exam du devoir en pc (0 si pas de note): ", limit=20, ispositif=True)
#         devoir_hg = get_int("\nMoyenne du devoir en hg (0 si pas de note): ", limit=20, ispositif=True)
#         exam_hg = get_int("\nNote exam du devoir en hg (0 si pas de note): ", limit=20, ispositif=True)
            
#         moyenne_francais = self.calcul_moyenne(devoir_francais, exam_francais)
#         moyenne_anglais = self.calcul_moyenne(devoir_anglais, exam_anglais)
#         moyenne_maths = self.calcul_moyenne(devoir_maths, exam_maths)
#         moyenne_svt = self.calcul_moyenne(devoir_svt, exam_svt)
#         moyenne_pc = self.calcul_moyenne(devoir_pc, exam_pc)
#         moyenne_hg = self.calcul_moyenne(devoir_hg, exam_hg)
#         moyenne_general = (moyenne_francais + moyenne_anglais + moyenne_hg + moyenne_maths + moyenne_pc + moyenne_svt) / 6
#         notes = {
#                 "FRANCAIS" : {
#                     "devoir": devoir_francais,
#                     "exam": exam_francais,
#                     "moyenne": moyenne_francais
#                     },
#                 "ANGLAIS" : {
#                 "devoir": devoir_anglais,
#                 "exam": exam_anglais,
#                 "moyenne": moyenne_anglais
#                     },
#                 "MATH" : {
#                 "devoir": devoir_maths,
#                 "exam": exam_maths,
#                 "moyenne": moyenne_maths
#                 },
#                 "SVT" : {
#                 "devoir": devoir_svt,
#                 "exam": exam_svt,
#                 "moyenne": moyenne_svt
#                 },
#                 "PC" : {
#                 "devoir":devoir_pc,
#                 "exam": exam_pc,
#                 "moyenne": moyenne_pc
#                 },
#                 "HG" : {
#                 "devoir": devoir_hg,
#                 "exam": exam_hg,
#                 "moyenne": moyenne_hg
#                 },
#                 "moyenne_general" : moyenne_general
#         }
#         return notes

#     def get_num(self) -> str:
#         while True :
#             num = input("\nEntrer le numero de l'etudiant : ")
#             if self.is_number_valid(num) :
#                 break
#             else :
#                 print("\nNumero invalide reesayer")
#         return num

#     def get_first_name(self) -> str:
#         while True :
#             prenom = input("\nEntrer le prenom de l'etudiant : ")
#             if self.is_first_name_valid(prenom):
#                 break
#             else :
#                 print("\nPrenom invalide reesayer")
#         return prenom

#     def get_last_name(self) -> str:
#         while True :
#             nom = input("\nEntrer le nom de l'etudiant : ")
#             if self.is_last_name_valid(nom):
#                 break
#             else :
#                 print("\nNom invalide reesayer")
#         return nom

#     def get_classe(self) -> str:
#         while True :
#             classe = input("\nEntrer la classe de l'etudiant : ")
#             if self.is_class_valid(classe):
#                 break
#             else :
#                 print("\nClasse invalide reesayer")
#         return classe

#     def get_date(self) -> str:
#         while True :
#             date = input("\nEntrer la date de l'etudiant : ")
#             if self.is_date_valid(date):
#                 break
#             else :
#                 print("\nDate invalide reesayer")
#         return date

#     def get_inforamtion(self) -> dict :
#         num = self.get_num()
#         prenom = self.get_first_name()
#         nom = self.get_last_name()
#         classe = self.get_classe()
#         date = self.get_date()
#         notes = self.get_notes()
#         new_data = {
#             "id" : self.data[-1]["id"] + 1 ,
#             "Code" : "BNT021",
#             "Numero" : num,
#             "Nom" : nom,
#             "Prenom": prenom,
#             "Date_naissane" : self.format_date(date),
#             "Classe" : self.format_classe(classe),
#             "Notes" : notes
#                 }
#         return new_data

#     def add_informations(self):
#         data = self.get_inforamtion()
#         list_data = []
#         list_data.append(data)
#         self.get_data()
#         self.data.append(data)
#         self.valid_data.append(data)
#         self.data_to_json(self.data, "data.json")
#         self.data_to_json(self.valid_data, "valid_data.json")
#         print("Etudiant ajouter avec succes")
#         self.display_info(list_data)

#     def five_first(self) -> list:
#         sorted_data = sorted(self.valid_data, key=lambda x: x["Notes"]["moyenne_general"], reverse=True)
#         first_five = sorted_data[:5]
#         return first_five

#     def get_invalid_cols(self, line : dict) -> list:
#         invalid_colums = []
#         prenom = line["Prenom"]
#         nom = line["Nom"]
#         num = line["Numero"]
#         classe = line["Classe"]
#         date = line["Date_naissane"]
#         notes = line["Notes"]
#         if self.is_number_valid(num) == False :
#             invalid_colums.append("Numero")
#         if self.is_first_name_valid(prenom) == False :
#             invalid_colums.append("Prenom")
#         if self.is_last_name_valid(nom) == False :
#             invalid_colums.append("Nom")
#         if self.is_class_valid(classe) == False :
#             invalid_colums.append("Classe")
#         if self.is_date_valid(date) == False :
#             invalid_colums.append("Date_naissane")
#         if self.is_note_valide(notes) == False :
#             invalid_colums.append("Notes")
#         return invalid_colums

#     def set_modifiactions(self, invalid_cols : list, line : dict):
#         prenom = line["Prenom"]
#         nom = line["Nom"]
#         numero = line["Numero"]
#         num = line["Numero"]
#         classe = line["Classe"]
#         date = line["Date_naissane"]
#         notes = line["Notes"]
#         if "Numero" in invalid_cols :
#             num = self.get_num()
#         if "Prenom" in invalid_cols :
#             prenom = self.get_first_name()
#         if "Nom" in invalid_cols :
#             nom = self.get_last_name()
#         if "Classe" in invalid_cols :
#             classe = self.get_classe()
#             classe=  self.format_classe(classe)
#         if "Date_naissane" in invalid_cols:
#             date = self.get_date()
#             date = self.format_date(date)
#         if "Notes" in invalid_cols:
#             notes = self.get_notes()
#         i = -1
#         print()
#         for data in self.invalid_data :
#             i += 1
#             if numero == data["Numero"] :
#                 data["Numero"] = num
#                 data["Prenom"] = prenom
#                 data["Nom"] = nom
#                 data["Classe"] = classe
#                 data["Date_naissane"] = date
#                 date["Notes"] = notes
#                 self.valid_data.append(data)

#                 del self.invalid_data[i]

#     def modif_invalid_inf(self) : 
#         data = self.search_by_num(self.invalid_data)
#         if len(data) > 0 :
#             self.display_info(data)
#             line=data[0]
#             invalid_cols = self.get_invalid_cols(line)
#             print("Colone(s) invalide(s) : ------> " , end=" ")
#             for col in invalid_cols :
#                 print(col , end=", " )
#             self.set_modifiactions(invalid_cols, line)

#         else :
#             print("\nCette Etudiant n'existe pas ou contient des informations invalides ! ")

#     def paginate(self, fixed_max_h : int = 5):
#         min_l = 0
#         max_l = fixed_max_h
#         data = self.valid_data[:]
#         while True:
#             os.system("clear")
#             data_to_display = data[min_l:max_l]
#             self.display_info(data_to_display)
#             print(f"{max_l if max_l < len(data) else len(data)} / {len(data)}")
#             print()
#             if max_l <= len(data) :
#                 print("1 : Suivant")
#             if  min_l > 0 :
#                 print("2 : Precedant")
#             print("0 : Sortir de la pagination")
#             print()
#             option = input("Option : ")
#             if option == "1" and max_l <= len(data):
#                 min_l = max_l
#                 max_l += fixed_max_h
#             elif option == "2" and  min_l > 0 :
#                     max_l = min_l
#                     min_l -= fixed_max_h
#             elif option == "0":
#                 os.system("clear")
#                 break
#             else :
#                 print("Option non valide")

#     def run(self):
#         os.system("clear")
#         self.set_invalid_and_valid()
#         while True :
#             # self.display_info(self.data)
#             option = self.display_menu()
#             if option == "1":
#                 self.display_info(self.valid_data)
#             elif option == "2":
#                 self.display_info(self.invalid_data)
#             elif option == "3":
#                 num = input("\nEntrer le numero de l'etudiant : ")
#                 data = self.search_by_num(self.data, num)
#                 self.display_info(data)
#             elif option == "4":
#                 result = self.five_first()
#                 self.display_info(result)
#             elif option == "5":
#                 self.add_informations()
#             elif option == "6": 
#                 self.modif_invalid_inf()
#             elif option == "7":
#                 self.paginate()
#             elif option == "8":
#                 fix_max_l = get_int("\nVeillez entrer le nombre de ligne que vous voulez paginer : ")
#                 self.paginate(fixed_max_h=fix_max_l)
#             elif option == "9":
#                 os.system("clear")
#             elif option == "0":
#                 print("AU REVOIR")
#                 break
#             else :
#                 print("Option non valide")