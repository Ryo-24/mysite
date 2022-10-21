import pandas as pd

df_people = pd.read_csv('people.csv')

# df_people = df_people[df_people['nationality'] == 'America']
# df_people = df_people.query("nationality == 'America'")
# df_people = df_people[df_people['nationality'].isin(['America'])]

df_people[(df_people['age'] >= 20) & (df_people['age'] < 30)]
df_people.query('age >= 20 & age < 30')\

df_people['nationality'].unique()

df_people.drop_duplicates(subset = 'nationality')

pd.get_dummies(df_people['nationality'])

# df_people = pd.get_dummies(df_people, columns = ['nationality'])




