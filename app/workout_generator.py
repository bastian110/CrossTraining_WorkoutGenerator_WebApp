import random
import numpy as np

def processWorkoutData(equipment, skills, duration):
    # Your processing logic here
    result = {'equipment': equipment, 'skills':skills, "duration": duration}
    print(result)
    return result

def chooseExercice(dataframe, muscles_list, equipment_list, difficulty , list_exercice_already_choose):
    list_exo = []
    random.shuffle(muscles_list)
    for muscle in muscles_list:
        
        exercices = list(dataframe.loc[(dataframe['Equipment'].isin(equipment_list)) 
                                                       & (dataframe['Difficulty'] <= difficulty) & (dataframe['Muscles Worked'] == muscle)]['Name'])
        


        # Continue choosing a random exercise until it's not already in list_exo
        while exercices:
            chosen_exercise = random.choice(exercices)
            if chosen_exercise not in list_exercice_already_choose:
                break
            exercices.remove(chosen_exercise)

        # If an exercise is found, add it to the list
        if exercices:
            list_exo.append(chosen_exercise)
    random.shuffle(list_exo)
    
    return list_exo

def weightExerciceGestion(dataframe, exercices_list, user):
    list_exercice_with_weight = []
    equiment_list = []
    for exercice in exercices_list:
        equipment = dataframe.loc[(dataframe['Name'] == exercice)]['Equipment']
        equiment_list.append(equipment)
        print(equipment)
        #if user.performance[exercice] != "" :
        #    list_exercice_with_weight.append((exercice, user.performance[exercice]))
        #elif user.level == 'beginner':
            
        #elif user.level == 'intermediate':
        #elif user.level == 'beginner':
    return list_exercice_with_weight

def wodComposition(dataframe, num_exercices_per_composant, choosing_exercice):
    type_wod=['EMOM', 'AMRAP', 'FOR TIME', 'TABATA']
    workout_compo = {}
    duration = 0
    try:
        exercices_list = random.sample(choosing_exercice, num_exercices_per_composant + int(random.uniform(-1,1)))
    except ValueError:
        exercices_list =  random.sample(choosing_exercice, num_exercices_per_composant-1)
    #list_exercice_with_weight = weightExerciceGestion(exercices_list, user)

    wod_type = random.choice(type_wod)
    if wod_type =='EMOM':
        duration = random.choice(np.arange(6, 16, num_exercices_per_composant))
        pause = 0
    elif wod_type=='AMRAP':
        duration = random.choice(np.arange(3, 14, num_exercices_per_composant))
        pause = 0
    elif wod_type=='FOR TIME':
        duration = "Timed performance"
        pause = 0
        print('no duration limit')
    elif wod_type=='TABATA':
        duration = random.choice(np.arange(6, 16, num_exercices_per_composant))
        pause = random.choice(np.arange(10, 25, 5))


    workout_compo["wod_type"] =wod_type 
    workout_compo['exercices_list'] = exercices_list 
    workout_compo['duration'] = (duration, pause)
    return workout_compo

def generateCompleteWod(dataframe, number_composant, muscles_list, equipment_list, difficulty):
        #duration =1, 2 ou 3 number of 'emom', 'amrap', 'fortime' or 'tabata'
        
        workout=[]
        list_exercice_already_choose = []
        for i in range(number_composant):
            num_exercises = round(random.uniform(-1,1))
            number_composant = number_composant + num_exercises
            print("####Number comp= ", number_composant) 
            if number_composant == 0:
                number_composant += 1
            choosing_exercice = chooseExercice(dataframe, muscles_list, equipment_list, difficulty, list_exercice_already_choose)
            each_workout = wodComposition(dataframe, number_composant,choosing_exercice)
            workout.append(each_workout)
            list_exercice_already_choose.extend( item for item in each_workout['exercices_list'])
        list_exercice_already_chooseToDict = {item: dataframe.loc[dataframe['Name'] == item, 'short_description'].iloc[0] for item in set(list_exercice_already_choose)}

        #print(list_exercice_already_chooseToDict)
        return(workout, list_exercice_already_chooseToDict)






    