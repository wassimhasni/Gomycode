import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

# Afficher les trois premières lignes
print(df.head(3))

# Supprimez les lignes avec des valeurs Nan
df = df.dropna()

# Extraction name et score
new_data = df[['name', 'score']]
print(new_data)

# ajouter un row
new_row = pd.DataFrame({'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}, index=['k'])
df = pd.concat([df, new_row])

# supprimer la colonne tentative
df = df.drop('attempts', axis=1)

# Export the DataFrame to a CSV file
df.to_csv('my_data.csv', index_label='index')

# Print the final DataFrame
print(df)

