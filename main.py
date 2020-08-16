from  Color_Image import * # Importando
if __name__ == '__main__': #
    direccion = input('Digite la ruta de la imagen: ') # Dirección de la carpeta en la que se encuentra la imagen
    nombre_imagen = input('Digite el nombre de la imagen: ') # Nombre de la imagen a cargar, se debe incluir el formato (.png)
    canal_color = input('Digite el canal de color deseado: ') #Elige entre Rojo, Verde y Azul
    Mi_Instancia = ColorImage(direccion,nombre_imagen)#LLamado clase
    Mi_Instancia.display_Properties()# Se visualiza la imagen original y se imprimen las respecivas dimensiones de esta
    Mi_Instancia.colorize_RGB(canal_color) # Visualiza la imagen en el canal previamente indicado
    Mi_Instancia.make_Gray() # Imagen escala de grises
    Mi_Instancia.make_Hue() # Imagen tonos resaltados
    cv2.waitKey(0)
