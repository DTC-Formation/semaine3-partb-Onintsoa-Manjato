contacts = []
contact = {}
user_input = input("Gestion des contacts : \n ___________________ \n\nEntrer ce que vous voulez faire (ajouter/afficher/rechercher/supprimer/quiter) : ")
while True :
#Ajouter
    if user_input  == "ajouter" :
        nom_input = input("Entrez le nom : ")
        prenom_input = input("Entrez le prénom : ")
        num_input = input("Entrez le numéro de téléphone : ")
        #Le numero doit etre des chiffres
        if num_input.isdigit() :
            contact = {"Nom" : nom_input, "Prénom" : prenom_input, "Téléphone" : num_input}
            contacts.append(contact)
            print("Le contact a été ajouté avec succès !\n")
        else :
            print("\nVerifier le numero que vous avez entrez\n")
#Afficher
    elif user_input == "afficher" : 
        if not contacts :
            print("Le contact est vide")
        else :
            print("contacts : ")
            for x in contacts :
                print(x, "\n")
#Rechercher
    elif user_input == "rechercher" :
        contact_a_rech = input("Entrer le nom du contact à rechercher : ")
        strcontact = str(contacts)
        if contact_a_rech in strcontact :
            print("contacts : ")
            for y in contacts :
                for key, val in y.items() :
                    if val == contact_a_rech :
                        print(y, "\n")
        else :
            print(contact_a_rech ,"n'est pas dans la liste des contacts\n")
#Supprimer
    elif user_input == "supprimer":
        contact_a_sup = input("Entrer le contact à supprimer : ")
        strcontact = str(contacts)
        if contact_a_sup in strcontact :
            for y in contacts :
                for key, val in y.items() :
                    if val == contact_a_sup :
                        contacts.remove(y)
                        print(y, "est supprimé de la liste des contacts\n")
        else :
            print(contact_a_sup ,"n'est pas dans la liste des contacts") 
#Quiter      
    elif user_input == "quiter" :
        print("___Bye___")
        break
#Saisie n'importe quoi
    else :
        print("Verifier votre saisie\n")
    user_input = input("Entrer ce que vous voulez faire (ajouter/afficher/rechercher/supprimer/quiter) : ")
