import pandas as pd
import plotly.graph_objects as go
from random import randint
import plotly.express as px

df = pd.read_csv('result.csv')

df['Age'] = df['Age'].replace('110+', float('nan'))

df = df.dropna(subset=['Age'])

df = df[df['Year'].between(1921, 2022)]

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

df = df.sort_values(['Year', 'Age'])

# df['Age'] = pd.cut(pd.to_numeric(df['Age']), bins=range(0, 120, 5)).astype(str)
# df['Age'] = df['Age'] // 5 * 5

# df['Year'] = df['Year'] // 5 * 5

df = df.dropna()

df['Female'] = df['Female'].astype('float')
df['Male'] = df['Male'].astype('float')

df = df.groupby(['country', 'Age', 'Year']).agg({'Female': 'mean', 'Male': 'mean'})

df = df.dropna()

df = df.reset_index()

df_man = df

df_man = df_man.drop(columns='Female', axis=1)

df_man['country'] = df_man['country'] + "_Male"

df_man.rename(columns={'Male': 'Death'}, inplace=True)

df_woman = df

df_woman = df_woman.drop(columns='Male', axis=1)

df_woman['country'] = df_woman['country'] + "_Female"

df_woman.rename(columns={'Female': 'Death'}, inplace=True)

# df['sum'] = df['Male'] + df['Female']

# top_10 = df.nlargest(10, 'sum')
# bottom_10 = df.nsmallest(10, 'sum')

# print(top_10)
# print(bottom_10)
# ITA have the largest total number of death (6/10) while AUS has the smallest.

# print(df['country'].unique())

df_new = df_man.append(df_woman)

print(df_man)
print(df_woman)

df_top = df_new[(df_new['country'] == 'AUS_Male') | (df_new['country'] == 'ITA_Male') | (df_new['country'] == 'ESP_Male') |
            (df_new['country'] == 'FRATNP_Male') | (df_new['country'] == 'AUS_Female') | (df_new['country'] == 'ITA_Female') |
            (df_new['country'] == 'ESP_Female') | (df_new['country'] == 'FRATNP_Female')]
print(df_top)
#
fig = px.scatter(df_top, x='Age', y='Death', color='country',
                 animation_frame='Year', range_x=[0, 100], range_y=[0, 20000],
                 color_discrete_map={'AUS_Male': '#cc0000', 'AUS_Female': '#ff3333',
                                     'ITA_Male': '#00cc00', 'ITA_Female': '#33ff33',
                                     'ESP_Male': '#cccc00', 'ESP_Female': '#ffff33',
                                     'FRATNP_Male': '#0000cc', 'FRATNP_Female': '#3333ff'}
                 )


fig.show()
