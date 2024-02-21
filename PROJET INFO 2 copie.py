#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:39:57 2023

@author: maissa
"""
import time
import tkinter as tk
import random
from tkinter import *
import os
from tkinter import ttk
import csv


'--------------fenetre : connexion------------------------------------------------'

def login():
    username = username_entry.get()
    password = password_entry.get()
    File_name = os.listdir()
    if str(username)+".csv" in File_name:
        File = open(str(username)+".csv", "r")
        liste_info = File.read().split(",")
        File.close()
        if password == liste_info[1] :
            messagebox.showinfo("Connexion réussie", f"Connexion réussie pour {username}")
            # Fermez la fenêtre de connexion
            root1.destroy()
            # Appelez la fonction pour afficher la fenêtre de jeu
            fenetre1(username,password)
            # Démarrer l'application
            root.mainloop()
            return
        else:
            messagebox.showerror("Erreur", "Mot de passe incorrect. Réessayez.")
            return
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur non trouvé. Veuillez vous inscrire.")
    return username,password
    
def register():
    username = username_entry.get()
    password = password_entry.get()    
    File = os.listdir()
    if str(username)+".csv" in File:
        messagebox.showerror("Erreur", "Ce nom d'utilisateur est déjà utilisé. Choisissez un autre.")
        return
    else: 
        File = open(str(username)+".csv", "w")
        File.write(str(username)+","+str(password)+",")
        File.close()
        print("Message 2 : Votre comte a été crée avec succès !")
        messagebox.showinfo("Inscription réussie", f"Inscription réussie pour {username}")
        # Fermez la fenêtre de connexion
        root1.destroy()
        # Appelez la fonction pour afficher la fenêtre de jeu
        fenetre1(username,password)
        # Démarrer l'application
        root.mainloop()
        return
    return username,password
        
'--------------Initialisation du jeu------------------------------------------------'
def fenetre1(username,password):
    
    def initialisation_du_jeu():  
        # Les dimensions du labyrinthe
        CANVAS_WIDTH = 600
        CANVAS_HEIGHT = 400
        CELL_SIZE = 20
        GRID_WIDTH = CANVAS_WIDTH // CELL_SIZE
        GRID_HEIGHT = CANVAS_HEIGHT // CELL_SIZE
        
        # Initialisation des variables de jeu
        global treasure_x
        global treasure_y
        treasure_x = random.randint(0, GRID_WIDTH-1)
        treasure_y = random.randint(0, GRID_HEIGHT-1)
        global indice_x
        global indice_y
        indice_x = random.randint(0, GRID_WIDTH-1)
        indice_y = random.randint(0, GRID_HEIGHT-1)
        global indice2_x
        global indice2_y
        indice2_x = random.randint(0, GRID_WIDTH-1)
        indice2_y = random.randint(0, GRID_HEIGHT-1)
        global probleme_x
        global probleme_y
        probleme_x = random.randint(0, GRID_WIDTH-1)
        probleme_y = random.randint(0, GRID_HEIGHT-1)
        global probleme2_x
        global porbleme2_y
        probleme2_x = random.randint(0, GRID_WIDTH-1)
        probleme2_y = random.randint(0, GRID_HEIGHT-1)        
        global player_x
        global player_y
        player_x = 0
        player_y = 0
        
        # Initialisation de la grille de jeu
        grid = []
        for i in range(GRID_WIDTH):
            row = []
            for j in range(GRID_HEIGHT):
                # Génère des murs aléatoires
                if random.random() < 0.3:
                    row.append(1)
                else:
                    row.append(0)
            grid.append(row)
        
        # S'assurer que le trésor n'est pas sur un mur
        while grid[treasure_x][treasure_y] == 1:
            treasure_x = random.randint(0, GRID_WIDTH-1)
            treasure_y = random.randint(0, GRID_HEIGHT-1)
        
        while grid[indice_x][indice_y]==1:
            indice_x = random.randint(0,GRID_WIDTH-1)
            indice_y = random.randint(0,GRID_HEIGHT-1)
        
        while grid[indice2_x][indice2_y]==1:
            indice2_x = random.randint(0,GRID_WIDTH-1)
            indice2_y = random.randint(0,GRID_HEIGHT-1)
        
        while grid[probleme_x][probleme_y]==1:
            probleme_x = random.randint(0,GRID_WIDTH-1)
            probleme_y = random.randint(0,GRID_HEIGHT-1)
            
        while grid[probleme2_x][probleme2_y]==1:
            probleme2_x = random.randint(0,GRID_WIDTH-1)
            probleme2_y = random.randint(0,GRID_HEIGHT-1)
        
        # Initialisation de la fenêtre de jeu
        root = tk.Tk()
        root.title("Chasse au trésor dans le labyrinthe")
        
        # Création du canevas pour afficher le labyrinthe
        canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        canvas.pack()
        
        # Fonction pour dessiner le labyrinthe
        def draw_grid():
            for i in range(GRID_WIDTH):
                for j in range(GRID_HEIGHT):
                    x1 = i * CELL_SIZE
                    y1 = j * CELL_SIZE
                    x2 = x1 + CELL_SIZE
                    y2 = y1 + CELL_SIZE
                    if grid[i][j] == 1:
                        canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                    else:
                        canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        
        # Fonction pour dessiner le joueur
        def draw_player():
            x1 = player_x * CELL_SIZE
            y1 = player_y * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_oval(x1, y1, x2, y2, fill="blue")
        
        # Fonction pour dessiner le trésor
            
        def draw_indice():
    
            x1 = indice_x * CELL_SIZE
            y1 = indice_y * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, fill="red")
            
            x1_2 = indice2_x * CELL_SIZE
            y1_2 = indice2_y * CELL_SIZE
            x2_2 = x1_2 + CELL_SIZE
            y2_2 = y1_2 + CELL_SIZE
            canvas.create_rectangle(x1_2, y1_2, x2_2, y2_2, fill="red")
            
        
        # Fonction pour déplacer le joueur
        def move_player(event):
            global player_x, player_y
            if event.keysym == "Up":
                if player_y > 0 and grid[player_x][player_y-1] == 0:
                    player_y -= 1
            elif event.keysym == "Down":
                if player_y < GRID_HEIGHT-1 and grid[player_x][player_y+1] == 0:
                    player_y += 1
            elif event.keysym == "Left":
                if player_x > 0 and grid[player_x-1][player_y] == 0:
                    player_x -= 1
            elif event.keysym == "Right":
                if player_x < GRID_WIDTH-1 and grid[player_x+1][player_y] == 0:
                    player_x += 1
            canvas.delete("all")
            draw_grid()
            draw_indice()
            draw_player()
            check_win(username)
            
        def enigme():
            a=(4*treasure_x-3-5*treasure_x+2)-1
            enigme = Tk()
            enigme.title("The MAZE")
            enigme.config(background="black")
        
            
            enigme = Label(enigme,text="Tic,Tac !")
            enigme.pack()
            
            enigme2 = Label(enigme , text="Mon abscisse est la solution de cette équation :  ")
            enigme2.pack()
            
            enigme3= Label(enigme , text="   "+str(a)+" -4x+3-2=-5x  ")
            enigme3.pack()
            
            enigme.mainloop()
    
        
        def enigme2():
            b=5*(treasure_y**2)+2*treasure_y - 3
            enigme = Tk()
            enigme.title("The MAZE")
            enigme.config(background="white")
        
            
            enigme = Label(enigme,text="Tic,Tac !")
            enigme.pack()
            
            enigme2 = Label(enigme , text="Mon ordonnée est la solution de cette équation :  ")
            enigme2.pack()
            
            enigme3= Label(enigme , text="   "+str(b)+"= 5x^2 + 2x - 3  ")
            enigme3.pack()
            
            enigme.mainloop()
            
            
        def probleme(username):
            
            def verifier():
                solution = 4 
                reponse=enigme3_entry.get()
                if int(reponse) == solution :
                    print("bonne reponse")
                    probleme_fen.destroy()
                    messagebox.showerror("BRAVO ! Vous avez trouvez la solution, vous gagnez 2 points et vous pouvez continuer")
                    File = open(str(username)+".csv", "a")
                    File.write(",Score , 2")
                    File.close()

                    
            probleme_fen = Tk()
            probleme_fen.title("The MAZE")
            probleme_fen.config(background="black")
            
        
            
            enigme = Label(probleme_fen,text="BOOM!")
            enigme.pack()
            
            enigme2 = Label(probleme_fen , text="Resou ce probleme ou tu ne pourras avancer ! ",bg="black",fg="white")
            enigme2.pack()
            
            enigme3= Label(probleme_fen , text="Si un prix a augmenté de 20 %, puis a été réduit de 20 %, quel est le pourcentage de changement total ?",bg="black",fg="white")
            enigme3.pack()
            
            global enigme3_entry
            enigme3_entry=Entry(probleme_fen,font=("Arial",18),bg="black",fg="white",)
            enigme3_entry.pack()
            
            button=Button(probleme_fen,text="Valider ?",bg="black",fg="black",command=verifier)
            button.pack()
            
            probleme_fen.mainloop()
    
    
        def probleme2(username):
            
            def verifier2():
                solution = 6 
                reponse=enigme3_entry.get()
                if int(reponse) == solution :
                    print("bonne reponse")
                    probleme_fen.destroy() 
                    messagebox.showerror("BRAVO ! Vous avez trouvez la solution, vous gagnez 2 points et vous pouvez continuer")
                    File = open(str(username)+".csv", "a")
                    File.write(",Score , 2")
                    File.close()
            probleme_fen = Tk()
            probleme_fen.title("The MAZE")
            probleme_fen.config(background="black")
        
            
            enigme = Label(probleme_fen,text="BOOM!")
            enigme.pack()
            
            enigme2 = Label(probleme_fen , text="Resou ce probleme ou tu ne pourras avancer ! ",bg="black",fg="white")
            enigme2.pack()
            
            enigme3= Label(probleme_fen , text="Si un rectangle a une longueur de 8 cm et une diagonale de 10 cm, quelle est la largeur du rectangle ?",bg="black",fg="white")
            enigme3.pack()
            
            global enigme3_entry
            enigme3_entry=Entry(probleme_fen,font=("Arial",18),bg="black",fg="white",)
            enigme3_entry.pack()
            
            button=Button(probleme_fen,text="Valider ?",bg="black",fg="black",command=verifier2)
            button.pack()
            
            probleme_fen.mainloop()     
    
           
    
            
        # Fonction pour vérifier si le joueur a trouvé le trésor
        from tkinter import messagebox

        def check_win(username):
                    #Fonction pour rafraichir la fenetre 
            def rafraichir_window():
                root.destroy()
                petit.destroy()
                initialisation_du_jeu()
            
            if player_x == treasure_x and player_y == treasure_y:
                print("bravo vous avez trouver le tresor")
                File = open(str(username)+".csv", "a")
                File.write(",Score , 5")
                File.close()
                 
                                        
                canvas.create_text(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, text="Vous avez trouvé le trésor !", fill="green", font=("Arial", 24))
                petit = Tk()
                petit.title("The MAZE")
                petit.geometry("350x175")
                petit.minsize(350,175)
                petit.maxsize(350,175)
                petit.config(background="black")
                
                label = Label(petit,text="Vous avez trouvé le tresor ! Passer au niveau suivant!", bg="black",fg="white")
                label.pack()
                

                suivant_bouton = Button(petit,text="Suivant", bg="black",fg="black", width=8, height=3,command=rafraichir_window)
                suivant_bouton.pack()
                
                petit.mainloop()
                


            elif player_x == indice_x and player_y == indice_y:

                enigme()
                File = open(str(username)+".csv", "a")
                File.write(",Score , -4")
                File.close()
                
            elif player_x == indice2_x and player_y == indice2_y:
                enigme2()
                File = open(str(username)+".csv", "a")
                File.write(",Score , -4")
                File.close()
                
            elif player_x == probleme_x and player_y == probleme_y: 
                probleme(username)
                
            elif player_x == probleme2_x and player_y == probleme2_y: 
                probleme2(username)
                        
                     
                
        # Dessiner le labyrinthe, le joueur et le trésor pour la première fois
        draw_grid()
        draw_indice()
        draw_player()
        
        # Attacher la fonction move_player à l'événement du clavier
        canvas.bind_all("<Key>", move_player)
        
        # Lancer la boucle principale du jeu
        root.mainloop()    
    File = open(str(username)+".csv", "r")
    liste_info = File.read().split(",")
    File.close()    
    score = 0 
    for i in range(len(liste_info)):
        if liste_info[i]=="Score ":
            score=score+int(liste_info[i+1])
            
    fenetre1 = Tk()
    fenetre1.title("Inscription :")
    fenetre1.geometry("500x200")
    fenetre1.maxsize(500,200)
    fenetre1.minsize(500,200)
    fenetre1.config(background="black")
    fenetre1_frame = Frame(fenetre1,width=460,height=160,bg="black")
    
    message1 = Label(fenetre1_frame,text="Bienvenue sur THE MAZE!", font=("Arial", 20), bg="black", fg="white")
    message1.grid(row=4, column=3)
    
    #Space
    Space = Label(fenetre1_frame,text="",bg="black",height=1)
    Space.grid(row=5,column=3)
    
    message2 = Label(fenetre1_frame,text="Votre score est de : "+str(score), font=("Arial", 20), bg="black", fg="white")
    message2.grid(row=6, column=3)
    
    #Space
    Space = Label(fenetre1_frame,text="",bg="black",height=1)
    Space.grid(row=7,column=3)
    
    suivant_button2 = Button(fenetre1_frame,text="Jouer",font=("Arial",18),bg="black",fg="black",command=initialisation_du_jeu)
    suivant_button2.grid(row=9,column=3)

    #Space
    Space = Label(fenetre1_frame,text="",bg="black",height=1)
    Space.grid(row=10,column=3)        
    
    regle_button = Button(fenetre1_frame,text="Regle",font=("Arial",18),bg="black",fg="black",command=regle)
    regle_button.grid(row=11,column=3)
    
    fenetre1_frame.pack(expand=YES)
    fenetre1.mainloop()
    
    
def regle():
    messagebox.showerror("Regle", "Le but est de trouver le tresor caché dans le labyrinte.\nMais ATTENTION, plusieurs pieges sont à resoudre.\nLes cases rouges sont la pour t'aider, mais ce ne sont pas tes amies, elles te font perdre des points !")
    return

    
'''def choix_difficulte():
    import tkinter as tk
    
    # création de la fenêtre principale
    root = tk.Tk()
    root.title("Choix de difficulté")
    
    # création des variables de contrôle pour chaque bouton radio
    var_difficulty = tk.StringVar(value="facile")
    
    # fonction de traitement des événements des boutons radio
    def on_radio_button_change():
        print("Difficulté sélectionnée :", var_difficulty.get())
    
    # création des boutons radio
    rb_facile = tk.Radiobutton(root, text="Facile", variable=var_difficulty, value="facile", command=on_radio_button_change)
    rb_facile.pack()
    
    rb_moyen = tk.Radiobutton(root, text="Moyen", variable=var_difficulty, value="moyen", command=on_radio_button_change)
    rb_moyen.pack()
    
    rb_difficile = tk.Radiobutton(root, text="Difficile", variable=var_difficulty, value="difficile", command=on_radio_button_change)
    rb_difficile.pack()

    
    suivant_button2 = Button(root,text="Suivant",font=("Arial",18),bg="white",fg="black",command=initialisation_du_jeu)
    suivant_button2.pack()
    
    # démarrage de la boucle principale
    root.mainloop()'''
    
'----------fenetre 1 : choix : connexion/inscription-----------------------------'

# Créez la fenêtre de connexion
root1 = tk.Tk()
root1.title("Jeu de Trésor - Connexion")

# Créez les widgets pour le nom d'utilisateur et le mot de passe
username_label = tk.Label(root1, text="Nom d'utilisateur:")
username_entry = tk.Entry(root1)
password_label = tk.Label(root1, text="Mot de passe:")
password_entry = tk.Entry(root1, show="*")  # Montre des astérisques pour le mot de passe

# Créez les boutons d'inscription et de connexion
register_button = tk.Button(root1, text="S'inscrire", command=register)
login_button = tk.Button(root1, text="Se connecter", command=login)

# Placez les widgets sur la fenêtre
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
register_button.pack()
login_button.pack()

# Exécutez la fenêtre principale
root1.mainloop()
