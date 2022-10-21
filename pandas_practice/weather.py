import pandas as pd

df = pd.read_csv('weather.csv')

df_head = df.head(3)
df_tail = df.tail(10)

df = df[
    ['年月日',
    '平均気温(℃)',
    '最高気温(℃)',
    '最低気温(℃)',
    '降水量の合計(mm)',
    '最深積雪(cm)',
    '平均雲量(10分比)',
    '平均蒸気圧(hPa)',
    '平均風速(m/s)',
    '日照時間(時間)'
    ]
]

# df = df.drop(['削除するカラム'], axis = 1)

df = df[1:]

df_type = df.dtypes
df_shape = df.shape
name_columns = df.columns
name_index = df.index

df.iloc[4:10, 2:6]
df.loc[5:10, '最高気温(℃)':'最深積雪(cm)']

df.columns = [
    '年月日',
    '平均気温',
    '最高気温',
    '最低気温',
    '降水量の合計',
    '最深積雪',
    '平均雲量',
    '平均蒸気圧',
    '平均風速',
    '日照時間'
]

# df = df.rename(columns = {
#     '平均気温':'平均気温(変更)'
# })

df.sort_values('最高気温', ascending = False)

df.isnull()

df.fillna(0)

df.dropna(axis = 1)

# df = df.drop('年月日', axis = 1)

# df.mean(axis = 0)
# df.median()
# df.std()
# df.max()
# df.min()
# df.describe()

import matplotlib.pyplot as plt

df[:50].plot(x = '年月日', y = ['平均気温', '最高気温', '最低気温'], legend = False)
plt.show()