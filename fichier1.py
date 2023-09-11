#menu d'un restaurant

while True:
    print("--Bienvenue chez Nogaye Foodies--")
    print("---Menu du jour--- ")
    print("taper 1 : pour le Mafé")
    print("taper 2 : pour le riz au poisson")
    print("taper 3 : pour le Domoda")
    print("taper 4 : pour le Yassa")
    Plat= int(input("choisissez un plat :"))
    if Plat == 1:
        print("Votre Mafé sera pret dans quelques minutes")
    if Plat== 2:
        print("Votre riz au poisson sera pret dans quelques minutes") 
    if Plat == 3:
        print("Votre Domoda sera pret dans quelques minutes") 
    if Plat == 4:
        print("Votre Yassa sera pret dans quelques minutes")     
    break
while True:
    demande= input("Voulez-vous un dessert ?:")
    if demande== "yes":
        print("--Choisissez votre dessert--")
        print("taper 1 : pour le jus Bouye")
        print("taper 2 : pour le jus Bissap")
        print("taper 1 : pour le Thé")
        print("taper 1 : pour une boule de glace")
    else:
        print("Merci et à la prochaine")
    Dessert= int(input("choisissez un Dessert :"))
    if Plat == 1:
        print("Votre jus Bouye sera pret dans quelques minutes")
    if Plat== 2:
        print("Votre jus Bissap  sera pret dans quelques minutes") 
    if Plat == 3:
        print("Votre Thé sera pret dans quelques minutes") 
    if Plat == 4:
        print("Votre boule de glace sera pret dans quelques minutes")     
    break
    

