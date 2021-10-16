import numpy as np
import pandas as pd
import shlex

with open('titanic_with_labels.csv', encoding='utf-8') as data:
    df = data.read()
df = df.replace('  ', ' NaN ')
df = shlex.split(df, posix=True)
df = np.array(df[7:]).reshape((10000, 8))
df = pd.DataFrame(df, columns=['none', 'sex', 'row_number', 'liters_drunk', 'age', 'drink', 'check_number', 'label'])
df['row_number'] = df['row_number'].astype('float')
df['liters_drunk'] = df['liters_drunk'].astype('int')
df['age'] = df['age'].astype('int')
df['check_number'] = df['check_number'].astype('int')
df['label'] = df['label'].astype('int')
df = df.drop(['none'], axis=1)

df['row_number'] = df['row_number'].replace(np.nan, -1)
df['row_number'] = df['row_number'].replace(-1, df['row_number'].aggregate(max))

sq_median_lit = df.sort_values('liters_drunk')['liters_drunk'].median() ** 2
avg_liters = int(df['liters_drunk'][(df['liters_drunk'] >= 0) & (df['liters_drunk'] <= int(sq_median_lit + 1))].mean())
df['liters_drunk'] = df['liters_drunk'].apply(lambda x: x if 0 <= x <= sq_median_lit else avg_liters)

df = df.drop(df[(df['sex'] == '-') | (df['sex'] == '"Не указан"')].index)
df['sex'] = df['sex'].apply(lambda x: 0 if x == 'ж' or x == 'Ж' else 1)

df['drink'] = df['drink'].apply(lambda x: 0 if x == 'Cola' or x == 'Fanta' or x == 'Water' else 1)

age_old = df['age'].apply(lambda x: 1 if x > 50 else 0)
age_adult = df['age'].apply(lambda x: 1 if 18 <= x <= 50 else 0)
age_kid = df['age'].apply(lambda x: 1 if x < 18 else 0)
df.insert(4, 'age_old', age_old)
df.insert(4, 'age_adult', age_adult)
df.insert(4, 'age_kid', age_kid)
df = df.drop(['age'], axis=1)
######################################
with open('cinema_sessions.csv') as data:
    cinema_sessions = data.read()
cinema_sessions = cinema_sessions.split()
cinema_sessions = np.array(cinema_sessions[2:]).reshape((10000, 3))
df2 = pd.DataFrame(cinema_sessions, columns=['none', 'check_number', 'session_start'])
df2 = df2.drop(['none'], axis=1)
df2['check_number'] = df2['check_number'].astype('int')
df2['session_start'] = df2['session_start'].apply(lambda x: x[:2])
df2['session_start'] = df2['session_start'].astype('int')

df2['morning'] = df2['session_start'].apply(lambda x: 1 if 6 <= x < 12 else 0)
df2['day'] = df2['session_start'].apply(lambda x: 1 if 12 <= x < 18 else 0)
df2['evening'] = df2['session_start'].apply(lambda x: 1 if 18 <= x <= 23 else 0)
df = df.set_index('check_number').sort_index()
df2 = df2.set_index('check_number').sort_index().drop(['session_start'], axis=1)

df3 = pd.concat([df, df2], axis=1).dropna()
df3 = df3.astype('int')
df3.to_csv('titanic_final.csv')
