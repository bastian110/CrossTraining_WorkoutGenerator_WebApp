import csv

def process_workout_data(equipment, skills, duration):
    # Your processing logic here
    result = "Processed data: equipment={}, skills={}, duration={}".format(equipment, skills, duration)
    return result


#generaliser cette fonction pour obtenir les infos d'une colonne du csv
def read_equipment_from_csv(file_path):
    equipment_list = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            equipment = row['Equipment']
            if equipment not in equipment_list:
                equipment_list.append(equipment)
    return equipment_list