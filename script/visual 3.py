import pandas as pd
import plotly.express as px

# Creating the data
data = {
    'Country': ['United States(ABD)', 'Combined Russia', 'Combined Germany'],
    'Gold': [332, 64, 242],
    'Silver': [252, 60, 273],
    'Bronze': [218, 69, 290]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Calculating the total medal count by country
df['Total Medals'] = df[['Gold', 'Silver', 'Bronze']].sum(axis=1)

# Defining colors for the pie chart
color_map = {
    'United States(ABD)': '#1f77b4',
    'Combined Russia': '#ff7f0e',
    'Combined Germany': '#2ca02c'
}

# Creating the pie chart
fig = px.pie(df, 
             values='Total Medals', 
             names='Country', 
             title='Total Medals by Country in Athletics',
             color='Country',
             color_discrete_map=color_map,  # Applying the custom color map
             hole=0.3)

# Displaying the chart
fig.show()
