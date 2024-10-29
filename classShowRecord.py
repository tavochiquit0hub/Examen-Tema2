import tkinter as tk
from tkinter import ttk  # Importa ttk para Treeview
from classGetRecord import GetRecord

class ShowRecord:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro de Usuarios")
        self.ventana.geometry("800x400")  # Ajuste de tamaño

        # Crear un frame para el Treeview y el Scrollbar
        frame = tk.Frame(self.ventana)
        frame.pack(pady=20, fill="both", expand=True)

        # Crear tabla Treeview
        self.tree = ttk.Treeview(frame, columns=("Web", "Email", "Password", "Name", "UserName", "ID"), show="headings")

        # Configuración de encabezados y tamaños de columnas
        self.tree.heading("Web", text="Web")
        self.tree.column("Web", width=100)

        self.tree.heading("Email", text="Email")
        self.tree.column("Email", width=150)

        self.tree.heading("Password", text="Password")
        self.tree.column("Password", width=100)

        self.tree.heading("Name", text="Name")
        self.tree.column("Name", width=100)

        self.tree.heading("UserName", text="UserName")
        self.tree.column("UserName", width=100)

        self.tree.heading("ID", text="ID")
        self.tree.column("ID", width=50)

        # Crear un Frame para el Treeview y el Scrollbar
        self.scrollbar_frame = tk.Frame(frame)
        self.scrollbar_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear Scrollbar
        self.scrollbar = ttk.Scrollbar(self.scrollbar_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Empaquetar el Treeview y el Scrollbar
        self.tree.pack(side=tk.LEFT, fill="both", expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")

        # Entrada para ID del registro
        self.entry_id = tk.Entry(self.ventana, width=20)
        self.entry_id.pack(pady=5)

        # Botón para cargar un registro específico
        self.boton_cargar_id = tk.Button(self.ventana, text="Cargar Registro por ID", command=self.load_record_by_id)
        self.boton_cargar_id.pack(pady=5)

        # Botón para cargar un registro aleatorio
        self.boton_cargar_aleatorio = tk.Button(self.ventana, text="Cargar Registro Aleatorio", command=self.load_random_record)
        self.boton_cargar_aleatorio.pack(pady=5)

        # Botón para cargar todos los registros
        self.boton_cargar_todos = tk.Button(self.ventana, text="Cargar Todos los Registros", command=self.load_all_records)
        self.boton_cargar_todos.pack(pady=5)

        self.get_record = GetRecord()  # Crear una instancia de GetRecord

    # Método para cargar un registro por ID
    def load_record_by_id(self):
        registro_id = self.entry_id.get()
        self.tree.delete(*self.tree.get_children())
        registro = self.get_record.get_record_by_id(registro_id)  # Obtener registro por ID
        if registro:
            self.tree.insert("", "end", values=(
                registro['Name'],
                registro['Email'],
                registro['Password'],
                registro['Name'],
                registro['UserName'],
                registro['ID']
            ))
        else:
            print("No se encontró el registro o hubo un error.")

    # Método para cargar un registro aleatorio
    def load_random_record(self):
        self.tree.delete(*self.tree.get_children())
        registro = self.get_record.get_random_record()
        if registro:
            self.tree.insert("", "end", values=(
                registro['Name'],
                registro['Email'],
                registro['Password'],
                registro['Name'],
                registro['UserName'],
                registro['ID']
            ))
        else:
            print("No se encontraron registros o hubo un error.")

    # Método para cargar todos los registros
    def load_all_records(self):
        self.tree.delete(*self.tree.get_children())
        registros = self.get_record.get_all_records()
        if registros:
            for registro in registros:
                self.tree.insert("", "end", values=(
                    registro['Name'],
                    registro['Email'],
                    registro['Password'],
                    registro['Name'],
                    registro['UserName'],
                    registro['ID']
                ))
        else:
            print("No se encontraron registros o hubo un error.")
