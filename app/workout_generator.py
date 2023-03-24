import random
import numpy as np

def processWorkoutData(equipment, skills, duration):
    # Your processing logic here
    result = {'equipment': equipment, 'skills':skills, "duration": duration}
    print(result)
    return result






def chooseExercice(dataframe, muscles_list, equipment_list, difficulty):
    list_exo = []
    random.shuffle(muscles_list)
    for muscle in muscles_list:

        exercice = list(dataframe.loc[(dataframe['Equipment'].isin(equipment_list)) 
                                                       & (dataframe['Difficulty'] <= difficulty) & (dataframe['Muscles Worked'] == muscle)]['Name'])
        #print(exercice)
        if not exercice == []:
            exercice_by_muscle = random.choice(exercice)
            list_exo.append(exercice_by_muscle)
        #else: print('no exercice for ',muscle, 'with this equipment and difficulty')
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
    type_wod=['emom', 'amrap', 'fortime', 'tabata']
    workout_compo = {}
    duration = 0
    exercices_list = random.sample(choosing_exercice, num_exercices_per_composant + int(random.uniform(-1,1)))
    #list_exercice_with_weight = weightExerciceGestion(exercices_list, user)

    wod_type = random.choice(type_wod)
    if wod_type =='emom':
        duration = random.choice(np.arange(6, 16, num_exercices_per_composant))
    elif wod_type=='amrap':
        duration = random.choice(np.arange(3, 14, num_exercices_per_composant))
    elif wod_type=='fortime':
        duration = random.uniform(0,100)
        print('no duration limit')
    elif wod_type=='tabata':
        duration = random.choice(np.arange(6, 16, num_exercices_per_composant))
        pause = random.choice(np.arange(10, 25, 5))
        duration = (duration, pause)

    workout_compo[wod_type] = [exercices_list, duration]
    return workout_compo

def generateCompleteWod(dataframe, number_composant, muscles_list, equipment_list, difficulty):
        #duration =1, 2 ou 3 number of 'emom', 'amrap', 'fortime' or 'tabata'
        
        workout=[]
        for i in range(number_composant):
            num_exercises = random.randint(1,number_composant)
            choosing_exercice = chooseExercice(dataframe, muscles_list, equipment_list, difficulty)
            workout.append(wodComposition(dataframe, number_composant,choosing_exercice))
        return(workout)



