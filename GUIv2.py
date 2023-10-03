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
#-------------------------------------------------------




#################################
### FUNCIONES DE LOS BOTONES ###
#################################
#-------------------------------------------------------
# Función para simular la adquisición de datos
def adquirir_datos():
    # adquisición de datos, reemplaza esto con tu lógica real
    dato = random.uniform(0, 5)  # Simula un dato en un rango de 0 a 5 V
    return dato
#-------------------------------------------------------

#-------------------------------------------------------
# Función para actualizar la gráfica en tiempo real
def graficar_datos():
    global contador
    mag_fis = combo_magnitud.get()
    escala = combo_escalas.get()
    mag_fis2 = combo_magnitud2.get()
    escala2 = combo_escalas2.get()
    print(mag_fis, escala, mag_fis2, escala2)

    # Borramos cualquier gráfica previa
    ax.clear()
    
    # Verificamos si se debe graficar el Canal 1
    if activar_canal1.get():
        # Simulamos la adquisición de datos para Canal 1 (reemplaza con tu lógica real)
        datos_canal1.append(adquirir_datos())
        
        # Limitamos la longitud de los datos para mantener la gráfica fija en el tiempo
        if len(datos_canal1) > max_datos:
            datos_canal1.pop(0)
        
        # Graficamos los datos del Canal 1
        ax.plot(datos_canal1, label="Canal 1", marker='o', linestyle='-', color='b')

        # Configuramos la leyenda de la gráfica
        ax.legend()
    
    # Verificamos si se debe graficar el Canal 2
    if activar_canal2.get():
        # Simulamos la adquisición de datos para Canal 2 (reemplaza con tu lógica real)
        datos_canal2.append(adquirir_datos())
        
        # Limitamos la longitud de los datos para mantener la gráfica fija en el tiempo
        if len(datos_canal2) > max_datos:
            datos_canal2.pop(0)
        
        # Graficamos los datos del Canal 2
        ax.plot(datos_canal2, label="Canal 2", marker='o', linestyle='-', color='r')

        # Configuramos la leyenda de la gráfica
        ax.legend()

    if not(activar_canal2.get()) and not(activar_canal1.get()):
        print("C A")
        ax.clear()
        contador += 1
        if contador == 2:
            return
    
    # Configuramos etiquetas y título
    ax.set_xlabel('Muestras')
    ax.set_ylabel(mag_fis)
    
    # Actualizamos el canvas
    canvas.draw()

    root.after(100, graficar_datos)

#-------------------------------------------------------

#-------------------------------------------------------
# Función para actualizar la gráfica en tiempo real
def almacenar_datos():
    # Datos de la sesion
    autor = autor_e.get()
    fecha = fecha_e.get()
    mag_fis = combo_magnitud.get()
    escala = combo_escalas.get()
    mag_fis2 = combo_magnitud2.get()
    escala2 = combo_escalas2.get()
    print(autor, fecha, mag_fis, escala)
#-------------------------------------------------------




##########################################
### CONFI INICIAL Y VARIABLES AUXILIARES ###
##########################################
#-------------------------------------------------------
# Configuración inicial
datos_canal1 = []  # Almacenará los datos adquiridos
datos_canal2 = []
max_datos = 50  # Número máximo de puntos en la gráfica
autor = ""
fecha = ""
mag_fis = ""
escala = ""
mag_fis2 = ""
escala2 = ""
contador = 0
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
