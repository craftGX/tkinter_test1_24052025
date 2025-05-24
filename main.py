import tkinter as tk

# Fonction pour traiter l'envoi du texte
def envoyer_texte():
    global prenom  # Déclarer prenom comme variable globale
    prenom = champ_texte.get()  # Récupérer le texte du champ prénom
    if prenom:  # Vérifier que le champ n'est pas vide
        label.config(text=f"Bonjour, {prenom}!")  # Modifier le texte du label
        message_bienvenue.config(text=f"Heureux de te revoir, {prenom}!")  # Mettre à jour le message de bienvenue
        champ_texte.config(state='disabled')  # Désactiver le champ prénom
        bouton_envoyer.config(state='disabled')  # Désactiver le bouton prénom
        activer_idee()  # Activer les éléments pour l'idée

def activer_idee():
    champ_idee.pack(pady=10)  # Afficher le champ de texte pour l'idée
    bouton_idee.pack(pady=10)  # Afficher le bouton pour l'idée

def envoyer_idee():
    idee = champ_idee.get()  # Récupérer le texte du champ idée
    if idee:  # Vérifier que le champ n'est pas vide
        mots_interdits = ["dormir", "gaming", "jouer", "trainer", "jeux-video", "film", "serie", "episode"]
        if any(mot in idee.lower() for mot in mots_interdits):
            message_idee.config(text="Très mauvaise idée!")  # Répondre avec une mauvaise idée
        else:
            message_idee.config(text=f"Très bonne idée, {prenom}!")  # Afficher la réponse

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Ma Fenêtre Tkinter")
fenetre.geometry("400x400")  # Largeur x Hauteur

# Ajouter un label avec couleur, style et padding intérieur
label = tk.Label(
    fenetre,
    text="Bonjour, Tkinter!",
    fg="white",
    bg="blue",
    font=("Helvetica", 16, "bold"),
    padx=5,
    pady=5
)
label.pack(pady=20)

# Champ de texte pour le prénom
champ_texte = tk.Entry(fenetre, width=30)
champ_texte.insert(0, "Prénom")
champ_texte.pack(pady=10)

# Bouton "Envoyer" pour le prénom
bouton_envoyer = tk.Button(fenetre, text="Envoyer", command=envoyer_texte)
bouton_envoyer.pack(pady=10)

# Message de bienvenue
message_bienvenue = tk.Label(fenetre, text="", font=("Helvetica", 12), pady=10)
message_bienvenue.pack()

# Champ de texte pour l'idée (initialement caché)
champ_idee = tk.Entry(fenetre, width=30)
champ_idee.insert(0, "Que va-t-on faire aujourd'hui?")
# champ_idee.pack(pady=10)  # Commenté pour le cacher

# Bouton "Envoyer" pour l'idée (initialement caché)
bouton_idee = tk.Button(fenetre, text="Envoyer l'idée", command=envoyer_idee)
# bouton_idee.pack(pady=10)  # Commenté pour le cacher

# Message pour la réponse à l'idée
message_idee = tk.Label(fenetre, text="", font=("Helvetica", 12), pady=10)
message_idee.pack()

# Lancer la boucle principale
fenetre.mainloop()