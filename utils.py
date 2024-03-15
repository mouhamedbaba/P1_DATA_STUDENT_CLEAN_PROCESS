# def get_date_month_digit() -> dict:
#     date_month_digit = {
#             "janvier" : "01",
#             "fevrier" : "02",
#             "mars" : "03",
#             "avril" : "04",
#             "mai" : "05",
#             "juin" : "06",
#             "juillet" : "07",
#             "aout" : "08",
#             "septembre" : "09",
#             "octobre" : "10",
#             "novembre" : "11",
#             "decembre" : "12"
#         }
#     return date_month_digit

# # PRCEDURE pour afficher un menu 
# def display_menu(menu: dict, choix = "CHOIX", ul_dec ="bullet") -> str:

#     bull = "○ "
#     b_s = "bullet"
#     empty = ""
#     print(f"""
#         ========================>  {choix.upper()} DISPONIBLES   <=========================
#     """.upper())
#     for i in menu.keys():
#         print(f"{bull if ul_dec == b_s else empty}{i:6} : {menu[i]} ")
        
# def get_int(prompt: str = "\nVeuillez entre un entier : ", ispositif: bool = False, limit:int | None = None) -> int:
#     number = input(prompt)
#     if number == "":
#         input("\nLa chaine ne peut pas etres vide, reessayer : ")
#         number = get_int(prompt, ispositif, limit)
#     if str(number).isdigit() == False:
#         print("\nVeuillez entre un entier : ")
#         number = get_int(prompt, ispositif, limit)
#     if limit != None and str(number).isdigit():
#         if int(number) > limit :
#             print(f"\nL'entier ne doit pas deppaser {limit} : ")
#             number = get_int(prompt, ispositif, limit)
#     if ispositif == True :
#         if int(number) < 0 and str(number).isdigit():
#             print("\nVeuillez entre un entier positif: ")
#             number = get_int(prompt, ispositif, limit)
#     return int(number)

# def get_str(prompt: str = "\nVeuillez entre un entier : ", limit : int | None = None) :
#     chaine = input(prompt)
#     message  = "\nVeuillez entre un chaine valide : "
#     alphab = [chr(i) for i in range(65, 91)]
#     have_car = False
#     for car in chaine :
#         if car.upper() in alphab:
#             have_car =True
#             break
#     if str(chaine).isdigit() or (limit != None and len(chaine) > limit) or have_car == False :
#         print(message)
#         chaine = get_str(prompt, limit)
#     return chaine