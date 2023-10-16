################
### LIBRERIAS ###
################
#-------------------------------------------------------
import tkinter as tk
from tkinter import ttk
#from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import serial
import time
#from matplotlib.animation import FuncAnimation
#-------------------------------------------------------




############################
### COMUNICACIÓN SERIAL ###
############################
#-------------------------------------------------------
# Configura el puerto serial de Arduino
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
                try:
                        arduino.flushInput()    #Limpiar algún residuo que haya
                        for i in range(max_muestras):   
                            dato = float(arduino.readline().decode().strip())   #Con 'decode' lo hago string y con 'strip' le quito el '\r'
                            datos_canal1.append(dato*5/255)     #Decodificar el dato
                        return
                except:
                        print("E1")

        if canalP == 2:         #Adquisión de datos solo para el canal 2
                try:
                        arduino.flushInput()    #Limpiar algún residuo que haya
                        for i in range(max_muestras):
                            dato = float(arduino.readline().decode().strip())
                            datos_canal2.append(dato*5/255)
                        return
                except:
                        print("E2")
#-------------------------------------------------------


#-------------------------------------------------------
# Función para actualizar la gráfica en tiempo real
def graficar_datos():
    global contador, datos_canal1, datos_canal2

    # Borrar gráfica previa
    ax.clear()
    
    # Verificar si se debe graficar el Canal 1
    if ech1:
        adquirir_datos(1)       #Obtener Datos para el Canal 1
        if len(datos_canal1) > max_muestras:            # Gráfica fija en el tiempo
            datos_canal1 = datos_canal1[-max_muestras:]
        ax.plot(datos_canal1, label="Canal 1", linestyle='-', color='b')    #Graficar los datos del canal 1
        ax.legend()


    # Verificar si se debe graficar el Canal 2
    if ech2:
        adquirir_datos(2)       #Obtener Datos para el Canal 2
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
    #ax.set_ylim(0, 5)  # Establecer límites en el eje Y de 0 a 5
    
    # Actualización del canvas
    canvas.draw()

    # Intervalo de graficación
    root.after(100, graficar_datos)

#-------------------------------------------------------

#-------------------------------------------------------
# Función para obtener los datos de la sesión
def almacenar_datos():
        #---> Datos
        autor = autor_e.get()
        fecha = fecha_e.get()
        mag_fis = combo_magnitud.get()      #Magnitud física ch1
        escala = combo_escalas.get()                #Escala ch1
        mag_fis2 = combo_magnitud2.get()
        escala2 = combo_escalas2.get()
        ech1 = activar_canal1.get()     #Canal 1 activado?
        ech2 = activar_canal1.get()
        print(autor, fecha, mag_fis, escala)
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
max_muestras = 50
datos_muestras = []
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

magnitudes = ["Magnitud 1", "Magnitud 2", "Magnitud 3", "Magnitud 4", "Magnitud 5", "Magnitud 6"]
combo_magnitud = ttk.Combobox(frame, values=magnitudes)
combo_magnitud.grid(row=3, column=1, padx=5, pady=20)
combo_magnitud.set("Seleccionar")
#-------------------------------------------------------

#-------------------------------------------------------
# Botón para seleccionar parámetros (valores específicos se pueden agregar después)
lbl_escalas = ttk.Label(frame, text="Escala (Canal 1)")
lbl_escalas.grid(row=4, column=0, padx=5, pady=20)

escalas = ["10 mV", "100 mV", "1 V", "2.5 V", "5 V", "10 V"]
combo_escalas = ttk.Combobox(frame, values=escalas)
combo_escalas.grid(row=4, column=1, padx=5, pady=20)
combo_escalas.set("Seleccionar")
#-------------------------------------------------------

#-------------------------------------------------------
# Botón para seleccionar la magnitud física
lbl_magnitud2 = ttk.Label(frame, text="Magnitud Física (Canal 2)")
lbl_magnitud2.grid(row=3, column=2, padx=5, pady=20)

magnitudes2 = ["Magnitud 1", "Magnitud 2", "Magnitud 3", "Magnitud 4", "Magnitud 5", "Magnitud 6"]
combo_magnitud2 = ttk.Combobox(frame, values=magnitudes)
combo_magnitud2.grid(row=3, column=3, padx=5, pady=20)
combo_magnitud2.set("Seleccionar")
#-------------------------------------------------------

#-------------------------------------------------------
# Botón para seleccionar parámetros (valores específicos se pueden agregar después)
lbl_escalas2 = ttk.Label(frame, text="Escala (Canal 2)")
lbl_escalas2.grid(row=4, column=2, padx=5, pady=20)

escalas2 = ["10 mV", "100 mV", "1 V", "2.5 V", "5 V", "10 V"]
combo_escalas2 = ttk.Combobox(frame, values=escalas)
combo_escalas2.grid(row=4, column=3, padx=5, pady=20)
combo_escalas2.set("Seleccionar")
#-------------------------------------------------------



# Arrancar la aplicación
root.mainloop()
