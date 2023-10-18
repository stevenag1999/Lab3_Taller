################
### LIBRERIAS ###
################
#-------------------------------------------------------
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import serial
import time
#-------------------------------------------------------





############################
### COMUNICACIÓN SERIAL ###
############################
#-------------------------------------------------------
# Iniciar puerto serial de Arduino
arduino = serial.Serial('COM6', 115200)

#Resetear arduino
arduino.setDTR(False)
arduino.flushInput()
arduino.setDTR(True)
#-------------------------------------------------------





#################################
### FUNCIONES DE LOS BOTONES ###
#################################
#-------------------------------------------------------
# Función para simular la adquisición de datos
def adquirir_datos(canalP):
        global datos_canal1, datos_canal2
        
        if canalP == 1:         #Adquisión de datos solo para el canal 1
            datos1 = []
            arduino.flushInput()    #Limpiar algún residuo que haya
            while True:
                if len(datos1) == max_muestras:         #Cuando tenga la cantidad de muestras que quiero, corto
                    datos_canal1 = datos1
                    break
                else:
                    try:
                            dato = float(arduino.readline().decode().strip())   #Adquirir datos para el canal 1
                            datos1.append(dato*5/255)
                    except:
                            cp = 2


        if canalP == 2:         #Adquisión de datos solo para el canal 2
            datos2 = []
            arduino.flushInput()    #Limpiar algún residuo que haya
            while True:
                if len(datos2) == max_muestras: #Cortar cuando se tengan las muestras que se quiere
                    datos_canal2 = datos2
                    break
                else:
                    try:
                            dato = float(arduino.readline().decode().strip())   #Adquirir datos para el canal 2
                            datos2.append(dato*5/255)   #decodificar valor
                    except:
                            cp = 2

        if canalP == 3:         #Adquisión de datos simultánea
            datos1 = []
            arduino.flushInput()    #Limpiar algún residuo que haya
            while True:
                if len(datos1) == max_muestras:
                    datos_canal1 = datos1
                    arduino.flushOutput()
                    comando = 0b11111111
                    arduino.write(bytes([comando])) #Informarle al arduino que el canal 1 está listo
                    break
                else:
                    try:
                            dato = float(arduino.readline().decode().strip())   #Adquirir datos para el canal 1
                            datos1.append(dato*5/255)
                    except:
                            cp = 2

            time.sleep(0.35)    #retardo para no mezclar datos

            datos2 = []
            arduino.flushInput()    #Limpiar algún residuo que haya
            while True:
                if len(datos2) == max_muestras:
                    datos_canal2 = datos2
                    arduino.flushOutput()
                    comando = 0b11111110
                    arduino.write(bytes([comando])) #Informarle al arduino que el canal 2 está listo
                    break
                else:
                    try:
                            dato = float(arduino.readline().decode().strip())   #Adquirir datos para el canal 2
                            datos2.append(dato*5/255)
                    except:
                            cp = 2

            time.sleep(0.2)
#-------------------------------------------------------

#-------------------------------------------------------
# Función para actualizar la gráfica en tiempo real
def graficar_datos():
    global contador, datos_canal1, datos_canal2

    # Borrar gráfica previa
    ax.clear()
    
    # Verificar si se debe graficar el Canal 1
    if ech1 == True and ech2 == False:
        adquirir_datos(1)       #Obtener Datos para el Canal 1
        if len(datos_canal1) > max_muestras:            # Gráfica fija en el tiempo
            datos_canal1 = datos_canal1[-max_muestras:]
        ax.plot(datos_canal1, label="Canal 1", linestyle='-', color='b')    #Graficar los datos del canal 1
        ax.legend()


    # Verificar si se debe graficar el Canal 2
    if ech2 == True and ech1 == False:
        adquirir_datos(2)       #Obtener Datos para el Canal 2
        if len(datos_canal2) > max_muestras:       # Gráfica fija en el tiempo
            datos_canal2 = datos_canal2[-max_muestras:]
        ax.plot(datos_canal2, label="Canal 2", linestyle='-', color='r') # Graficar datos del Canal 2
        ax.legend()

    if ech1 == True and ech2 == True:
        adquirir_datos(3)       #Obtener Datos para los canales 1 y 2
        if len(datos_canal1) > max_muestras:            # Gráfica fija en el tiempo
            datos_canal1 = datos_canal1[-max_muestras:]
        ax.plot(datos_canal1, label="Canal 1", linestyle='-', color='b')    #Graficar los datos del canal 1
        ax.legend()
        if len(datos_canal2) > max_muestras:       # Gráfica fija en el tiempo
            datos_canal2 = datos_canal2[-max_muestras:]
        ax.plot(datos_canal2, label="Canal 2", linestyle='-', color='r') # Graficar datos del Canal 2
        ax.legend()

    # Acción para borrar las gráficas cuando los canales estén desactivados
    if not(ech1) and not(ech2):
        print("Limpiando Gráficas... Por favor, espere un momento.")
        ax.clear()
        contador += 1
        if contador == 2:
            contador = 0
            return
    
    # etiquetas
    ax.set_xlabel('Muestras')
    ax.set_ylabel(mag_fis)
    
    # Actualización del canvas
    canvas.draw()

    # Intervalo de graficación
    root.after(50, graficar_datos)
