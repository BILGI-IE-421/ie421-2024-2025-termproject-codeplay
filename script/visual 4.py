import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import ipywidgets as widgets
from IPython.display import display

# Write the full path to your file (e.g., C:\Users\Username\Documents\Total Medals 1976-2024.csv)
file_path = r'C:\Users/ataka/Downloads/Data\Total Medals 1976-2024.csv'

# Load the data
data = pd.read_csv(file_path, delimiter=';', skiprows=1)

# Adjust column names
columns = ['Country', 'Placeholder', 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024]
data.columns = columns
data = data.drop(columns=['Placeholder']).dropna()

# Transform the data to long format
long_data = pd.melt(data, id_vars=['Country'], var_name='Year', value_name='Medals')
long_data['Medals'] = pd.to_numeric(long_data['Medals'], errors='coerce')
long_data = long_data.dropna()

# Available countries and colors
available_countries = long_data['Country'].unique()
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']

# Country selection widget
country_selector = widgets.SelectMultiple(
    options=available_countries,
    value=['Russia:', 'Germany:', 'USA:'],
    description='Countries',
    disabled=False
)

# Color selection widget
color_selector = widgets.SelectMultiple(
    options=colors,
    value=['red', 'blue', 'green'],
    description='Colors',
    disabled=False
)

# Function to create the plot
def plot_medal_predictions(countries, selected_colors):
    plt.figure(figsize=(12, 6))
    
    for country, color in zip(countries, selected_colors):
        country_data = long_data[long_data['Country'] == country]
        X = country_data['Year'].values.reshape(-1, 1)
        y = country_data['Medals'].values

        # Train the model
        model = LinearRegression()
        model.fit(X, y)

        # Make predictions
        years = np.arange(1976, 2030, 1).reshape(-1, 1)
        predictions = model.predict(years)

        # Plotting
        plt.scatter(X, y, color=color, label=f"{country} (Actual Data)")
        plt.plot(years, predictions, color=color, linestyle='--', label=f"{country} (Prediction)")

    # Graph settings
    plt.title("Medal Predictions for Selected Countries (1976-2030)")
    plt.xlabel("Years")
    plt.ylabel("Total Medal Count")
    plt.legend()
    plt.grid(True)
    plt.show()

# Create interactive plot
widgets.interactive(plot_medal_predictions, countries=country_selector, selected_colors=color_selector)