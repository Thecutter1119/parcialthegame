import tkinter as tk
from tkinter import messagebox
import random

class Game():

    def iniciar_juego(self):
        try:
            self.rango_maximo = int(self.rango_entry.get())
            if self.rango_maximo <= 0:
                raise ValueError("El rango debe ser mayor que 0.")
            
            #dividir entre 20
            self.intentos_maximos = self.rango_maximo // 20
            self.numero_adivinar = random.randint(1, self.rango_maximo)
            self.intentos = 0
            
            self.rango_entry.config(state="disabled")
            self.btniniciar.config(state="disabled")
            
            # intentos
            self.lblintentos.config(text=f"Tienes {self.intentos_maximos} intentos para adivinar el número.")
            
            self.intento_entry.config(state="normal")
            self.btnintentar.config(state="normal")
        
        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}")

    def probar_intento(self):
        try:
            intento_usuario = int(self.intento_entry.get())
            
            if intento_usuario < 1 or intento_usuario > self.rango_maximo:
                messagebox.showwarning("Advertencia", f"Por favor, ingresa un número entre 1 y {self.rango_maximo}.")
                return
            #sumar intento fallido
            self.intentos += 1
            
            if intento_usuario == self.numero_adivinar:
                messagebox.showinfo("felicidades", f"has acertado el número!!!!! {self.numero_adivinar}!\nLo lograste en {self.intentos} intentos.")
                self.finalizar_juego()
            elif intento_usuario < self.numero_adivinar:
                messagebox.showinfo("Intenta de nuevo", "El número a adivinar es mayor.")
            else:
                messagebox.showinfo("Intenta de nuevo", "El número a adivinar es menor.")
            
            #intentos que quedan
            if self.intentos >= self.intentos_maximos:
                messagebox.showinfo("fin del juego", f"agoto los intentos, el número correcto era {self.numero_adivinar}.")
                self.finalizar_juego()
            else:
                self.lblintentos.config(text=f"tiene {self.intentos_maximos - self.intentos} intentos restantes.")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número entero.")
    
    def finalizar_juego(self):
        self.intento_entry.config(state="disabled")
        self.btnintentar.config(state="disabled")
        
        self.rango_entry.config(state="normal")
        self.btniniciar.config(state="normal")
    
    def salir(self):
        respuesta = messagebox.askyesnocancel("Salir", "¿Estas Seguro que quieres salir y no quieres seguir jugando ☹️ ?")
        if respuesta is True:  
            self.ventana.destroy()
        elif respuesta is False:  
            pass 

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Juego de adivinar")
        self.ventana.config(width=800, height=600)
        self.ventana.config(bg="white")
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)


        self.numero_adivinar = 0
        self.intentos_maximos = 0
        self.intentos_realizados = 0
        self.rango_maximo = 0

        self.titulo = tk.Label(self.ventana, text="Juego de Adivinar el Número", font=("Arial", 15))
        self.titulo.place(x=20, y=10)

        self.mensaje = tk.Label(self.ventana, text="Introduce el rango máximo para adivinar el número:")
        self.mensaje.pack(pady=10)

        self.rango_entry = tk.Entry(self.ventana)
        self.rango_entry.pack(pady=10)
        
        self.btniniciar = tk.Button(self.ventana, text="Iniciar Juego", command=self.iniciar_juego)
        self.btniniciar.pack(pady=10)

        self.lblintento = tk.Label(self.ventana, text="Introduce un número para adivinar:")
        self.lblintento.pack(pady=5)

        self.intento_entry = tk.Entry(self.ventana)
        self.intento_entry.pack(pady=5)

        self.btnintentar = tk.Button(self.ventana, text="Intentar", command=self.probar_intento)
        self.btnintentar.pack(pady=10)

        self.lblintentos = tk.Label(self.ventana, text="")
        self.lblintentos.pack(pady=10)
        
        self.ventana.mainloop()