#-------------------------------------------------------

#-------------------------------------------------------
# Función para almacenar  los datos de la sesión
def almacenar_datos():
        global ID, autor, fecha, mag_fis, escala, mag_fis2, escala2, ech1, ech2, datos_canal1, datos_canal2

        ID += 1 
        autor = autor_e.get()
        fecha = fecha_e.get()
        mag_fis = mag_fis_e.get()
        escala = combo_escalas.get()
        mag_fis2 = mag_fis2_e.get()
        escala2 = combo_escalas2.get()
        ech1 = activar_canal1.get()
        if ech1:
                c1 = "1"
                datos1 = datos_canal1
        else:
                c1 = "0"
                datos1 = [0]*max_muestras
        ech2 = activar_canal2.get()
        if ech2:
                c2 = "1"
                datos2 = datos_canal2
        else:
                c2 = "0"
                datos2 = [0]*max_muestras

        # Abrir  archivo en modo 'append'
        with open('datos.txt', 'a') as file:
                # Escribir información
                file.write("\n"+str(ID)+","+autor+","+fecha+","+mag_fis+","+str(escala)+","+mag_fis2+","+str(escala2)+","+"1"+","+"1"+",")
                for i in range(len(datos1)):
                    file.write(str(datos1[i]) + ",")
                for i in range(len(datos2)):
                    file.write(str(datos2[i]) + ",")

        # mostrar mensaje de éxito 
        print("\nDatos almacenados exitosamente.")
        print("\nSe almacena: ")
        print(ID, autor, fecha, mag_fis, escala, mag_fis2, escala2, c1, c2)
        print("")
        print("D1: ", datos1)
        print("")
        print("D2: ", datos2)

        # Limpiar listas auxiliares de datos
        datos1 = []
        datos2 = []

        file.close()
#-------------------------------------------------------

#-------------------------------------------------------
def cargar_datos():
    try:
        with open('datos.txt', 'r') as file:
                
            for line in file:

                for i in range(2):
                        ax.clear()
                
                columns = line.strip().split(',')       # Separar los datos en las columnas

                if len(columns) < 10:
                    print("La línea no contiene suficientes elementos:", line)
                    continue

                ID, autor, fecha, mag_fis, escala, mag_fis2, escala2, c1, c2, *datos = columns

                # Imprimir datos guardadosdos
                print("ID:", ID)
                print("Autor:", autor)
                print("Fecha:", fecha)
                print("Magnitud Física 1:", mag_fis)
                print("Escala 1:", escala)
                print("Magnitud Física 2:", mag_fis2)
                print("Escala 2:", escala2)
                print("Canal 1:", c1)
                print("Canal 2:", c2)

                # Convertir las cadenas de datos en listas de números
                datos1 = [float(value) if value else 0.0 for value in datos[:max_muestras]]
                datos2 = [float(value) if value else 0.0 for value in datos[max_muestras:]]

                print("Datos Canal 1: ", datos1)
                print("Datos Canal 2: ", datos2)

                # graficar datos
                if c1 == '1':
                    ax.plot(datos1, label="Canal 1", linestyle=':', color='b')
                if c2 == '1':
                    ax.plot(datos2, label="Canal 2", linestyle=':', color='r')
                ax.legend()
                ax.set_xlabel('Muestras')
                ax.set_ylabel(mag_fis)
                canvas.draw()

    except FileNotFoundError:
        print("El archivo de datos no existe.")
