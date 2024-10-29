import requests

class GetRecord:
    __url = "https://671be4192c842d92c381a4d4.mockapi.io/test"

    # Función para obtener el último registro desde la API
    def get_last_record(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            data = response.json()

            # Obtiene el último registro
            if data:
                return data[-1]  # Devuelve el último registro
            else:
                return None  # Si no hay registros
        except Exception as e:
            print(f"Error: {e}")  # Manejo de errores
            return None  # Devuelve None en caso de error

    # Función para obtener un registro por ID
    def get_record_by_id(self, registro_id):
        try:
            response = requests.get(f"{self.__url}/{registro_id}")
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            return response.json()  # Devuelve el registro encontrado
        except Exception as e:
            print(f"Error: {e}")  # Manejo de errores
            return None  # Devuelve None en caso de error

    # Función para obtener todos los registros
    def get_all_records(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            return response.json()  # Devuelve todos los registros
        except Exception as e:
            print(f"Error: {e}")  # Manejo de errores
            return None  # Devuelve None en caso de error

    # Función para obtener un registro aleatorio
    def get_random_record(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            data = response.json()

            if data:
                import random
                return random.choice(data)  # Devuelve un registro aleatorio
            else:
                return None  # Si no hay registros
        except Exception as e:
            print(f"Error: {e}")  # Manejo de errores
            return None  # Devuelve None en caso de error
