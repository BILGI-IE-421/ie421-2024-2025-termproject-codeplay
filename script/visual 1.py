import pandas as pd
import plotly.graph_objects as go

# Data for the top 20 countries
data = {
    "Country": [
        "United States",
        "Combined Russian total ",
        "Combined German total ",
        "Soviet Union*",
        "Great Britain",
        "France",
        "Germany***",
        "China",
        "Italy",
        "Australia**",
        "Hungary",
        "Sweden",
        "East Germany*",
        "Japan",
        "Russia",
        "Canada",
        "Netherlands",
        "Romania",
        "South Korea",
        "Poland"
    ],
    "Bronze": [780, 504, 498, 325, 344, 296, 290, 197, 228, 228, 182, 182, 178, 166, 127, 158, 134, 124, 110, 142],
    "Silver": [880, 514, 468, 357, 337, 279, 272, 226, 201, 193, 161, 180, 150, 137, 129, 116, 105, 108, 100, 93],
    "Gold": [1101, 609, 450, 440, 299, 238, 241, 302, 228, 185, 187, 152, 169, 168, 153, 80, 105, 98, 109, 73]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a stacked bar chart
fig = go.Figure()

# Add traces for each medal type without text on bars
fig.add_trace(go.Bar(
    x=df['Country'],
    y=df['Gold'],
    name='Gold',
    marker_color='gold',
    hoverinfo='text',
    hovertemplate='Gold: %{y}<extra></extra>'  # Toplam kısmı kaldırıldı
))

fig.add_trace(go.Bar(
    x=df['Country'],
    y=df['Silver'],
    name='Silver',
    marker_color='silver',
    hoverinfo='text',
    hovertemplate='Silver: %{y}<extra></extra>'  # Toplam kısmı kaldırıldı
))

fig.add_trace(go.Bar(
    x=df['Country'],
    y=df['Bronze'],
    name='Bronze',
    marker_color='#cd7f32',
    hoverinfo='text',
    hovertemplate='Bronze: %{y}<extra></extra>'  # Toplam kısmı kaldırıldı
))

# Update layout
fig.update_layout(
    title='Top 20 Countries by Medals in Summer Olympics (1896-2024)',
    xaxis_title='Country',
    yaxis_title='Number of Medals',
    barmode='stack',
    xaxis_tickangle=-45
)

# Show the figure
fig.show()