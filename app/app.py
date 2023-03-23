from flask import Flask, render_template, request
import pandas as pd
import csv

from workout_generator import process_workout_data

app = Flask(__name__)

@app.route('/')
def overview():
    return render_template('overview.html')

@app.route('/workout')
def workout():
    equipment_list = read_equipment_from_csv('/Users/bastianchuttarsing/Documents/Crosstraining_WebApp/data-science/dataset/dataset_exercices_crosstraining.csv')
    return render_template('workout.html', equipment_list=equipment_list)

@app.route('/workout/summary')
def workout_summary():
    return render_template('workout_summary.html')

def read_equipment_from_csv(file_path):
    equipment_list = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            equipment = row['Equipment']
            if equipment not in equipment_list:
                equipment_list.append(equipment)
    return equipment_list

@app.route('/process_workout', methods=['POST'])
def process_workout():
    checked_equipment = request.form.getlist('equipment')
    checked_skills = request.form.getlist('skills')
    checked_duration = request.form.getlist('duration')
    
    result = process_workout_data(checked_equipment, checked_skills, checked_duration)
    return render_template('workout_summary.html', workout_summary=result)

if __name__ == '__main__':
    app.run(debug=True)
