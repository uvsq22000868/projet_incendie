#groupe MIASHS TD1
#Margaux Ulliac
#Sulayman Charpentier
#madjoua Djeti
#Fouad Abdoullah
#https://github.com/uvsq22000868/projet_incendie


import tkinter as tk

#on crée la fenêtre sur laquelle seront les parcelles avec l'incendie
HEIGHT=400
WIDTH=600
root= tk.Tk()
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')

canvas.grid(column=0, row=0)
root.mainloop()

#on insère le quadrillage


#On insère le bouton qui va situer aléatoirement les parcelles d'eau, de forêt et de prairie.



#programme "principal" 


from tkinter import *
window= Tk()
window.title("Jeux de la vie")
window.geometry("600x600")
window.minsize(150,150)
window.maxsize(800,800)
window.config(background='white')
frame=Frame(window,bg="white")
table=[[0] * 15 for i in range(15)]
table1=table
tablevie=[[0] * 15 for i in range(15)]
 
 
file=open("regles py.txt",encoding="utf8")
contenu=file.read()
file.close()
 
 
def reglesjeu():
    window2=Tk()
    window2.title("Règles du jeu")
    window2.geometry("600x600")
    window2.minsize(150,150)
    window2.maxsize(800,800)
    window2.config(background='white')
    label_title2=Label(window2,text="Voici le concept et les règles du jeu de la vie:")
    label_title2.pack(side=TOP)
    labelregles=Label(window2,text=contenu,wraplength=500,justify=LEFT)
    labelregles.pack(pady=10)
 
 
