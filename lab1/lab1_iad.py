import pandas as pd
import matplotlib.pyplot as plt
import graphics

plt.style.use('ggplot')  # Красиві графіки
plt.rcParams['figure.figsize'] = (15, 5)  # Розмір картинок

def read_file(file):
    df = pd.read_csv(file, sep=';', encoding='utf8', decimal=',')
    return df

def parse_df(dataframe):
    df['day/month'] = pd.to_datetime(df['day/month'], format='%d.%b').dt.strftime('%d.%m.2019')
    df['Time'] = pd.to_datetime(df['Time']).dt.strftime(r'%H:%M')
    df['Humidity'] = df['Humidity'].str.rstrip('%').astype(float) / 100.0
    df["Wind Speed"] = df["Wind Speed"].str.extract('(\d+)', expand=False).astype(int)
    df["Wind Gust"] = df["Wind Gust"].str.extract('(\d+)', expand=False).astype(int)
    return dataframe

file = "DATABASE.csv"
df = read_file(file)
parse_df(df)
df.set_index('day/month', inplace=True)
print(df)
print(df.dtypes)


k = int(input('How many graphics?\n'))
print('\nWhich column?') 
columns=[]
for j in range(k):
    column=input() 
    columns.append(column)
    
graphics.show(df, columns)
