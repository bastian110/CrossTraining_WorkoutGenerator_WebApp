import pandas as pd
import numpy as np

def map_words(row):
    word_to_int = {'beginner': 1, 'intermediate': 2, 'advanced': 3, 'pro': 4, 'challenging': 5}
    words = row.split()
    ints = [word_to_int[word] for word in words]
    return max(ints)

def loadPandasDataFromCsv(path):
    df = pd.read_csv(path)
    df = df.applymap(lambda x: x.lower() if type(x) == str else x)
    df = df.applymap(lambda x: x.strip() if type(x) == str else x)
    df['Muscles Worked'] = df['Muscles Worked'].str.replace('and|\\sand\\s',' ',regex=True)

    # Use Series.replace with regex=True
    df['Muscles Worked'] = df['Muscles Worked'].replace({r'quads(\s|$)': r'quadriceps\1',r'full-body(\s|$)': r'full_body\1',r'hamstrings(\s|$)': r'hamstring\1',
                    r'shoulders(\s|$)': r'shoulder\1',r'glutes(\s|$)': r'glute\1',r'hams(\s|$)': r'hamstring\1'}, regex=True)
    df['Difficulty'] = df['Difficulty'].replace({'beginner to intermediate': 'beginner intermediate',' beginner to intermediate': 'beginner intermediate',
                                                'intermediate to advanced': 'intermediate advanced','beginner to advanced':'beginner intermediate advanced',
                                                ' beginner to advanced':'beginner intermediate advanced' })


    df['Difficulty'] = df['Difficulty'].apply(map_words)

    return df

def getListUniqueElementInDfColomn(dataframe, colomn_name):
    list_unique_element = list(dataframe[colomn_name].unique())
    list_unique_element.sort()
    return list_unique_element



