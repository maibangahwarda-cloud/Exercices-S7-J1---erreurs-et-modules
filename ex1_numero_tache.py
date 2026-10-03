taches = [" Reviser Python ", " Faire les exercices ", " Lire le cours "]

for i in range(3):
    print(f'{i+1} {taches[i]}')

while(True):
    try:
        numero_taches = int(input("Numero de la tache : "))
    except ValueError as error:
        print(error)

    else:
        if (numero_taches <= 1 and numero_taches <=len(taches)):
         print(taches[numero_taches-1 ])
        break
else:
    
    print(f"Choisissez un numero entre 1 et 3.")

finally : 
("fin_de_la_tentative")        