def quadrillage():
  window1= Tk()
  window1.title("Jeux de la vie")
  window1.geometry("600x600")
  window1.minsize(150,150)
  window1.maxsize(800,800)
  window1.config(background='white')
 
 
 
 
  frame1=Frame(window1,bg="white")
  label_title1=Label(frame1, text="choisissez les dimensions du jeu",font=("Ariel",10),bg='white',fg='blue' )
  label_title1.pack(expand=YES)
  frame1.pack(side=TOP)
 
 
  def boutoncellule(event,i,j):
    global table
    global tablevie
    table[i][j].config(background="yellow")
    tablevie[i][j]=1
 
  def clickdroit(event,i,j):
    global table
    global tablevie
    table[i][j].config(background="white")
    tablevie[i][j]=0
 
  framjeu=Frame(window1,bg='white')
  for i in range(15):
    for j in range(15):
      d= carré_button=Button(framjeu,bg='white',width=2,height=1)
      table[i][j]=d
      d.grid(row=i, column=j)
      def gest(evt,i=i,j=j):
          return boutoncellule(evt,i,j)
      def mort(evt, i=i, j=j):
        return clickdroit(evt,i,j)
      d.bind("<Button-1>",gest)
      d.bind("<Button-3>",mort)
  framjeu.pack(expand=YES)
 
 
 
  def jeu():
     global table1
     global tablevie
     for i in range(15):
       for j in range(15):
        if 0<i<14 and 0<j<14 and tablevie[i][j]==0 and tablevie[i+1][j]+tablevie[i-1][j]+tablevie[i+1][j+1]+tablevie[i+1][j-1]+tablevie[i][j+1]+tablevie[i-1][j-1]+tablevie[i-1][j+1]+tablevie[i][j-1]==3:
            tablevie[i][j]=1
        elif  0<i<14 and 0<j<14 and tablevie[i][j]==1 and tablevie[i+1][j]+tablevie[i-1][j]+tablevie[i+1][j+1]+tablevie[i+1][j-1]+tablevie[i][j+1]+tablevie[i-1][j-1]+tablevie[i-1][j+1]+tablevie[i][j-1]==2:
            tablevie[i][j]=1
        elif  0<i<14 and 0<j<14 and tablevie[i][j]==1 and tablevie[i+1][j]+tablevie[i-1][j]+tablevie[i+1][j+1]+tablevie[i+1][j-1]+tablevie[i][j+1]+tablevie[i-1][j-1]+tablevie[i-1][j+1]+tablevie[i][j-1]==3:
            tablevie[i][j]=1
        elif  0<i<14 and 0<j<14 and tablevie[i][j]==1 and tablevie[i+1][j]+tablevie[i-1][j]+tablevie[i+1][j+1]+tablevie[i+1][j-1]+tablevie[i][j+1]+tablevie[i-1][j-1]+tablevie[i-1][j+1]+tablevie[i][j-1]==1:
            tablevie[i][j]=0
        elif  0<i<14 and 0<j<14 and tablevie[i][j]==1 and tablevie[i+1][j]+tablevie[i-1][j]+tablevie[i+1][j+1]+tablevie[i+1][j-1]+tablevie[i][j+1]+tablevie[i-1][j-1]+tablevie[i-1][j+1]+tablevie[i][j-1]>3:
            tablevie[i][j]=0
 
 
 
        if 0<j<14 and tablevie[0][j]==0 and tablevie[1][j]+tablevie[1][j+1]+tablevie[1][j-1]+tablevie[0][j+1]+tablevie[0][j-1]==3:
            tablevie[0][j]=1
        elif  0<j<14 and tablevie[0][j]==1 and tablevie[1][j]+tablevie[1][j+1]+tablevie[1][j-1]+tablevie[0][j+1]+tablevie[0][j-1]==2:
            tablevie[0][j]=1
        elif 0<j<14 and tablevie[0][j]==1 and tablevie[1][j]+tablevie[1][j+1]+tablevie[1][j-1]+tablevie[0][j+1]+tablevie[0][j-1]==3:
           tablevie[0][j]=1
        elif 0<j<14 and tablevie[0][j]==1 and tablevie[1][j]+tablevie[1][j+1]+tablevie[1][j-1]+tablevie[0][j+1]+tablevie[0][j-1]==1:
            tablevie[0][j]=0
        elif 0<j<14 and tablevie[0][j]==1 and tablevie[1][j]+tablevie[1][j+1]+tablevie[1][j-1]+tablevie[0][j+1]+tablevie[0][j-1]>3:
            tablevie[0][j]=0
 
        if 0<i<14 and tablevie[i][0]==0 and tablevie[i+1][0]+tablevie[i-1][0]+tablevie[i+1][1]+tablevie[i][1]+tablevie[i-1][1]==3:
            tablevie[i][0]=1
        elif 0<i<14 and tablevie[i][0]==1 and tablevie[i+1][0]+tablevie[i-1][0]+tablevie[i+1][1]+tablevie[i][1]+tablevie[i-1][1]==2:
            tablevie[i][0]=1
        elif 0<i<14 and tablevie[i][0]==1 and tablevie[i+1][0]+tablevie[i-1][0]+tablevie[i+1][1]+tablevie[i][1]+tablevie[i-1][1]==3:
            tablevie[i][0]=1
        elif 0<i<14 and tablevie[i][0]==1 and tablevie[i+1][0]+tablevie[i-1][0]+tablevie[i+1][1]+tablevie[i][1]+tablevie[i-1][1]==1:
           tablevie[i][0]=0
        elif 0<i<14 and  tablevie[i][0]==1 and tablevie[i+1][0]+tablevie[i-1][0]+tablevie[i+1][1]+tablevie[i][1]+tablevie[i-1][1]>3:
            tablevie[i][0]=0
 
 
 
        if 0<j<14 and tablevie[14][j]==0 and tablevie[13][j]+tablevie[14][j+1]+tablevie[14][j-1]+tablevie[13][j+1]+tablevie[13][j-1]==3:
            tablevie[14][j]=1
        elif 0<j<14 and tablevie[14][j]==1 and tablevie[13][j]+tablevie[14][j+1]+tablevie[14][j-1]+tablevie[13][j+1]+tablevie[13][j-1]==2:
            tablevie[14][j]=1
        elif 0<j<14 and tablevie[14][j]==1 and tablevie[13][j]+tablevie[14][j+1]+tablevie[14][j-1]+tablevie[13][j+1]+tablevie[13][j-1]==3:
             tablevie[14][j]=1
        elif 0<j<14 and tablevie[14][j]==1 and tablevie[13][j]+tablevie[14][j+1]+tablevie[14][j-1]+tablevie[13][j+1]+tablevie[13][j-1]==1:
            tablevie[14][j]=0
        elif 0<j<14 and tablevie[14][j]==1 and tablevie[13][j]+tablevie[14][j+1]+tablevie[14][j-1]+tablevie[13][j+1]+tablevie[13][j-1]>3:
            tablevie[14][j]=0
 
 
        if 0<i<14 and tablevie[i][14]==0 and tablevie[i+1][13]+tablevie[i-1][13]+tablevie[i+1][14]+tablevie[i][13]+tablevie[i-1][14]==3:
            tablevie[i][14]=1
        elif 0<i<14 and tablevie[i][14]==1 and tablevie[i+1][13]+tablevie[i-1][13]+tablevie[i+1][14]+tablevie[i][13]+tablevie[i-1][14]==2:
            tablevie[i][14]=1
        elif 0<i<14 and tablevie[i][14]==1 and tablevie[i+1][13]+tablevie[i-1][13]+tablevie[i+1][14]+tablevie[i][13]+tablevie[i-1][14]==3:
            tablevie[i][14]=1
        elif 0<i<14 and tablevie[i][14]==1 and tablevie[i+1][13]+tablevie[i-1][13]+tablevie[i+1][14]+tablevie[i][13]+tablevie[i-1][14]==1:
            tablevie[i][14]=0
        elif 0<i<14 and tablevie[i][14]==1 and tablevie[i+1][13]+tablevie[i-1][13]+tablevie[i+1][14]+tablevie[i][13]+tablevie[i-1][14]>3:
            tablevie[i][14]=0
 
 
 
        if tablevie[0][0]==0 and tablevie[1][0]+tablevie[0][1]+tablevie[1][1]==3:
            tablevie[0][0]=1
        elif tablevie[0][0]==1 and tablevie[1][0]+tablevie[0][1]+tablevie[1][1]==2:
            tablevie[0][0]=1
        elif tablevie[0][0]==1 and tablevie[1][0]+tablevie[0][1]+tablevie[1][1]==3:
            tablevie[0][0]=1
        elif tablevie[0][0]==1 and tablevie[1][0]+tablevie[0][1]+tablevie[1][1]==1:
            tablevie[0][0]=0
        elif tablevie[0][0]==1 and tablevie[1][0]+tablevie[0][1]+tablevie[1][1]>3:
            tablevie[0][0]=0
 
 
        if tablevie[14][0]==0 and tablevie[14][1]+tablevie[13][0]+tablevie[13][1]==3:
            tablevie[14][0]=1
        elif tablevie[14][0]==1 and tablevie[14][1]+tablevie[13][0]+tablevie[13][1]==2:
            tablevie[14][0]=1
        elif tablevie[14][0]==1 and tablevie[14][1]+tablevie[13][0]+tablevie[13][1]==3:
            tablevie[14][0]=1
        elif tablevie[14][0]==1 and tablevie[14][1]+tablevie[13][0]+tablevie[13][1]==1:
            tablevie[14][0]=0
        elif tablevie[14][0]==1 and tablevie[14][1]+tablevie[13][0]+tablevie[13][1]>3:
            tablevie[14][0]=0
 
 
        if tablevie[0][14]==0 and tablevie[1][14]+tablevie[0][13]+tablevie[1][13]==3:
            tablevie[0][14]=1
        elif tablevie[0][14]==1 and tablevie[1][14]+tablevie[0][13]+tablevie[1][13]==2:
            tablevie[0][14]=1
        elif tablevie[0][14]==1 and tablevie[1][14]+tablevie[0][13]+tablevie[1][13]==3:
            tablevie[0][14]=1
        elif tablevie[0][14]==1 and tablevie[1][14]+tablevie[0][13]+tablevie[1][13]==1:
            tablevie[0][14]=0
        elif tablevie[0][14]==1 and tablevie[1][14]+tablevie[0][13]+tablevie[1][13]>3:
            tablevie[0][14]=0
 
 
        if tablevie[14][14]==0 and tablevie[14][13]+tablevie[13][14]+tablevie[13][13]==3:
            tablevie[14][14]=1
        elif tablevie[14][14]==1 and tablevie[14][13]+tablevie[13][14]+tablevie[13][13]==2:
            tablevie[14][14]=1
        elif tablevie[14][14]==1 and tablevie[14][13]+tablevie[13][14]+tablevie[13][13]==3:
            tablevie[14][14]=1
        elif tablevie[14][14]==1 and tablevie[14][13]+tablevie[13][14]+tablevie[13][13]==1:
            tablevie[14][14]=0
        elif tablevie[14][14]==1 and tablevie[14][13]+tablevie[13][14]+tablevie[13][13]>3:
            tablevie[14][14]=0
 
 
     for i in range(15):
       for j in range(15):
           if tablevie[i][j]==1:
            d=table[i][j]
            d.config(bg="yellow")
           else:
            d=table[i][j]
            d.config(bg="white")
       #while (d).cget('white')  and (tamble[i+1][j])['yellow'] and (table[i-1][j])['yellow'] and (table[i+1][j+1])['yellow'] and (table[i+1][j-1])['yellow']:
       # d.config(bg="yellow")
 
  def jeuauto():
    while 1:
        jeu()
 
 
 
 
 
 
 
 
  def arret():
    jouer_button4.config(state=DISABLED)
  def reset():
    window1.destroy()
    quadrillage()
 
 
 
  jouer_button4=Button(window1,text='Jouer',font=("Ariel",10),bg='white',fg='blue',command=jeuauto)
  jouer_button4.pack(side=BOTTOM,pady=10)
  jouer_button5=Button(window1,text='Stop',font=("Ariel",10),bg='white',fg='blue',command=arret)
  jouer_button5.pack(side=BOTTOM)
  jouer_button6=Button(window1,text='Recommencer',font=("Ariel",10),bg='white',fg='blue',command=reset)
  jouer_button6.pack(side=BOTTOM,pady=10)
 
 
 
 
 
 
 
 
label_title=Label(frame, text="Bienvenu sur le jeu de la vie",font=("Ariel",16),bg='white',fg='blue')
label_title.pack()
 
 
 
jouer_button=Button(frame,text='Jouer',font=("Ariel",10),bg='white',fg='blue',command=quadrillage)
jouer_button.pack(pady=10)
 
jouer_button1=Button(frame,text='Règles du jeu',font=("Ariel",10),bg='white',fg='blue',command=reglesjeu)
jouer_button1.pack(pady=10)
 
 
 
 
 
 
frame.pack(expand=YES)
 
window.mainloop()
