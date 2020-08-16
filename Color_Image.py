import math
import numpy as np
import cv2
import os
class ColorImage: # Se crea la clase ColorImage
    def __init__(self,string,image_name): #Constructor definición
        self.string= string # String es la ruta de la imagen
        self.image_name = image_name
        self.carga_imagen= cv2.imread(os.path.join(self.string,self.image_name)) #Carga la imagen dada la dirección y nombre de la imagen
    def display_Properties(self):
        cv2.imshow('Imagen Original', self.carga_imagen) # Imagen original visualización
        print("Las dimensiones de la imagen son:")
        print(self.carga_imagen.shape[1], "pixeles de ancho por", self.carga_imagen.shape[0], "pixeles de alto" ) # Se imprimen las respectivas dimensiones de la imagen
    def make_Gray(self):
        gris = cv2.cvtColor(self.carga_imagen, cv2.COLOR_BGR2GRAY) #Imagen convertida a escala de grises
        cv2.imshow('Imagen en grises', gris)
    def colorize_RGB(self,canal):
        if canal == "Rojo":  # Los canales Verde y Azul se convierten en cero si el canal de color seleccionado es Rojo
            b=self.carga_imagen.copy()
            b[:, :, 0] = 0
            b[:, :, 1] = 0 
            cv2.imshow('Imagen Rojiza',b)# Se visualiza imagen Rojiza
        if canal == "Verde": # Los canales Rojo y Azul se convierten en cero si el canal de color seleccionado es Verde
            b = self.carga_imagen.copy()
            b[:, :, 0] = 0
            b[:, :, 2] = 0
            cv2.imshow('Verdoza', b) # Se visualiza imagen Verdoza
        if canal == "Azul": # Los canales Verde y Rojo se convierten en cero si el canal de color seleccionado es Azul
            b = self.carga_imagen.copy()
            b[:, :, 1] = 0
            b[:, :, 2] = 0
            cv2.imshow('Imagen Azuloza', b)# Se visualiza imagen Azuloza
    def make_Hue(self):
        hsv = cv2.cvtColor(self.carga_imagen, cv2.COLOR_BGR2HSV) # Imagen transformada al espacio HSV
        hsv[:,:,1] = 255 # Componente S en 255
        hsv[:,:,2] = 255 # Componente v en 255
        hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Imagen transformada al espacio RGB de nuevo
        cv2.imshow('Imagen Tonos Resaltados', hsv) # Se visualiza la imagen obtenida
