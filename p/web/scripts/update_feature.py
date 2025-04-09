import csv
import os

def update_feature_file(feature_file, scenario_name, csv_file):
    # Leer el CSV y guardar los datos en una lista de diccionarios
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # Leer el archivo .feature
    with open(feature_file, 'r') as file:
        lines = file.readlines()

    # Encontrar el escenario y la tabla de ejemplos correspondiente
    new_lines = []
    inside_scenario = False
    inside_examples = False
    scenario_found = False
    
    for line in lines:
        if scenario_name in line:
            inside_scenario = True
            scenario_found = True
            new_lines.append(line)
        elif inside_scenario and line.strip().startswith('Ejemplos:'):
            inside_examples = True
            new_lines.append(line)
            # Añadir la nueva tabla de ejemplos
            header = " | ".join(data[0].keys())
            new_lines.append(f"      | {header} |\n")
            for row in data:
                values = " | ".join(row.values())
                new_lines.append(f"      | {values} |\n")
        elif inside_examples and line.strip().startswith('|'):
            # Ignorar las líneas de la tabla de ejemplos existente
            continue
        else:
            if inside_examples:
                inside_examples = False
                inside_scenario = False
            new_lines.append(line)

    if not scenario_found:
        raise ValueError(
            f"Scenario '{scenario_name}' not found in '{feature_file}'")

    # Escribir los cambios en el archivo .feature
    with open(feature_file, 'w') as file:
        file.writelines(new_lines)


files = [
    {
        'path_feature': 'features/dependientes.feature',
        'scenario_outline': 'Esquema del escenario: Agregar dependientes',
        'data': 'data/dependinetes.csv'
    }
]

for file in files:
    update_feature_file(file['path_feature'], file['scenario_outline'], file['data'])
