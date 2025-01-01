import pandas as pd
import plotly.express as px


data = {
    'Country': ['United States(ABD)', 'Combined Russia', 'Combined Germany'],
    'Gold': [332, 64, 242],
    'Silver': [252, 60, 273],
    'Bronze': [218, 69, 290]
}


df = pd.DataFrame(data)


df['Total Medals'] = df[['Gold', 'Silver', 'Bronze']].sum(axis=1)


color_map = {
    'United States(ABD)': '#1f77b4',
    'Combined Russia': '#ff7f0e',
    'Combined Germany': '#2ca02c'
}


fig = px.pie(df, 
             values='Total Medals', 
             names='Country', 
             title='Total Medals by Country in Athletics',
             color='Country',
             color_discrete_map=color_map,  
             hole=0.3)


fig.show()
