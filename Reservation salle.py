from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Entry
import  customtkinter

root = Tk()
root.title("Aw KA HOTEL")
root.geometry("1000x650")
#root.resizable(False, False)
root.configure(background='#60554F')

lbltitre = customtkinter.CTkLabel(master=root,text="RESERVATION",height=30,width=40,border=1,corner_radius=20,bg_color="#FCFAFA",)
lbltitre.place(x=400, y=0, width=200)

lblnom = Label(root, text="Salle", font=("sans serif", 12), background='#60554F', foreground='black')
lblnom.place(x=30, y=130, width=80)
txtdate=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtdate.place(x=200,y=130,width=160)
lblprenom = Label(root, text="Client", font=("sans serif", 12), background='#60554F', foreground='black')
lblprenom.place(x=40, y=190, width=60)
txtdate=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtdate.place(x=200,y=190,width=160)

lblnumero = Label(root, text="Date_reservation", font=("sans serif", 12), background='#60554F', foreground='black')
lblnumero.place(x=0, y=250, width=210)
txtdate=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtdate.place(x=200,y=250,width=160)

lblsalaire = Label(root, text="Date_fin_reservation", font=("sans serif", 12), background='#60554F', foreground='black')
lblsalaire.place(x=0, y=310, width=220)
txtdate=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtdate.place(x=200,y=310,width=160)

lbldate = Label(root, text="Prix", font=("sans serif", 12), background='#60554F', foreground='black')
lbldate.place(x=10, y=370, width=80)
txtdate=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtdate.place(x=200,y=370,width=160)
buttrechercher= customtkinter.CTkButton(master=root,text="Rechercher",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttrechercher.place(x=10,y=450,width=110)

txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=200,y=450,width=160)

buttEnregistrer= customtkinter.CTkButton(master=root,text="Enregistrer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttEnregistrer.place(x=10,y=560,width=100)


buttmodifier= customtkinter.CTkButton(master=root,text="Modifier",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttmodifier.place(x=115,y=560,width=100)


buttonsupp= customtkinter.CTkButton(master=root,text="Supprimer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttonsupp.place(x=220,y=560,width=100)

tableAfficher = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, ), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=600, height=600)
style = ttk.Style(root)
style.configure("Treeview",background="#D9D9D9")
# Entete
tableAfficher.heading(1, text="Id_Salle")
tableAfficher.heading(2, text="Id_client")
tableAfficher.heading(3, text="Date_reservation")
tableAfficher.heading(4, text="Date_fin_reservation")
tableAfficher.heading(5, text="Prix")
# definir les dimentions des colonnes
tableAfficher.column(1, width=10)
tableAfficher.column(2, width=40)
tableAfficher.column(3, width=40)
tableAfficher.column(4, width=40)
tableAfficher.column(5, width=40)
liste = ["a","b","c","d","e"]
tableAfficher.insert('',1,values=liste)

root.mainloop()