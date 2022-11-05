'''import cv2
import numpy as np

leo = cv2.imread('image/leonel.jpg',cv2.IMREAD_COLOR)
cv2.putText(leo,"Python Examples",(50,450),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255), 3)
cv2.imshow('leonel',leo)

#cv2.imshow('leonel', cv2.resize(leo,(1200,720),interpolation = cv2.INTER_CUBIC))

cv2.waitKey(0)
cv2.destroyAllWindows()'''

#pip install tk pour intaller la biblioteque tkinter sous windows

from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk
import PIL
import tkinter as tk

#Create an instance of tkinter frame
win = Tk() #ouvre la fenetre general de tkinter
win.geometry("1000x720") # la taille de la fenetre

#Load the image
path_image = "image/mehemet.jpg" # chemin de l'image
resize_dim = (640,480) #taille de redimentionement de l'image

img = cv2.imread(path_image)#lis l'image avec opencv pour l'afficher
image = PIL.Image.open(path_image)#lis l'image pour extraire ses dimention

resized_image = cv2.resize(img, resize_dim, interpolation = cv2.INTER_AREA) #redimensioner l'image

width, height = image.size #extrait les dimention de l'image initial
print(width,height)#affiche les dimention de l'image initiale

#Rearrange colors
blue,green,red = cv2.split(resized_image)
img = cv2.merge((red,green,blue))
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)

texte = "Hoşgeldiniz mehemet bey"
l = Label(win, text = texte)# creation du label texte
l.config(font =("Courier", 14)) #la police du texte et la taille
l.config(fg='yellow')
#l.config(bg='white', fg='yellow') la couleur et le font du texte
l.config(height=9, width=100) # une surface totale de 9 lignes sur 100 caractères.
l.pack(side=BOTTOM) #position du label texte

#Create a Label to display the image
l.pack()
Label(win, image= imgtk).pack()
win.mainloop()

# link :https://www.fil.univ-lille1.fr/~marvie/python/chapitre6.html#manipulation-de-texte