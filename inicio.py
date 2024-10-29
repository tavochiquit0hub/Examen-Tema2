import tkinter as tk
from classShowRecord import ShowRecord  # Importa la clase ShowRecord

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.resizable(False, False)  # Evita que la ventana se redimensione
app = ShowRecord(ventana)
ventana.mainloop()