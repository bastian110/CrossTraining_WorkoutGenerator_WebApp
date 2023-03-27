from flask import Flask, render_template, request
import pandas as pd


from workout_generator import processWorkoutData, generateCompleteWod
from load_pd_dataset import getListUniqueElementInDfColomn, loadPandasDataFromCsv

df = loadPandasDataFromCsv('/Users/bastianchuttarsing/Documents/Crosstraining_WebApp/data-science/dataset/dataset_exercices_crosstraining.csv')
difficulty = 5 # to be defined by the user's profile

app = Flask(__name__)

@app.route('/')
def overview():
    return render_template('overview.html')

@app.route('/workout')
def workout():
    equipment_list = getListUniqueElementInDfColomn(df,'Equipment')
    return render_template('workout.html', equipment_list=equipment_list)

@app.route('/workout/summary')
def workout_summary():
    return render_template('workout_summary.html')


@app.route('/process_workout', methods=['POST'])
def process_workout():
    checked_equipment = request.form.getlist('equipment')
    checked_skills = request.form.getlist('skills')
    checked_duration = int(request.form.get('duration'))
    print("checked_duration#############", checked_duration)
    
    result = processWorkoutData(checked_equipment, checked_skills, checked_duration)
    workout = generateCompleteWod(df, checked_duration , list(set(df['Muscles Worked'].str.split(' ').sum()))[1:] , checked_equipment, difficulty)
    print(workout)
    return render_template('workout_summary.html', workout_summary=workout)

if __name__ == '__main__':
    app.run(debug=True)
