contacts = []
contact = {}

user_input = input("Voulez-vous ajouter un contact ou afficher la liste des contacts ? (ajouter/afficher) :")
while user_input == ("ajouter" or "afficher") :
    contacts.append(contact) 
    
    if user_input == "ajouter" :
        nom_input = input("Entrez le nom : ")
        prenom_input = input("Entrez le prénom : ")
        num_input = input("Entrez le numéro de téléphone : ")
        contact = {"Nom" : nom_input, "Prénom" : prenom_input, "Téléphone" : num_input}
        print("Le contact a été ajouté avec succès !")
    elif user_input == "afficher" :
        for x in contacts :
            print(x)
    user_input = input("Voulez-vous ajouter un contact ou afficher la liste des contacts ? (ajouter/afficher) :")