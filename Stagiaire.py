class Stagiaire:
    nombre_stagiaires = 0
    liste_stagiaires = []
    def __init__(self, nom:str=None, prenom:str=None, filiere:str=None, note1:float=None, note2:float=None, note3:float=None):
        self.__matricule = Stagiaire.nombre_stagiaires
        self.__nom = nom
        self.__prenom = prenom
        self.__filiere = filiere
        self.__note1 = note1
        self.__note2 = note2
        self.__note3 = note3
        Stagiaire.nombre_stagiaires += 1
        Stagiaire.liste_stagiaires.append(self)

    def __del__(self):
        Stagiaire.nombre_stagiaires -= 1

    def __str__(self):
        return "Matricle: {}, Nom: {}, Prenom: {}, Filiere: {}, Note1: {}, Note2: {}, Note3: {}".format(self.__matricule, self.__nom, self.__prenom, self.__filiere, self.__note1, self.__note2, self.__note3)

    def __eq__(self, other):
        return self.matricule == other.matricule

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, matricule):
        self.__matricule=matricule

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    @property
    def filiere(self):
        return self.__filiere

    @filiere.setter
    def filiere(self, filiere):
        self.__filiere = filiere

    @property
    def note1(self):
        return self.__note1

    @note1.setter
    def note1(self, note1):
        self.__note1 = note1

    @property
    def note2(self):
        return self.__note2

    @note2.setter
    def note2(self, note2):
        self.__note2 = note2

    @property
    def note3(self):
        return self.__note3

    @note3.setter
    def note3(self, note3):
        self.__note3 = note3

    # methode qui calcul la moyenne d'un stagiaire
    def calcul_moyenne(self):
        return (self.__note1 + self.__note2 + self.__note3) / 3

    # methode qui rechercher un stagiaire par son nom
    @classmethod
    def rechercher_stagiaire(cls, nom:str):
        for stagiaire in cls.liste_stagiaires:
            if stagiaire.nom == nom:
                return stagiaire

    # methode qui supprimer un stagiaire
    @classmethod
    def supprimer_stagiaire(cls, nom):
        if cls.rechercher_stagiaire(nom) is not None:
            cls.liste_stagiaires.remove(cls.rechercher_stagiaire(nom))
        else:
            print(f"Stagiaire '{nom}' n'existe pas")

    # methode qui afficher la meilleure moyenne
    @classmethod
    def meilleure_moyenne(cls):
        moyenne = 0
        meilleur_stagiaire = None
        for stagiaire in cls.liste_stagiaires:
            if stagiaire.calculMoyenne() > moyenne:
                moyenne = stagiaire.calcul_moyenne()
                meilleur_stagiaire = stagiaire
        return meilleur_stagiaire

    # methode qui afficher les stagiaires
    @classmethod
    def afficher_stagiaires(cls):
        if len(cls.liste_stagiaires) == 0:
            print("Aucun stagiaire")
        else:
            for stagiaire in cls.liste_stagiaires:
                print(stagiaire)





