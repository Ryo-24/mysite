import pandas as pd

df_iris = pd.read_csv('iris.csv')

# print(df_iris)

df_iris['Class'].unique()

df_iris['Class'].value_counts()

df_iris.groupby('Class').mean()
df_iris.groupby('Class').std()

