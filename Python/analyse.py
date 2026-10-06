#importation des données encadrements montpellier 2023 pour avoir le prix moyen médian des studio et T1

import pandas as pd
df = pd.read_excel(r"C:\Users\kenfa\OneDrive\Bureau\meublé-non meublé.xlsx")
donnees=df[["nombre_de_piece","prix_med","meuble"]]

#filtrer les t1 et ou studio avec le prix médian au mètre carré

t1=donnees[donnees["nombre_de_piece"]=="1"]

#séparer meublé et non meublé

meuble=t1[t1["meuble"]==True]
non_meuble=t1[t1["meuble"]==False]

#importation de données provennant d'observatoire des loyers montpellier pour extraire la superficie moyenne des studio

L25=pd.read_excel(r"C:\\Users\\kenfa\\OneDrive\\Bureau\\Loyer 2025.xls")
L24=pd.read_excel(r"C:\Users\kenfa\OneDrive\Bureau\Loyer 2024.xlsx")
L23=pd.read_excel(r"C:\Users\kenfa\OneDrive\Bureau\Loyer 2023.xlsx")

#Fusion des données de 2025 2024 et 2024

fusion=pd.concat([L25,L24,L23])

#extraction des studios ou T1 pour la superficie

superficie_t1=fusion[fusion["nombre_pieces_local"]=="Appart 1P"]

#importation des données sur les charges 

charge=pd.read_excel(r"C:\Users\kenfa\OneDrive\Bureau\charges.xlsx")

#importation du panier d'équipement étudiant 

panier=pd.read_excel(r"C:\Users\kenfa\OneDrive\Bureau\Panier_amenagement_studio_etudiant.xlsx")

#Calcul du prix au mètre carré hors charge

prix_meuble=meuble["prix_med"].mean()
prix_non_meuble=non_meuble["prix_med"].mean()

#Calcul de la Superficie moyenne T1 ou Studio

Superficie=superficie_t1 ["surface_moyenne"].mean()

#Estimation des charges

C=charge["Charges"].mean()

#Calcul du montant de loyer typique

Loyer_meuble=prix_meuble*Superficie+C
Loyer_non_meuble=prix_non_meuble*Superficie +C

#Cout d'aménagement typique

amenagement=panier ["Prix median"].sum()

#Point de bascul

point_bascule=amenagement/(12*(Loyer_meuble-Loyer_non_meuble))

#tableau por enregistrer les paramètre

parametre = []
parametre.append([Loyer_meuble,Loyer_non_meuble,amenagement,point_bascule])
tableau1=pd.DataFrame(parametre,columns=["Loyer_meuble","Loyer_non_meuble","Montant_aménagement","point_bascule"])

#Evolution des dépenses en cout cumulé

resultat = []
for annee in range(1,21):
    mois=annee*12
    cout_meuble=mois*Loyer_meuble 
    cout_non_meuble=mois*Loyer_non_meuble + amenagement
    if cout_non_meuble>cout_meuble:
      ecart=cout_non_meuble-cout_meuble
    else :
      ecart=cout_meuble-cout_non_meuble
    resultat.append([annee, cout_meuble, cout_non_meuble, ecart])

 #tableau pour enregistré les cout cumulé

tableau2 = pd.DataFrame(resultat, columns=["Annee", "Cout_meuble", "Cout_non_meuble", "Ecart"])
print(point_bascule)
print(type(point_bascule))