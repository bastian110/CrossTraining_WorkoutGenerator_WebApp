from flask import Flask, render_template, request
import pandas as pd


from workout_generator import processWorkoutData, generateCompleteWod
from load_pd_dataset import getListUniqueElementInDfColomn, loadPandasDataFromCsv, getDescriptionFromName

df = loadPandasDataFromCsv('/Users/bastianchuttarsing/Documents/Crosstraining_WebApp/data-science/dataset/dataset_exercices_crosstraining.csv')


app = Flask(__name__)

@app.route('/')
def overview():
    return render_template('overview.html')

@app.route('/workout')
def workout():
    equipment_list = getListUniqueElementInDfColomn(df,'Equipment')
    difficulty_list = getListUniqueElementInDfColomn(df,'Difficulty')
    return render_template('workout.html', equipment_list=equipment_list, difficulty_list=difficulty_list)

@app.route('/workoutsummary')
def workout_summary():
    exerciceDescription = getDescriptionFromName(df, )
    return render_template('workout_summary.html')


@app.route('/process_workout', methods=['POST'])
def process_workout():
    checked_equipment = request.form.getlist('equipment')
    checked_duration = int(request.form.get('duration'))
    checked_difficulty = int(request.form.get('difficulty'))
    
    workout, exercice_description_dict = generateCompleteWod(df, checked_duration , list(set(df['Muscles Worked'].str.split(' ').sum()))[1:] , checked_equipment, checked_difficulty)
    #print(workout)
    return render_template('workout_summary.html', workout_summary=workout, exercice_description_dict=exercice_description_dict)

if __name__ == '__main__':
    app.run(debug=True)
