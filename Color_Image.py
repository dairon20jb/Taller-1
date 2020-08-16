import math
import numpy as np
import cv2
import os
class ColorImage:
    def __init__(self,string):
        self.string= string
        image_name = 'lena.png'
        self.carga_imagen= cv2.imread(os.path.join(string, image_name))
    def display_Properties(self):
        cv2.imshow('Imagen', self.carga_imagen)
        cv2.waitKey(0)
        print("- Dimensiones de la imagen:")
        print(self.carga_imagen.shape)
    def make_Gray(self):
        gris = cv2.cvtColor(self.carga_imagen, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Imagen', gris)
        cv2.waitKey(0)
    def colorize_RGB(self,canal):
        if canal == "rojo":
            b=self.carga_imagen
            b[:, :, 0] = 0
            b[:, :, 1] = 0
            cv2.imshow('Imagen',b)
            cv2.waitKey(0)
        if canal == "verde":
            b = self.carga_imagen
            b[:, :, 0] = 0
            b[:, :, 2] = 0
            cv2.imshow('Imagen', b)
            cv2.waitKey(0)
        if canal == "azul":
            b = self.carga_imagen
            b[:, :, 1] = 0
            b[:, :, 2] = 0
            cv2.imshow('Imagen', b)
            cv2.waitKey(0)

    def make_Hue(self):
        hsv = cv2.cvtColor(self.carga_imagen, cv2.COLOR_BGR2HSV)
        hsv[:,:,1] = 255
        hsv[:,:,2] = 255
        hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('Imagen', hsv)
        cv2.waitKey(0)