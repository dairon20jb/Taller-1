from  Color_Image import * #

if __name__ == '__main__': #
    print("Digite la ruta de la carpeta")
    direccion = 'C:\PRUEBA'
    Mi_Instancia = ColorImage(direccion)
    Mi_Instancia.display_Properties()
    Mi_Instancia.colorize_RGB('verde')
    Mi_Instancia.make_Gray()
    Mi_Instancia.make_Hue()

