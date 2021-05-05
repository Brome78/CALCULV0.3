from math import *
from tkinter import *
from tkinter.messagebox import *
import turtle
import tkinter as tk
from tkinter import ttk
from sympy import *

fontTitle=("Comic Sans MS", 24, "bold underline")


def principal():
    
    def chap1Menu():
        framePrincipal.destroy()
        frameChap1=Frame(fenetrePrincipal)
        frameChap1.pack(side=TOP)

        #Partie des perimetres

        #deplacement turtle

        def forward(a):
            t.forward(a)

        def back(a):
            t.back(a)

        def left(a):
            t.left(a)

        def right(a):
            t.right(a)

        frameDessin=LabelFrame(fenetrePrincipal, text="Dessin")
        frameDessin.configure(font=fontTitle)
        canvas=Canvas(frameDessin, width=1000, height=350)
        canvas.grid(row=1, column=1)
        t=turtle.RawTurtle(canvas)
        t.pensize(1)
        t.color("#ff0000", 'yellow')
        def erase():
            t.clear()
            t.penup()
        eraseButton=Button(frameDessin, text="Effacer", command=erase)
        eraseButton.grid(row=1, column=2)

        #Couleur de trait

        def colorBlue():
            t.pencolor("blue")
        def colorRed():
            t.pencolor("red")
        def colorGreen():
            t.pencolor("green")
        def colorBlack():
            t.pencolor("black")
        def colorGrey():
            t.pencolor("grey")
        def colorCyan():
            t.pencolor("cyan")
        
        #Couleur de fond

        def colorFillBlue():
            t.fillcolor("blue")
        def colorFillRed():
            t.fillcolor("red")
        def colorFillGreen():
            t.fillcolor("green")
        def colorFillBlack():
            t.fillcolor("black")
        def colorFillGrey():
            t.fillcolor("grey")
        def colorFillCyan():
            t.fillcolor("cyan")
        
        #Taille crayon

        frameTaille=LabelFrame(frameDessin,text="Taille de trait :")
        frameTaille.grid(row=1, column=3)
        
        penSizeSelector=Scale(frameTaille, variable=int,  from_=1, to=25, resolution=1)
        penSizeSelector.grid(row=1, column=3)
        
        def penSizeSettings():
            penSizeSet=float(penSizeSelector.get())
            t.pensize(penSizeSet)
        penSizeSetButton=Button(frameTaille, command=penSizeSettings, text="Set")
        penSizeSetButton.grid(row=1, column=4)
        
        
        #Couleur

        frameColorDessin=LabelFrame(frameDessin, text="Couleur de trait :")
        frameColorDessin.grid(row=2, column=3)
        frameColorFillDessin=LabelFrame(frameDessin, text="Couleur de remplissage :")
        frameColorFillDessin.grid(row=3, column=3)

        #Bouton de trait

        blue=Button(frameColorDessin, background="blue", command=colorBlue, width=6)
        blue.grid(row=2, column=4)
        red=Button(frameColorDessin, background="red", command=colorRed, width=6)
        red.grid(row=2, column=5)
        green=Button(frameColorDessin, background="green", command=colorGreen, width=6)
        green.grid(row=2, column=6)
        black=Button(frameColorDessin, background="black", command=colorBlack, width=6)
        black.grid(row=2, column=7)
        grey=Button(frameColorDessin, background="grey", command=colorGrey, width=6)
        grey.grid(row=2, column=8)
        cyan=Button(frameColorDessin, background="cyan", command=colorCyan, width=6)
        cyan.grid(row=2, column=9)

        #Bouton de fond
        
        blue=Button(frameColorFillDessin, background="blue", command=colorFillBlue, width=6)
        blue.grid(row=3, column=4)
        red=Button(frameColorFillDessin, background="red", command=colorFillRed, width=6)
        red.grid(row=3, column=5)
        green=Button(frameColorFillDessin, background="green", command=colorFillGreen, width=6)
        green.grid(row=3, column=6)
        black=Button(frameColorFillDessin, background="black", command=colorFillBlack, width=6)
        black.grid(row=3, column=7)
        grey=Button(frameColorFillDessin, background="grey", command=colorFillGrey, width=6)
        grey.grid(row=3, column=8)
        cyan=Button(frameColorFillDessin, background="cyan", command=colorFillCyan, width=6)
        cyan.grid(row=3, column=9)

        def perimetre():
            frameChap1.destroy()
            framePerimetre=Frame(fenetrePrincipal)
            framePerimetre.pack()
            

            

            #Fonctions pour le carré

            def carre():
                framePerimetre.destroy()
                frameCarre=LabelFrame(fenetrePrincipal, text="1. Périmètre d'un carré", padx=450)
                frameCarre.configure(font=fontTitle)
                frameCarre.pack(side=TOP)

                frameDessin.pack()

                entree=Spinbox(frameCarre, textvariable=int, width=50, from_=0, to=1000000)
                entree.grid(row=1,column=1)

                #Dessin
                
                def resultat():
                    c=float(entree.get())
                    if c != 0:
                        perimetreCarre.set("Perimetre = " + str(c*4) + " unités")
                        if (c) < 176:
                            t.pendown()
                            t.begin_fill()
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée")                        
                    else: 
                        showerror("Error", "Un côté ne peut pas être égal à 0")
                        perimetreCarre.set("Périmètre = ERROR")
                
                perimetreCarre = StringVar()

                Resultat=Label(frameCarre, textvariable=perimetreCarre)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCarre, text="Valider", command=resultat, background="green")
                validerButton.grid(row=3,column=1)

                

                def retourCarre():
                    frameCarre.destroy()
                    frameDessin.pack_forget()
                    perimetre()
                retourCarreButton=Button(frameCarre, text="Retour", command=retourCarre, width=20, background="blue")
                retourCarreButton.grid(row=1, column=10)
                t.penup()
                
                
            #Fonction pour le rectangle

            def rectangle():
                framePerimetre.destroy()
                frameRectangle=LabelFrame(fenetrePrincipal, text="2. Périmètre d'un rectangle", padx=450)
                frameRectangle.configure(font=fontTitle)  
                frameRectangle.pack(side=TOP)

                longueur=Label(frameRectangle, text="Longueur =")
                longueur.grid(row=1, column=1)
                entreel=Spinbox(frameRectangle, textvariable=int, width=50, from_=0, to=1000000)
                entreel.grid(row=1,column=2)

                largeur=Label(frameRectangle, text="Largeur =")
                largeur.grid(row=2, column=1)
                entreeL=Spinbox(frameRectangle, textvariable=int, width=50, from_=0, to=1000000)
                entreeL.grid(row=2,column=2)

                #Dessin

                frameDessin.pack()

                def resultat():
                    l=float(entreel.get())
                    L=float(entreeL.get())
                    if l and L != 0:
                        perimetreRectangle.set("Perimètre = " + str(l*2+L*2)+" unités")
                        if (l or L) < 176:
                            t.pendown()
                            t.begin_fill()
                            forward(l)
                            left(90)
                            forward(L)
                            left(90)
                            forward(l)
                            left(90)
                            forward(L)
                            left(90)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée")
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre égale à 0")
                        perimetreRectangle.set("Périmètre = ERROR")
                
                perimetreRectangle = StringVar()

                Resultat=Label(frameRectangle, textvariable=perimetreRectangle)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameRectangle, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourRectangle():
                    frameRectangle.destroy()
                    frameDessin.pack_forget()
                    perimetre()
                retourRectangleButton=Button(frameRectangle, text="Retour", command=retourRectangle, width=20, background="blue")
                retourRectangleButton.grid(row=1, column=10)
                t.penup()
                    
                
            #Fonction pour le cercle

            def cercle():
                framePerimetre.destroy()
                frameCercle=LabelFrame(fenetrePrincipal, text="3. Périmètre d'un cercle", padx=400)
                frameCercle.configure(font=fontTitle)
                frameCercle.pack(side=TOP)

                rayon=Label(frameCercle, text="Rayon =")
                rayon.grid(row=1, column=1)

                entree=Spinbox(frameCercle, textvariable=int, width=50, from_=0, to=1000000)
                entree.grid(row=1,column=2)

                frameDessin.pack()
                
                def resultat():
                    r=float(entree.get())
                    if r != 0:
                        perimetreCercle.set("Perimetre = " + str(r*2*pi)+ " unités")
                        if (r) < 84:
                            t.pendown()
                            t.begin_fill()
                            t.circle(r, 360)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée")
                        
                        
                    else: 
                        showerror("Error", "Un rayon ne peut pas être égal à 0")
                        perimetreCercle.set("Périmètre = ERROR")
                
                perimetreCercle = StringVar()

                Resultat=Label(frameCercle, textvariable=perimetreCercle)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCercle, text="Valider", command=resultat, background="green")
                validerButton.grid(row=3,column=1)
                def retourCercle():
                    frameCercle.destroy()
                    frameDessin.pack_forget()
                    perimetre()
                retourCercleButton=Button(frameCercle, text="Retour", command=retourCercle, width=20, background="blue")
                retourCercleButton.grid(row=1, column=10)
                t.penup()
            
            
            

            #Boutons Perimetre

            carreButton=Button(framePerimetre, text="1.Carré", command=carre, width=20, pady=5)
            carreButton.grid(row=1,column=1)
            rectangleButton=Button(framePerimetre, text="2.Rectangle", command=rectangle, width=20, pady=5)
            rectangleButton.grid(row=1, column=2)
            cercleButton=Button(framePerimetre, text="3.Cercle", command=cercle, width=20, pady=5)
            cercleButton.grid(row=2, column=1)

            def retourPerimetre():
                framePerimetre.destroy()
                chap1Menu()
            retourPerimetreButton=Button(framePerimetre, text="Retour", command=retourPerimetre, width=20, background="blue", pady=5)
            retourPerimetreButton.grid(row=1, column=10)
        
            
        
        #Partie aire

        def aire():
            
            frameChap1.destroy()
            frameAire=Frame(fenetrePrincipal)
            frameAire.pack(side=TOP)

            #Fonctions pour le carré

            def carre():
                frameAire.destroy()
                frameCarre=LabelFrame(fenetrePrincipal, text="1. Aire d'un Carré")
                frameCarre.configure(font=fontTitle)
                frameCarre.pack(side=TOP)

                entree=Spinbox(frameCarre, textvariable=int, width=50, from_=0, to=1000000)
                entree.grid(row=1,column=1)

                #Dessin

                frameDessin.pack()
                
                def resultat():
                    c=float(entree.get())
                    if c != 0:
                        aireCarre.set("Aire = " + str(float(entree.get())**2)+" unités²")
                        if (c) < 176:
                            t.pendown()
                            t.begin_fill()
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée") 
                    else: 
                        showerror("Error", "Un côté ne peut pas être égal à 0")
                        aireCarre.set("Aire = ERROR")
                
                aireCarre = StringVar()

                Resultat=Label(frameCarre, textvariable=aireCarre)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCarre, text="Valider", command=resultat, background="green")
                validerButton.grid(row=3,column=1)
                def retourCarre():
                    frameCarre.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourCarreButton=Button(frameCarre, text="Retour", command=retourCarre, width=20, background="blue")
                retourCarreButton.grid(row=1, column=10)

            #Fonction pour le rectangle

            def rectangle():
                frameAire.destroy()
                frameRectangle=LabelFrame(fenetrePrincipal, text="2. Aire d'un Rectangle")
                frameRectangle.configure(font=fontTitle)
                frameRectangle.pack(side=TOP)

                longueur=Label(frameRectangle, text="Longueur =")
                longueur.grid(row=1, column=1)
                entreel=Spinbox(frameRectangle, textvariable=int, width=50, from_=0, to=1000000)
                entreel.grid(row=1,column=2)

                largeur=Label(frameRectangle, text="Largeur =")
                largeur.grid(row=2, column=1)
                entreeL=Spinbox(frameRectangle, textvariable=int, width=50, from_=0, to=1000000)
                entreeL.grid(row=2,column=2)

                #Dessin

                frameDessin.pack()

                def resultat():
                    l=float(entreel.get())
                    L=float(entreeL.get())
                    if l and L != 0:
                        aireRectangle.set("Aire = " + str(l*L)+" unités²")
                        if (l or L) < 176:
                            t.pendown()
                            t.begin_fill()
                            forward(l)
                            left(90)
                            forward(L)
                            left(90)
                            forward(l)
                            left(90)
                            forward(L)
                            left(90)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée")
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre égale à 0")
                        aireRectangle.set("Aire = ERROR")
                
                aireRectangle = StringVar()

                Resultat=Label(frameRectangle, textvariable=aireRectangle)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameRectangle, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourRectangle():
                    frameRectangle.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourRectangleButton=Button(frameRectangle, text="Retour", command=retourRectangle, width=20, background="blue")
                retourRectangleButton.grid(row=1, column=10)    
                
            #Fonction pour le cercle

            def cercle():
                frameAire.destroy()
                frameCercle=LabelFrame(fenetrePrincipal, text="3. Aire d'un cercle")
                frameCercle.configure(font=fontTitle)
                frameCercle.pack(side=TOP)

                rayon=Label(frameCercle, text="Rayon =")
                rayon.grid(row=1, column=1)

                entree=Spinbox(frameCercle, textvariable=int, width=50, from_=0, to=1000000)
                entree.grid(row=1,column=2)

                #Dessin

                frameDessin.pack()
                
                def resultat():
                    r=float(entree.get())
                    if r != 0:
                        aireCercle.set("Aire = " + str((r**2)*pi)+" unités²")
                        if (r) < 176:
                            t.pendown()
                            t.begin_fill()
                            t.circle(r, 360)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée")
                    else: 
                        showerror("Error", "Un rayon ne peut pas être égal à 0")
                        aireCercle.set("Aire = ERROR")
                
                aireCercle = StringVar()

                Resultat=Label(frameCercle, textvariable=aireCercle)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCercle, text="Valider", command=resultat, background="green")
                validerButton.grid(row=3,column=1)
                def retourCercle():
                    frameCercle.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourCercleButton=Button(frameCercle, text="Retour", command=retourCercle, width=20, background="blue")
                retourCercleButton.grid(row=1, column=10)

            #Fonctions pour le triangle

            def triangle():
                frameAire.destroy()
                frameTriangle=LabelFrame(fenetrePrincipal, text="4. Aire d'un triangle")
                frameTriangle.configure(font=fontTitle)
                frameTriangle.pack(side=TOP)

                base=Label(frameTriangle, text="Longueur de la Base =")
                base.grid(row=1, column=1)
                entreeB=Spinbox(frameTriangle, textvariable=int, width=50, from_=0, to=1000000)
                entreeB.grid(row=1,column=2)

                hauteur=Label(frameTriangle, text="Hauteur =")
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameTriangle, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeB.get()) != 0:
                        aireTriangle.set("Aire = " + str((float(entreeB.get())*float(entreeH.get()))/2)+" unités²")

                    else: 
                        showerror("Error", "Un rayon ne peut pas être égal à 0")
                        aireTriangle.set("Aire = ERROR")
                
                aireTriangle = StringVar()

                Resultat=Label(frameTriangle, textvariable=aireTriangle)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameTriangle, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourTriangle():
                    frameTriangle.destroy()
                    
                    aire()
                retourTriangleButton=Button(frameTriangle, text="Retour", command=retourTriangle, width=20, background="blue")
                retourTriangleButton.grid(row=1, column=10)
            
            #Fonction pour le Parrallelogramme

            def parrallelogramme():
                frameAire.destroy()
                frameParrallelogramme=LabelFrame(fenetrePrincipal, text="5. Aire d'un parrallélogramme")
                frameParrallelogramme.configure(font=fontTitle)
                frameParrallelogramme.pack(side=TOP)

                base=Label(frameParrallelogramme, text="Longueur de la Base =")
                base.grid(row=1, column=1)
                entreeB=Spinbox(frameParrallelogramme, textvariable=int, width=50, from_=0, to=1000000)
                entreeB.grid(row=1,column=2)

                hauteur=Label(frameParrallelogramme, text="Hauteur =")
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameParrallelogramme, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=2,column=2)

                frameDessin.pack()

                def resultat():
                    B=float(entreeB.get())
                    H=float(entreeH.get())
                    if B and H != 0:
                        aireParrallelogramme.set("Aire = " + str(B*H)+" unités²")
                        if B or H < 176:
                            for i in range (2):
                                t.forward(B)
                                t.left(120)
                                t.forward(H*1.4)
                                t.left(60)
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée") 
                    else: 
                        showerror("Error", "Une longueur de la Base ou une hauteur ne peut pas etre égale à 0")
                        aireParrallelogramme.set("Aire = ERROR")
                
                aireParrallelogramme = StringVar()

                Resultat=Label(frameParrallelogramme, textvariable=aireParrallelogramme)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameParrallelogramme, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourParrallelogramme():
                    frameParrallelogramme.destroy()
                    
                    aire()
                retourParrallelogrammeButton=Button(frameParrallelogramme, text="Retour", command=retourParrallelogramme, width=20, background="blue")
                retourParrallelogrammeButton.grid(row=1, column=10) 
            
            #Fonction pour le losange

            def losange():
                frameAire.destroy()
                frameLosange=LabelFrame(fenetrePrincipal, text="6. Aire d'un losange")
                frameLosange.configure(font=fontTitle)
                frameLosange.pack(side=TOP)

                diagonal1=Label(frameLosange, text="Diagonale 1 =")
                diagonal1.grid(row=1, column=1)
                entree1=Spinbox(frameLosange, textvariable=int, width=50, from_=0, to=1000000)
                entree1.grid(row=1,column=2)

                diagonal2=Label(frameLosange, text="Diagonale 2 =")
                diagonal2.grid(row=2, column=1)
                entree2=Spinbox(frameLosange, textvariable=int, width=50, from_=0, to=1000000)
                entree2.grid(row=2,column=2)

                def resultat():
                    if float(entree1.get()) and float(entree2.get()) != 0:
                        aireLosange.set("Aire = " + str((float(entree1.get())*float(entree2.get()))/2)+" unités²")
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre égale à 0")
                        aireLosange.set("Aire = ERROR")
                
                aireLosange = StringVar()

                Resultat=Label(frameLosange, textvariable=aireLosange)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameLosange, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourLosange():
                    frameLosange.destroy()
                    
                    aire()
                retourLosangeButton=Button(frameLosange, text="Retour", command=retourLosange, width=20, background="blue")
                retourLosangeButton.grid(row=1, column=10) 

            #Fonction pour le trapeze

            def trapeze():
                frameAire.destroy()
                frameTrapeze=LabelFrame(fenetrePrincipal, text="7. Aire d'un trapèze")
                frameTrapeze.configure(font=fontTitle)
                frameTrapeze.pack(side=TOP)

                petitcote=Label(frameTrapeze, text="Petit Côté =")
                petitcote.grid(row=1, column=1)
                entreeP=Spinbox(frameTrapeze, textvariable=int, width=50, from_=0, to=1000000)
                entreeP.grid(row=1,column=2)

                grandcote=Label(frameTrapeze, text="Grand Côté =")
                grandcote.grid(row=2, column=1)
                entreeG=Spinbox(frameTrapeze, textvariable=int, width=50, from_=0, to=1000000)
                entreeG.grid(row=2,column=2)

                hauteur=Label(frameTrapeze, text="Hauteur =")
                hauteur.grid(row=3, column=1)
                entreeH=Spinbox(frameTrapeze, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=3,column=2)

                def resultat():
                    if float(entreeP.get()) and float(entreeG.get()) and float(entreeH.get()) != 0:
                        aireTrapeze.set("Aire = " + str(((float(entreeP.get())+float(entreeG.get()))/2)*float(entreeH.get()))+" unités²")
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre égale à 0")
                        aireTrapeze.set("Aire = ERROR")
                
                aireTrapeze = StringVar()

                Resultat=Label(frameTrapeze, textvariable=aireTrapeze)
                Resultat.grid(row=4,column=1)
                            
                
                validerButton=Button(frameTrapeze, text="Valider", command=resultat, background="green")
                validerButton.grid(row=5,column=1)
                def retourTrapeze():
                    frameTrapeze.destroy()
                    
                    aire()
                retourTrapezeButton=Button(frameTrapeze, text="Retour", command=retourTrapeze, width=20, background="blue")
                retourTrapezeButton.grid(row=1, column=10) 

            #Fonctions pour le cube

            def cube():
                frameAire.destroy()
                frameCube=LabelFrame(fenetrePrincipal, text="8. Aire d'un cube")
                frameCube.configure(font=fontTitle)
                frameCube.pack(side=TOP)

                entree=Spinbox(frameCube, textvariable=int, width=50, from_=0, to=1000000)
                entree.grid(row=1,column=1)

                frameDessin.pack()
                
                def resultat():
                    c=float(entree.get())
                    if c != 0:
                        aireCube.set("Aire = " + str((c**2)*6)+" unités²")
                        if c<176:
                            t.goto(0,0)
                            t.pendown()
                            for i in range(4):
                                t.forward(c)
                                t.left(90)
                            
                            t.goto(((1/2)*c),((1/2)*c))
                            
                            for i in range(4):
                                t.forward(c)
                                t.left(90)
                            
                            t.goto(((3/2)*c),((1/2)*c))
                            t.goto(c,0)
                            
                            t.goto(c,c)
                            t.goto(((3/2)*c),((3/2)*c))
                            
                            t.goto(((1/2)*c),((3/2)*c))
                            t.goto(0,c)
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée") 
                    else: 
                        showerror("Error", "Un côté ne peut pas être égal à 0")
                        aireCube.set("Aire = ERROR")
                
                aireCube = StringVar()

                Resultat=Label(frameCube, textvariable=aireCube)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCube, text="Valider", command=resultat, background="green")
                validerButton.grid(row=3,column=1)
                def retourCube():
                    frameCube.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourCubeButton=Button(frameCube, text="Retour", command=retourCube, width=20, background="blue")
                retourCubeButton.grid(row=1, column=10)
            
            #Fonction pour le pave droit

            def pave():
                frameAire.destroy()
                framePave=LabelFrame(fenetrePrincipal, text="9. Aire d'un pavé droit") 
                framePave.configure(font=fontTitle) 
                framePave.pack(side=TOP)

                longueur=Label(framePave, text="Longueur =")
                longueur.grid(row=1, column=1)
                entreel=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000)
                entreel.grid(row=1,column=2)

                largeur=Label(framePave, text="Largeur =")
                largeur.grid(row=2, column=1)
                entreeL=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000)
                entreeL.grid(row=2,column=2)

                hauteur=Label(framePave, text="Hauteur =")
                hauteur.grid(row=3, column=1)
                entreeH=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=3,column=2)

                frameDessin.pack()

                def resultat():
                    l=float(entreel.get())
                    L=float(entreeL.get())
                    H=float(entreeH.get())
                    if l and L and H != 0:
                        airePave.set("Aire = " + str(2*(l*L+L*H+l*H))+" unités²")

                        if l or L or H < 176:

                            t.goto(0,0)
                            t.pendown()
                            for i in range(2):
                                t.forward(l)
                                t.left(90)
                                t.forward(L)
                                t.left(90)
                            
                            t.goto((1/2)*H,(1/2)*L)
                            
                            for i in range(2):
                                t.forward(l)
                                t.left(90)
                                t.forward(L)
                                t.left(90)
                            t.forward(l)
                            t.goto(l,0)
                            
                            t.goto(l,L)
                            t.goto((3/2)*l,(3/2)*L)
                            t.back(l)
                            
                            t.goto(0,L)

                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée") 
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre égale à 0")
                        airePave.set("Aire = ERROR")
                
                airePave = StringVar()

                Resultat=Label(framePave, textvariable=airePave)
                Resultat.grid(row=4,column=1)
                            
                
                validerButton=Button(framePave, text="Valider", command=resultat, background="green")
                validerButton.grid(row=5,column=1)
                def retourPave():
                    framePave.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourPaveButton=Button(framePave, text="Retour", command=retourPave, width=20, background="blue")
                retourPaveButton.grid(row=1, column=10) 
            
            #Fonctions pour le cylindre

            def cylindre():
                frameAire.destroy()
                frameCylindre=LabelFrame(fenetrePrincipal, text="10. Aire d'un cylindre")
                frameCylindre.configure(font=fontTitle)
                frameCylindre.pack(side=TOP)

                rayon=Label(frameCylindre, text="Rayon =")
                rayon.grid(row=1, column=1)
                entreeR=Spinbox(frameCylindre, textvariable=int, width=50, from_=0, to=1000000)
                entreeR.grid(row=1,column=2)

                hauteur=Label(frameCylindre, text="Hauteur =")
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameCylindre, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeR.get()) != 0:
                        aireCylindre.set("Aire = " + str(2*pi*float(entreeR.get())*float(entreeH.get()))+" unités²")
                    else: 
                        showerror("Error", "Un rayon ne peut pas être égal à 0")
                        aireCylindre.set("Aire = ERROR")
                
                aireCylindre = StringVar()

                Resultat=Label(frameCylindre, textvariable=aireCylindre)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameCylindre, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourCylindre():
                    frameCylindre.destroy()
                    
                    aire()
                retourCylindreButton=Button(frameCylindre, text="Retour", command=retourCylindre, width=20, background="blue")
                retourCylindreButton.grid(row=1, column=10)
            
            #Fonctions pour le sphere

            def sphere():
                frameAire.destroy()
                frameSphere=LabelFrame(fenetrePrincipal, text="11. Aire d'une sphère")
                frameSphere.configure(font=fontTitle)
                frameSphere.pack(side=TOP)

                entree=Spinbox(frameSphere, textvariable=int, width=50, from_=0, to=1000000)
                entree.grid(row=1,column=1)
                
                def resultat():
                    if float(entree.get()) != 0:
                        aireSphere.set("Aire = " + str((float(entree.get())**2)*4*pi)+" unités²")
                    else: 
                        showerror("Error", "Un rayon ne peut pas être égal à 0")
                        aireSphere.set("Aire = ERROR")
                
                aireSphere = StringVar()

                Resultat=Label(frameSphere, textvariable=aireSphere)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameSphere, text="Valider", command=resultat, background="green")
                validerButton.grid(row=3,column=1)
                def retourSphere():
                    frameSphere.destroy()
                    
                    aire()
                retourSphereButton=Button(frameSphere, text="Retour", command=retourSphere, width=20, background="blue")
                retourSphereButton.grid(row=1, column=10)
            
            #Boutons aire

            carreButton=Button(frameAire, text="1.Carré", command=carre, width=20, pady=5)
            carreButton.grid(row=1,column=1)
            rectangleButton=Button(frameAire, text="2.Rectangle", command=rectangle, width=20, pady=5)
            rectangleButton.grid(row=1, column=2)
            cercleButton=Button(frameAire, text="3.Cercle", command=cercle, width=20, pady=5)
            cercleButton.grid(row=2, column=1)
            triangleButton=Button(frameAire, text="4.Triangle", command=triangle, width=20, pady=5)
            triangleButton.grid(row=2, column=2)
            parrallelogrammeButton=Button(frameAire, text="5.Parralélogramme", command=parrallelogramme, width=20, pady=5)
            parrallelogrammeButton.grid(row=3, column=1)
            losangeButton=Button(frameAire, text="6.Losange", command=losange, width=20, pady=5)
            losangeButton.grid(row=3, column=2)
            trapezeButton=Button(frameAire, text="7.Trapèze", command=trapeze, width=20, pady=5)
            trapezeButton.grid(row=4, column=1)
            cubeButton=Button(frameAire, text="8.Cube", command=cube, width=20, pady=5)
            cubeButton.grid(row=4, column=2)
            paveButton=Button(frameAire, text="9.Pavé Droit", command=pave, width=20, pady=5)
            paveButton.grid(row=5, column=1)
            cylindreButton=Button(frameAire, text="10.Cylindre", command=cylindre, width=20, pady=5)
            cylindreButton.grid(row=5, column=2)
            sphereButton=Button(frameAire, text="11.Sphère", command=sphere, width=20, pady=5)
            sphereButton.grid(row=6, column=1)

            #Bouton Retour

            def retourAire():
                frameAire.destroy()
                chap1Menu()
            retourAireButton=Button(frameAire, text="Retour", command=retourAire, width=20, background="blue", pady=5)
            retourAireButton.grid(row=1, column=10)

        #Partie Volume

        def volume():

            frameChap1.destroy()
            frameVolume=Frame(fenetrePrincipal)
            frameVolume.pack(side=TOP)

            #Fonctions pour le cube

            def cube():
                frameVolume.destroy()
                frameCube=LabelFrame(fenetrePrincipal, text="1. Volume d'un cube")
                frameCube.configure(font=fontTitle)
                frameCube.pack(side=TOP)

                entree=Spinbox(frameCube, textvariable=int, width=50, from_=0, to=1000000)
                entree.grid(row=1,column=1)
                
                frameDessin.pack()
                
                def resultat():
                    c=float(entree.get())
                    if c != 0:
                        aireCube.set("Aire = " + str((c**2)*6)+" unités²")
                        if c<176:
                            t.goto(0,0)
                            t.pendown()
                            for i in range(4):
                                t.forward(c)
                                t.left(90)
                            
                            t.goto(((1/2)*c),((1/2)*c))
                            
                            for i in range(4):
                                t.forward(c)
                                t.left(90)
                            
                            t.goto(((3/2)*c),((1/2)*c))
                            t.goto(c,0)
                            
                            t.goto(c,c)
                            t.goto(((3/2)*c),((3/2)*c))
                            
                            t.goto(((1/2)*c),((3/2)*c))
                            t.goto(0,c)
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée") 
                    else: 
                        showerror("Error", "Un côté ne peut pas être égal à 0")
                        volumeCube.set("Volume = ERROR")
                
                volumeCube = StringVar()

                Resultat=Label(frameCube, textvariable=volumeCube)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCube, text="Valider", command=resultat, background="green")
                validerButton.grid(row=3,column=1)
                def retourCube():
                    frameCube.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourCubeButton=Button(frameCube, text="Retour", command=retourCube, width=20, background="blue")
                retourCubeButton.grid(row=1, column=10)
            
            #Fonction pour le pave droit

            def pave():
                frameVolume.destroy()
                framePave=LabelFrame(fenetrePrincipal, text="2. Volume d'un pavé droit") 
                framePave.configure(font=fontTitle) 
                framePave.pack(side=TOP)

                longueur=Label(framePave, text="Longueur =")
                longueur.grid(row=1, column=1)
                entreel=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000)
                entreel.grid(row=1,column=2)

                largeur=Label(framePave, text="Largeur =")
                largeur.grid(row=2, column=1)
                entreeL=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000)
                entreeL.grid(row=2,column=2)

                hauteur=Label(framePave, text="Hauteur =")
                hauteur.grid(row=3, column=1)
                entreeH=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=3,column=2)

                frameDessin.pack()

                def resultat():
                    l=float(entreel.get())
                    L=float(entreeL.get())
                    H=float(entreeH.get())
                    if l and L and H != 0:
                        airePave.set("Aire = " + str(2*(l*L+L*H+l*H))+" unités²")

                        if l or L or H < 176:

                            t.goto(0,0)
                            t.pendown()
                            for i in range(2):
                                t.forward(l)
                                t.left(90)
                                t.forward(L)
                                t.left(90)
                            
                            t.goto((1/2)*H,(1/2)*L)
                            
                            for i in range(2):
                                t.forward(l)
                                t.left(90)
                                t.forward(L)
                                t.left(90)
                            t.forward(l)
                            t.goto(l,0)
                            
                            t.goto(l,L)
                            t.goto((3/2)*l,(3/2)*L)
                            t.back(l)
                            
                            t.goto(0,L)
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessinée") 
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre égale à 0")
                        airePave.set("Aire = ERROR")
                
                volumePave = StringVar()

                Resultat=Label(framePave, textvariable=volumePave)
                Resultat.grid(row=4,column=1)
                            
                
                validerButton=Button(framePave, text="Valider", command=resultat, background="green")
                validerButton.grid(row=5,column=1)
                def retourPave():
                    framePave.destroy()
                    frameDessin.pack_forget()
                    volume()
                retourPaveButton=Button(framePave, text="Retour", command=retourPave, width=20, background="blue")
                retourPaveButton.grid(row=1, column=10) 

            #Fonctions pour le cylindre

            def cylindre():
                frameVolume.destroy()
                frameCylindre=LabelFrame(fenetrePrincipal, text="3. Volume d'un cylindre")
                frameCylindre.configure(font=fontTitle)
                frameCylindre.pack(side=TOP)

                rayon=Label(frameCylindre, text="Rayon =")
                rayon.grid(row=1, column=1)
                entreeR=Spinbox(frameCylindre, textvariable=int, width=50, from_=0, to=1000000)
                entreeR.grid(row=1,column=2)

                hauteur=Label(frameCylindre, text="Hauteur =")
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameCylindre, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeR.get()) != 0:
                        volumeCylindre.set("Volume = " + str(2*pi*float(entreeR.get())*float(entreeH.get()))+" unités³")
                    else: 
                        showerror("Error", "Un rayon ne peut pas être égal à 0")
                        volumeCylindre.set("Volume = ERROR")
                
                volumeCylindre = StringVar()

                Resultat=Label(frameCylindre, textvariable=volumeCylindre)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameCylindre, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourCylindre():
                    frameCylindre.destroy()
                    volume()
                retourCylindreButton=Button(frameCylindre, text="Retour", command=retourCylindre, width=20, background="blue")
                retourCylindreButton.grid(row=1, column=10)
            
            #Fonctions pour la pyramide a base carré

            def pyramidecarre():
                frameVolume.destroy()
                framePyramideCarre=LabelFrame(fenetrePrincipal, text="4. Volume d'une pyramide à base carrée")
                framePyramideCarre.configure(font=fontTitle)
                framePyramideCarre.pack(side=TOP)

                cote=Label(framePyramideCarre, text="Coté =")
                cote.grid(row=1, column=1)
                entreeC=Spinbox(framePyramideCarre, textvariable=int, width=50, from_=0, to=1000000)
                entreeC.grid(row=1,column=2)

                hauteur=Label(framePyramideCarre, text="Hauteur =")
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(framePyramideCarre, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeC.get()) != 0:
                        volumePyramideCarre.set("Volume = " + str(((float(entreeC.get())**2)*float(entreeH.get()))/3)+" unités³")
                    else: 
                        showerror("Error", "Un coté ou une hauteur ne peut pas être égal à 0")
                        volumePyramideCarre.set("Volume = ERROR")
                
                volumePyramideCarre = StringVar()

                Resultat=Label(framePyramideCarre, textvariable=volumePyramideCarre)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(framePyramideCarre, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourPyramideCarre():
                    framePyramideCarre.destroy()
                    volume()
                retourPyramideCarreButton=Button(framePyramideCarre, text="Retour", command=retourPyramideCarre, width=20, background="blue")
                retourPyramideCarreButton.grid(row=1, column=10)
            
            #Fonctions pour la pyramide a base autre

            def pyramideautre():
                frameVolume.destroy()
                framePyramide=LabelFrame(fenetrePrincipal, text="5. Volume d'une pyramide")
                framePyramide.configure(font=fontTitle)
                framePyramide.pack(side=TOP)

                aireBase=Label(framePyramide, text="Aire de la base =")
                aireBase.grid(row=1, column=1)
                entreeB=Spinbox(framePyramide, textvariable=int, width=50, from_=0, to=1000000)
                entreeB.grid(row=1,column=2)

                hauteur=Label(framePyramide, text="Hauteur =")
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(framePyramide, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeB.get()) != 0:
                        volumePyramide.set("Volume = " + str((float(entreeB.get())*float(entreeH.get()))/3)+" unités³")
                    else: 
                        showerror("Error", "Un coté ou une hauteur ne peut pas être égal à 0")
                        volumePyramide.set("Volume = ERROR")
                
                volumePyramide = StringVar()

                Resultat=Label(framePyramide, textvariable=volumePyramide)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(framePyramide, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourPyramide():
                    framePyramide.destroy()
                    volume()
                retourPyramideButton=Button(framePyramide, text="Retour", command=retourPyramide, width=20, background="blue")
                retourPyramideButton.grid(row=1, column=10)

            #Fonctions pour le cone

            def cone():
                frameVolume.destroy()
                frameCone=LabelFrame(fenetrePrincipal, text="6. Volume d'un cône")
                frameCone.configure(font=fontTitle)
                frameCone.pack(side=TOP)

                rayon=Label(frameCone, text="Rayon =")
                rayon.grid(row=1, column=1)
                entreeR=Spinbox(frameCone, textvariable=int, width=50, from_=0, to=1000000)
                entreeR.grid(row=1,column=2)

                hauteur=Label(frameCone, text="Hauteur =")
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameCone, textvariable=int, width=50, from_=0, to=1000000)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeR.get()) != 0:
                        volumeCone.set("Volume = " + str((pi*(float(entreeR.get())**2)*float(entreeH.get()))/3)+" unités³")
                    else: 
                        showerror("Error", "Un rayon ou la hauteur ne peut pas être égal à 0")
                        volumeCone.set("Volume = ERROR")
                
                volumeCone = StringVar()

                Resultat=Label(frameCone, textvariable=volumeCone)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameCone, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
                def retourCone():
                    frameCone.destroy()
                    volume()
                retourConeButton=Button(frameCone, text="Retour", command=retourCone, width=20, background="blue")
                retourConeButton.grid(row=1, column=10)
            
            #Fonctions pour le sphere

            def sphere():
                frameVolume.destroy()
                frameSphere=LabelFrame(fenetrePrincipal, text="7. Volume d'une sphère")
                frameSphere.configure(font=fontTitle)
                frameSphere.pack(side=TOP)

                entree=Spinbox(frameSphere, textvariable=int, width=50, from_=0, to=1000000)
                entree.grid(row=1,column=1)
                
                def resultat():
                    if float(entree.get()) != 0:
                        volumeSphere.set("Volume = " + str((float(entree.get())**2)*(4/3)*pi)+" unités³")
                    else: 
                        showerror("Error", "Un rayon ne peut pas être égal à 0")
                        volumeSphere.set("Volume = ERROR")
                
                volumeSphere = StringVar()

                Resultat=Label(frameSphere, textvariable=volumeSphere)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameSphere, text="Valider", command=resultat, background="green")
                validerButton.grid(row=3,column=1)
                def retourSphere():
                    frameSphere.destroy()
                    volume()
                retourSphereButton=Button(frameSphere, text="Retour", command=retourSphere, width=20, background="blue")
                retourSphereButton.grid(row=1, column=10)

            #Boutons volume

            cubeButton=Button(frameVolume, text="1.Cube", command=cube, width=20, pady=5)
            cubeButton.grid(row=1, column=1)
            paveButton=Button(frameVolume, text="2.Pavé Droit", command=pave, width=20, pady=5)
            paveButton.grid(row=1, column=2)
            cylindreButton=Button(frameVolume, text="3.Cylindre", command=cylindre, width=20, pady=5)
            cylindreButton.grid(row=2, column=1)
            pyramidecarreButton=Button(frameVolume, text="4.Pyramide à base carré", command=pyramidecarre, width=20, pady=5)
            pyramidecarreButton.grid(row=2, column=2)
            pyramideautreButton=Button(frameVolume, text="5.Pyramide à base particulière", command=pyramideautre, width=20, pady=5)
            pyramideautreButton.grid(row=3, column=1)
            coneButton=Button(frameVolume, text="6.Cone", command=cone, width=20, pady=5)
            coneButton.grid(row=3, column=2)
            sphereButton=Button(frameVolume, text="7.Sphère", command=sphere, width=20, pady=5)
            sphereButton.grid(row=4, column=1)

            def retourVolume():
                frameVolume.destroy()
                chap1Menu()
            retourVolumeButton=Button(frameVolume, text="Retour", command=retourVolume, width=20, background="blue", pady=5)
            retourVolumeButton.grid(row=1, column=10)

        def retourChap1():
            frameChap1.destroy()
            principal()
            
        retourChap1Button=Button(frameChap1, text="Retour", command=retourChap1, width=20, background="blue", pady=5)
        retourChap1Button.grid(row=1, column=10)

        perimetreButton=Button(frameChap1, command=perimetre, width=20, text="1.Périmètre", pady=5)
        perimetreButton.grid(row=1,column=1)
        aireButton=Button(frameChap1, text="2.Aire", command=aire, width=20, pady=5)
        aireButton.grid(row=1,column=2)
        volumeButton=Button(frameChap1, text="3.Volume", command=volume, width=20, pady=5)
        volumeButton.grid(row=2,column=1)

    def chap2Menu():
        framePrincipal.destroy()
        frameChap2=Frame(fenetrePrincipal)
        frameChap2.pack()

        def denombrement():
            frameChap2.destroy()
            frameDenombrement=Frame(fenetrePrincipal)
            frameDenombrement.pack()

            def ordre():
                frameDenombrement.destroy()
                frameOrdre=LabelFrame(fenetrePrincipal, text="1. Ordre pris en compte")
                frameOrdre.configure(font=fontTitle)
                frameOrdre.pack()

                N=Label(frameOrdre, text="L'effectif N = ")
                N.grid(row=1,column=1)
                entreeN=Spinbox(frameOrdre, textvariable=int, width=50, from_=0, to=1000000)
                entreeN.grid(row=1,column=2)

                K=Label(frameOrdre, text="Nombre d'éléments K de N = ")
                K.grid(row=2,column=1)
                entreeK=Spinbox(frameOrdre, textvariable=int, width=50, from_=0, to=1000000)
                entreeK.grid(row=2,column=2)

                def resultat():
                    if float(entreeK.get()) > float(entreeN.get()):
                        showerror("Error", "Il y a plus d'éléments de K que d'effectif N")
                        valeurOrdre.set("Arangements = ERROR")
                    elif float(entreeK.get()) == float(entreeN.get()):
                        valeurOrdre.set("Permutations = " + str(factorial(float(entreeN.get()))))
                    else:
                        valeurOrdre.set("Arangements = "+str((factorial(float(entreeN.get())))/factorial((float(entreeN.get()))-float(entreeK.get()))))

                valeurOrdre = StringVar()

                Resultat=Label(frameOrdre, textvariable=valeurOrdre)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameOrdre, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)

                def retourOrdre():
                    frameOrdre.destroy()
                    denombrement()
            
                retourOrdreButton=Button(frameOrdre, text="Retour", command=retourOrdre, width=20, background="blue")
                retourOrdreButton.grid(row=1, column=10)
            

            def noOrdre():
                frameDenombrement.destroy()
                frameNoOrdre=Frame(fenetrePrincipal, text="2. Ordre non pris en compte")
                frameNoOrdre.configure(font=fontTitle)
                frameNoOrdre.pack()

                N=Label(frameNoOrdre, text="L'effectif N = ")
                N.grid(row=1,column=1)
                entreeN=Spinbox(frameNoOrdre, textvariable=int, width=50, from_=0, to=1000000)
                entreeN.grid(row=1,column=2)

                K=Label(frameNoOrdre, text="Nombre d'éléments K de N = ")
                K.grid(row=2,column=1)
                entreeK=Spinbox(frameNoOrdre, textvariable=int, width=50, from_=0, to=1000000)
                entreeK.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeK.get()) > float(entreeN.get()):
                        showerror("Error", "Il y a plus d'éléments de K que d'effectif N")
                        valeurNoOrdre.set("Nombre de combinaisons = ERROR")
                    else:
                        valeurNoOrdre.set("Nombre de combinaisons = "+str(factorial(float(entreeN.get()))/(factorial(float(entreeK.get()))*factorial(float(entreeN.get())-float(entreeK.get())))))
                
                valeurNoOrdre = StringVar()

                Resultat=Label(frameNoOrdre, textvariable=valeurNoOrdre)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameNoOrdre, text="Valider", command=resultat, background="green")
                validerButton.grid(row=4,column=1)
            
                def retourNoOrdre():
                    frameNoOrdre.destroy()
                    denombrement()
            
                retourNoOrdreButton=Button(frameNoOrdre, text="Retour", command=retourNoOrdre, width=20, background="blue")
                retourNoOrdreButton.grid(row=1, column=10)

            ordreButton=Button(frameDenombrement, text="1.Ordre pris en compte", command=ordre, pady=5)
            ordreButton.grid(row=1, column=1)
            noOrdreButton=Button(frameDenombrement, text="2.Ordre non pris en compte", command=noOrdre, pady=5)
            noOrdreButton.grid(row=1, column=2)

            def retourDenombrement():
                frameDenombrement.destroy()
                chap2Menu()
            
            retourDenombrementButton=Button(frameDenombrement, text="Retour", command=retourDenombrement, width=20, background="blue", pady=5)
            retourDenombrementButton.grid(row=1, column=10)

        denombrementButton=Button(frameChap2, text="1.Dénombrements et Combinaisons", command=denombrement, width=30, pady=5)
        denombrementButton.grid(row=1, column=1)


        def retourChap2():
            frameChap2.destroy()
            principal()
            
        retourChap2Button=Button(frameChap2, text="Retour", command=retourChap2, width=20, background="blue", pady=5)
        retourChap2Button.grid(row=1, column=10)
    
    def chap3Menu():
        framePrincipal.destroy()
        framePremier=LabelFrame(fenetrePrincipal, text="Nombre Premier")
        framePremier.pack()

        entree=Spinbox(framePremier, textvariable=int, width=50, from_=0, to=1000000)
        entree.grid(row=1, column=1)
        
        def estPremier():
            n=int(entree.get())
            print(n)
            for i in range(2, n+1):
                if n%i==0:
                    valeurResultat.set(str(n)+" n'est pas premier")
                else:
                    valeurResultat.set(str(n)+" est premier")
        
        valeurResultat= StringVar()
        Resultat=Label(framePremier, textvariable=valeurResultat)
        Resultat.grid(row=2, column=1)
        
        estPremierButton=Button(framePremier, text="Vérifier", command=estPremier)
        estPremierButton.grid(row=1, column=2)
    
    def chap4Menu():
        framePrincipal.destroy()
        frameChap4=Frame(fenetrePrincipal)
        frameChap4.pack()

        def distance():
            frameChap4.pack_forget()
            frameDistance=LabelFrame(fenetrePrincipal, text="1. Conversions de Distance")
            frameDistance.configure(font=fontTitle)
            frameDistance.pack()

            resultatConvertis=StringVar()

            def valider():
                entree2.grid_forget()

                if distance1.get() == 'kilomètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**4))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**5))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**6))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**9))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**12))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if distance1.get() == 'hectomètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**4))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**5))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**8))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**11))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if distance1.get() == 'décamètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**4))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**7))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**10))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                    
                if distance1.get() == 'mètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**6))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**9))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if distance1.get() == 'décimètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-4))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**5))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**8))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if distance1.get() == 'centimètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-5))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-4))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**4))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**7))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if distance1.get() == 'millimètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-6))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-5))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-4))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**6))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if distance1.get() == 'micromètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-9))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-8))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-7))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-6))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-5))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-4))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if distance1.get() == 'micromètre':
                    if distance2.get() == 'kilomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-12))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'hectomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-11))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décamètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-10))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'mètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-9))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'décimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-8))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'centimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-7))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'millimètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-6))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'micromètre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=3)
                    elif distance2.get() == 'nanomètre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)

                
            
            distance1=ttk.Combobox(frameDistance)
            distance1.grid(row=2,column=1)

            distance1['values']=('kilomètre',
                                'hectomètre',
                                'décamètre',
                                'mètre',
                                'décimètre',
                                'centimètre',
                                'millimètre',
                                'micromètre',
                                'nanomètre',
                                '         ')
            distance1.current(9)

            distance2=ttk.Combobox(frameDistance)
            distance2.grid(row=2,column=3)

            distance2['values']=('kilomètre',
                                'hectomètre',
                                'décamètre',
                                'mètre',
                                'décimètre',
                                'centimètre',
                                'millimètre',
                                'micromètre',
                                'nanomètre',
                                '          ')
            distance2.current(9)

            fleche1=Label(frameDistance, text="=>")
            fleche1.grid(row=2,column=2)
            fleche2=Label(frameDistance, text="=>")
            fleche2.grid(row=3,column=2)

            entree1=Spinbox(frameDistance, textvariable=int, width=50, from_=0, to=1000000)
            entree1.grid(row=3,column=1)

            

            entree2=Label(frameDistance, textvariable=resultatConvertis, width=50)
            entree2.grid(row=3,column=3)

            valider=Button(frameDistance, text="Valider", command=valider)
            valider.grid(row=3, column=4)

            def retourDistance():
                frameDistance.destroy()
                chap4Menu()
                
            retourDistanceButton=Button(frameDistance, text="Retour", command=retourDistance, width=20, background="blue", pady=5)
            retourDistanceButton.grid(row=2, column=10)
        
        def surface():
            frameChap4.pack_forget()
            frameSurface=LabelFrame(fenetrePrincipal, text="2. Conversion de Surface")
            frameSurface.configure(font=fontTitle)
            frameSurface.pack()

            resultatConvertis=StringVar()
            unite1=StringVar()
            unite2=StringVar()

            def valider():
                entree2.grid_forget()

                

                if surface1.get() == 'kilomètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get()))+" km²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" hm²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" dam²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" m²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**8)+" dm²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**10)+" cm²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**12)+" mm²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**18)+" µm²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**24)+" nm²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**6)+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**7)+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**9)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39)+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if surface1.get() == 'hectomètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get()))+" hm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" dam²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" m²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" dm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10*8)+" cm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**10)+" mm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**16)+" µm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**22)+" nm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**5)+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**6)+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**8)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-1))+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if surface1.get() == 'décamètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" hm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" dam²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" m²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" dm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" cm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**8)+" mm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**14)+" µm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**20)+" nm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**1)+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**4)+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**5)+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**7)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-2))+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                    
                if surface2.get() == 'mètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" hm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" dam²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" m²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" dm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" cm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" mm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**12)+" µm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**18)+" nm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**3)+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**4)+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**6)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-3))+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if surface1.get() == 'décimètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-8)+" km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" hm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" dam²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" m²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" dm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" cm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" mm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**10)+" µm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**16)+" nm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-1))+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**2)+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**3)+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**5)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-4))+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if surface1.get() == 'centimètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-10)+" km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-8)+" hm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" dam²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" m²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" dm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" cm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" mm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**8)+" µm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**14)+" nm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-2))+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**1)+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**2)+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**4)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-5))+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if surface1.get() == 'millimètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-12)+" km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-10)+" hm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-8)+" dam²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" m²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" dm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" cm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" mm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" µm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**12)+" nm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-3))+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**0)+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**1)+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**3)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-6))+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if surface1.get() == 'micromètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-18)+" km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-16)+" hm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-14)+" dam²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-12)+" m²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-10)+" dm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-8)+" cm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" mm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" µm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" nm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-4))+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**(-1))+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**0)+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**2)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-7))+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                if surface1.get() == 'micromètre²':
                    if surface2.get() == 'kilomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-24)+" km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-22)+" hm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décamètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-20)+" dam²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-18)+" m²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'décimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-16)+" dm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'centimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-14)+" cm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'millimètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-12)+" mm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'micromètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" µm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'nanomètre²':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" nm²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-5))+" ha")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'yard²':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**(-2))+" yard²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pied²':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**(-1))+" pied²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'pouce²':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**1)+" pouce²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    elif surface2.get() == 'mille²':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-8))+" mille²")
                        unite1.set("km²")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=3)
                
                

                
            
            surface1=ttk.Combobox(frameSurface)
            surface1.grid(row=2,column=1)

            surface1['values']=('kilomètre²',
                                'hectomètre²',
                                'décamètre²',
                                'mètre²',
                                'décimètre²',
                                'centimètre²',
                                'millimètre²',
                                'micromètre²',
                                'nanomètre²',
                                #'hectare',
                                #'yard²',
                                #'pied²',
                                #'pouce²',
                                #'mille²',
                                '         ')
            surface1.current(9)

            surface2=ttk.Combobox(frameSurface)
            surface2.grid(row=2,column=4)

            surface2['values']=('kilomètre²',
                                'hectomètre²',
                                'décamètre²',
                                'mètre²',
                                'décimètre²',
                                'centimètre²',
                                'millimètre²',
                                'micromètre²',
                                'nanomètre²',
                                'hectare',
                                'yard²',
                                'pied²',
                                'pouce²',
                                'mille²',
                                '          ')
            surface2.current(14)

            uniteLabel1=Label(frameSurface, textvariable=unite1)
            uniteLabel1.grid(row=3,column=2)

            fleche1=Label(frameSurface, text="=>")
            fleche1.grid(row=2,column=3)
            fleche2=Label(frameSurface, text="=>")
            fleche2.grid(row=3,column=3)

            entree1=Spinbox(frameSurface, textvariable=int, width=50, from_=0, to=1000000)
            entree1.grid(row=3,column=1)

            

            entree2=Label(frameSurface, textvariable=resultatConvertis, width=50)
            entree2.grid(row=3,column=4)

            valider=Button(frameSurface, text="Valider", command=valider)
            valider.grid(row=3, column=6)

            def retourSurface():
                frameSurface.destroy()
                chap4Menu()
                
            retourSurfaceButton=Button(frameSurface, text="Retour", command=retourSurface, width=20, background="blue", pady=5)
            retourSurfaceButton.grid(row=2, column=10)
        

        distanceButton=Button(frameChap4, command=distance, text="Distance", width=20, pady=5)
        distanceButton.grid(row=1,column=1)
        surfaceButton=Button(frameChap4, command=surface, text="Surface", width=20, pady=5)
        surfaceButton.grid(row=1,column=2)

        def retourChap4():
            frameChap4.destroy()
            principal()
            
        retourChap4Button=Button(frameChap4, text="Retour", command=retourChap4, width=20, background="blue", pady=5)
        retourChap4Button.grid(row=1, column=10)

    def chap5Menu():
        framePrincipal.destroy()
        frameChap5=LabelFrame(fenetrePrincipal, text="5. Triangles rectangles")
        frameChap5.configure(font=fontTitle)
        frameChap5.pack()


        def valider():
            a=float(entreeA.get())
            b=float(entreeB.get())
            c=float(entreeC.get())
            if a**2+b**2==c**2:
                valeurResultat.set("Le triangle est rectangle")
            else:
                valeurResultat.set("Le triangle n'est pas rectangle")

        valeurResultat=StringVar()
        Resultat=Label(frameChap5, textvariable=valeurResultat)
        Resultat.grid(row=3,column=2)

        labelA=Label(frameChap5, text="Premier coté")
        labelA.grid(row=1,column=1)
        entreeA=Spinbox(frameChap5, textvariable=int, width=50, from_=0, to=1000000)
        entreeA.grid(row=2,column=1)
        
        labelB=Label(frameChap5, text="Second coté")
        labelB.grid(row=1,column=2)
        entreeB=Spinbox(frameChap5, textvariable=int, width=50, from_=0, to=1000000)
        entreeB.grid(row=2,column=2)

        labelC=Label(frameChap5, text="Plus long coté")
        labelC.grid(row=1,column=3)
        entreeC=Spinbox(frameChap5, textvariable=int, width=50, from_=0, to=1000000)
        entreeC.grid(row=2,column=3)

        validerButton=Button(frameChap5, text="Valider", command=valider, width=10)
        validerButton.grid(row=2,column=4)

        def retourChap5():
            frameChap5.destroy()
            principal()
            
        retourChap5Button=Button(frameChap5, text="Retour", command=retourChap5, width=20, background="blue", pady=5)
        retourChap5Button.grid(row=1, column=10)
    
    def chap6Menu():
        framePrincipal.destroy()
        frameChap6=LabelFrame(fenetrePrincipal, text="6. Dérivation")
        frameChap6.configure(font=fontTitle)
        frameChap6.pack()

        x=Symbol('x')

        def valider():
            fstr=str(fonctionsEntree.get())
            f=sympify(fstr)
            f_prime=f.diff(x)
            resultatValeur.set(f_prime)

        resultatValeur=StringVar()

        fonctionsEntree=Entry(frameChap6, width=100)
        fonctionsEntree.grid(row=1,column=2)
        fonctionsDerive=Label(frameChap6, textvariable=resultatValeur, width=20, pady=5)
        fonctionsDerive.grid(row=3,column=2)
        validerButton=Button(frameChap6, text="Valider", command=valider, width=20, pady=5)
        validerButton.grid(row=1,column=3)

        def retourChap6():
            frameChap6.destroy()
            principal()
            
        retourChap5Button=Button(frameChap6, text="Retour", command=retourChap6, width=20, background="blue", pady=5)
        retourChap5Button.grid(row=1, column=10)


    framePrincipal=Frame(fenetrePrincipal, borderwidth=2)
    framePrincipal.pack(side=TOP)
    chap1Button=Button(framePrincipal, text="1.Périmètre, Aire, Volume", command=chap1Menu, width=20, pady=5)
    chap1Button.grid(row=1,column=1)
    chap2Button=Button(framePrincipal, text="2.Probabilité", command=chap2Menu, width=20, pady=5)
    chap2Button.grid(row=1,column=2)
    chap3Button=Button(framePrincipal, text="3.Nombres premier", command=chap3Menu, width=20, pady=5)
    #chap3Button.grid(row=2,column=1)
    chap4Button=Button(framePrincipal, text="4.Conversions", command=chap4Menu, width=20, pady=5)
    chap4Button.grid(row=2,column=2)
    chap5Button=Button(framePrincipal, text="5.Triangles rectangles", command=chap5Menu, width=20, pady=5)
    chap5Button.grid(row=3,column=1)
    chap6Button=Button(framePrincipal, text="6.Dérivation", command=chap6Menu, width=20, pady=5)
    chap6Button.grid(row=3,column=2)
    #chap11Button=Button(framePrincipal, text="11.Equation", command=chap11Menu)
    #chap7Button=Button(framePrincipal, text="7.Espaces", command=chap7Menu)
    #chap8Button=Button(framePrincipal, text="8.Théorème de Thalès", command=chap8Menu)
    #chap9Button=Button(framePrincipal, text="9.Orthogonalité", command=chap9Menu)
    #chap10Button=Button(framePrincipal, text="10.Trigonométrie", command=chap10Menu)
    

fenetrePrincipal = Tk()
fenetrePrincipal.title('CALCUL V3.0')
fenetrePrincipal.configure(background='gray70')

frameExit=Frame(fenetrePrincipal, padx=200, background='gray70')
frameExit.pack(side=BOTTOM)

close=Button(frameExit, text="Fermer", command=fenetrePrincipal.quit, background="red", activebackground="red", width=10, heigh=5)
close.grid(row=1,column=1)

#Commande de plein écran

def fullscreenDestroy():
    fenetrePrincipal.attributes('-fullscreen', False)
def fullscreenActive():
    fenetrePrincipal.attributes('-fullscreen', True)

fenetrePrincipal.attributes('-fullscreen', True)
fenetrePrincipal.bind('<Escape>', lambda e: fullscreenDestroy())
fenetrePrincipal.bind('<F11>', lambda e: fullscreenActive())

principal()

fenetrePrincipal.mainloop()