from gestion_stagiaires.Stagiaire import Stagiaire


while True:
    print("""
    1-Afficher tous les stagiaires
    2-Ajouter un stagiaire
    3-Rechercher un stagiaire
    4-Modifier un stagiaire
    5-Supprimer un stagiaire
    6-Afficher la meilleure moyenne parmi tous les stagiaires
    7-Quitter
    """)

    choix=input("Votre choix: ")

    if choix=="1":
        Stagiaire.afficher_stagiaires()

    elif choix=="2":
        nouveau_stagiaire=Stagiaire()
        nouveau_stagiaire.nom = input("Nouveau Nom: ")
        nouveau_stagiaire.prenom = input("Nouveau Prenom: ")
        nouveau_stagiaire.note1 = float(input("Nouveau Note1: "))
        nouveau_stagiaire.note2 = float(input("Nouveau Note2: "))
        nouveau_stagiaire.note3 = float(input("Nouveau Note3: "))

    elif choix=="3":
        while True:
            nom_rechercher=input("Le nom du stagiaire vous devez rechercher. pour quitter[x] : ")
            stagiaire_rechercher=Stagiaire.rechercher_stagiaire(nom_rechercher)
            if stagiaire_rechercher is not None:
                print(stagiaire_rechercher)
            else:
                print(f"\nStagiaire '{nom_rechercher}' n'existe pas\n")

            if nom_rechercher.lower()=="x":
                break

    elif choix=="4":
        nom_encienne=input("Le nom du stagiaire vous devez modifier : ")
        stagiaire_modifie= Stagiaire.rechercher_stagiaire(nom_encienne)
        if stagiaire_modifie is None:
            print("\nLe stagiaire n'existe pas\n")
        else:
            stagiaire_modifie.nom=input("Nouveau Nom: ")
            stagiaire_modifie.prenom=input("Nouveau Prenom: ")
            stagiaire_modifie.note1=float(input("Nouveau Note1: "))
            stagiaire_modifie.note2=float(input("Nouveau Note2: "))
            stagiaire_modifie.note3=float(input("Nouveau Note3: "))

    elif choix=="5":
        while True:
            nom_supprimer = input("Le nom du stagiaire vous devez supprimer. pour quitter[x]: ")
            Stagiaire.supprimer_stagiaire(nom_supprimer)
            if nom_supprimer.lower()=="x":
                break

    elif choix=="6":
        print(Stagiaire.meilleure_moyenne())

    elif choix=="7":
        break