#-------------------------------------------------------

#-------------------------------------------------------
def determinar_comando(ech1, ech2, escala, escala2):
    comando = 0b00000000
    
    # Configurar el bit 0 según ech1
    if ech1:
        comando |= 0b00000001
    else:
        comando &= 0b11111110

    # Configurar el bit 1 según ech2
    if ech2:
        comando |= 0b00000010
    else:
        comando &= 0b11111101

    # Configurar los bits [2:4] según la escala 1
    if escala == "10 mV":
        comando |= 0b00000000
    elif escala == "100 mV":
        comando |= 0b00000100
    elif escala == "1 V":
        comando |= 0b00001000
    elif escala == "2.5 V":
        comando |= 0b00001100
    elif escala == "5 V":
        comando |= 0b00010000
    elif escala == "10 V":
        comando |= 0b00010100
    else:
        comando |= 0b00010000

    # Configurar los bits [5:7] según la escala 2
    if escala2 == "10 mV":
        comando |= 0b00000000
    elif escala2 == "100 mV":
        comando |= 0b00100000
    elif escala2 == "1 V":
        comando |= 0b01000000
    elif escala2 == "2.5 V":
        comando |= 0b01100000
    elif escala2 == "5 V":
        comando |= 0b10000000
    elif escala2 == "10 V":
        comando |= 0b10100000
    else:
        comando |= 0b10000000

    return comando
#-------------------------------------------------------

#-------------------------------------------------------
def actualizar_informacion():
        #arduino.flushOutput()    #Vaciar residuos de la comu serial
        
        global escala, escala2, ech1, ech2
        escala = combo_escalas.get()                #Escala ch1
        escala2 = combo_escalas2.get()
        ech1 = activar_canal1.get()     #Canal 1 activado?
        ech2 = activar_canal2.get()

        comando = determinar_comando(ech1, ech2, escala, escala2)       #Dterminar la instrucción a enviar

        arduino.write(bytes([comando]))
#-------------------------------------------------------





##########################################
### CONFI INICIAL Y VARIABLES AUXILIARES ###
##########################################
#-------------------------------------------------------
# Configuración inicial
#comando = 0b00000000    #(bit0:ch1), (bit1:ch2), (bits[2:4]:escala), (bits[5:7]:escala2)
ID = 0  # id grabaciones de datos
datos_canal1 = []  # datos canal 1
datos_canal2 = []
ech1 = False    #Activar canal 1?
ech2 = False    #Activar canal 2?
autor = ""
fecha = ""
mag_fis = ""
escala = ""
mag_fis2 = ""
escala2 = ""
contador = 0
max_muestras = 100
cp = 0     #Contador de prueba
#-------------------------------------------------------





###########################
######### VENTANAS #########
###########################
#-------------------------------------------------------
# Ventana principal
root = tk.Tk()
root.title("Sistema de Adquisición de Datos")
root.geometry("680x680") #Tamaño
#-------------------------------------------------------

#-------------------------------------------------------
# Frame para los elementos de la GUI
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=5, pady=10)
# 2 columnas talvez
#-------------------------------------------------------

#-------------------------------------------------------
# Espacio de graficacion
fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(row=5, column=0, columnspan=3, padx=5, pady=20)
ax.set_title('Visualización en Tiempo Real')
#-------------------------------------------------------






##########################
### DATOS DE LA SESIÓN ###
##########################
#-------------------------------------------------------
# Autor
autor_l = ttk.Label(frame, text="Autor:", width=10)
autor_l.grid(row=1, column=0, padx=5, pady=20)
autor_e = ttk.Entry(frame, width=20)
autor_e.grid(row=1, column=1, padx=5, pady=20)
#-------------------------------------------------------

#-------------------------------------------------------
# Fecha
fecha_l = ttk.Label(frame, text="Fecha:", width=10)
fecha_l.grid(row=1, column=2, padx=5, pady=20)
fecha_e = ttk.Entry(frame, width=20)
fecha_e.grid(row=1, column=3, padx=5, pady=20)
#-------------------------------------------------------






