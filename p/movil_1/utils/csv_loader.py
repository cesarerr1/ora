import csv

def load_csv(file_path):
    """Carga los datos desde un archivo CSV y los devuelve como una lista de diccionarios."""
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            # Verificar que los datos fueron cargados correctamente
            print(f"Datos cargados desde el CSV: {data}")
            if not data:
                raise ValueError(f"El archivo CSV '{file_path}' está vacío o no tiene datos.")
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo CSV no encontrado: {file_path}")