###################################
############# BOTONES #############
###################################
#-------------------------------------------------------
# Botón para apagar la aplicación
btn_apagar = ttk.Button(frame, text="Apagar", command=root.destroy, width=20)
btn_apagar.grid(row=0, column=0, padx=5, pady=20)
#-------------------------------------------------------

#-------------------------------------------------------
# Botón para graficar
btn_graficar = ttk.Button(frame, text="Graficar", command=graficar_datos, width=20)
btn_graficar.grid(row=0, column=1, padx=5, pady=20)
#-------------------------------------------------------

#-------------------------------------------------------
# Botón para almacenar datos
btn_almacenar_datos = ttk.Button(frame, text="Almacenar Datos", command=almacenar_datos, width=20)
btn_almacenar_datos.grid(row=0, column=2, padx=5, pady=20)
#-------------------------------------------------------

#-------------------------------------------------------
# Botón para cargar y graficar datos
btn_cargar_datos = ttk.Button(frame, text="Cargar Datos", command=cargar_datos, width=20)
btn_cargar_datos.grid(row=0, column=3, padx=5, pady=20)
#-------------------------------------------------------

#-------------------------------------------------------
# Botón para actualizar datos
btn_almacenar_datos = ttk.Button(frame, text="Actualizar Datos", command=actualizar_informacion, width=20)
btn_almacenar_datos.grid(row=5, column=3, padx=5, pady=20)
#-------------------------------------------------------






#################################
### ACTIVACIÓN DE LOS CANALES ###
#################################
#-------------------------------------------------------
# Variable para verificar si se debe graficar el canal 1
activar_canal1 = tk.BooleanVar()
activar_canal1.set(False)

# Variable para verificar si se debe graficar el canal 2
activar_canal2 = tk.BooleanVar()
activar_canal2.set(False)
#-------------------------------------------------------

#-------------------------------------------------------
# Checkbutton para activar/desactivar canal1
chk_graf_canal1 = ttk.Checkbutton(frame, text="Activar Canal 1", variable=activar_canal1)
chk_graf_canal1.grid(row=2, column=0, padx=5, pady=20)

# Checkbutton para activar/desactivar canal2
chk_graf_canal2 = ttk.Checkbutton(frame, text="Activar Canal 2", variable=activar_canal2)
chk_graf_canal2.grid(row=2, column=2, padx=5, pady=20)
#-------------------------------------------------------







#############################
### MAGNITUDES Y ESCALAS ###
#############################
#-------------------------------------------------------
# Magnitud física canal 1
lbl_magnitud = ttk.Label(frame, text="Magnitud Física (Canal 1)")
lbl_magnitud.grid(row=3, column=0, padx=5, pady=20)

mag_fis_e = ttk.Entry(frame, width=20)
mag_fis_e.grid(row=3, column=1, padx=5, pady=20)
#-------------------------------------------------------

#-------------------------------------------------------
# Escala 1
lbl_escalas = ttk.Label(frame, text="Escala (Canal 1)")
lbl_escalas.grid(row=4, column=0, padx=5, pady=20)

escalas = ["10 mV", "100 mV", "1 V", "2.5 V", "5 V", "10 V"]
combo_escalas = ttk.Combobox(frame, values=escalas)
combo_escalas.grid(row=4, column=1, padx=5, pady=20)
combo_escalas.set("Seleccionar")
#-------------------------------------------------------

#-------------------------------------------------------
# Magnitud Física 2
lbl_magnitud2 = ttk.Label(frame, text="Magnitud Física (Canal 2)")
lbl_magnitud2.grid(row=3, column=2, padx=5, pady=20)

mag_fis2_e = ttk.Entry(frame, width=20)
mag_fis2_e.grid(row=3, column=3, padx=5, pady=20)
#-------------------------------------------------------

#-------------------------------------------------------
# Escala 2
lbl_escalas2 = ttk.Label(frame, text="Escala (Canal 2)")
lbl_escalas2.grid(row=4, column=2, padx=5, pady=20)

escalas2 = ["10 mV", "100 mV", "1 V", "2.5 V", "5 V", "10 V"]
combo_escalas2 = ttk.Combobox(frame, values=escalas)
combo_escalas2.grid(row=4, column=3, padx=5, pady=20)
combo_escalas2.set("Seleccionar")
#-------------------------------------------------------




# Arrancar la aplicación
root.mainloop()
