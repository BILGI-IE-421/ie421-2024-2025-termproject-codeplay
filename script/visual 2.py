import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


years = [1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024]
russia_medals = [125, 195, 0, 132, 112, 63, 89, 90, 60, 65, 56, 71, 0]
germany_medals = [129, 126, 59, 102, 82, 65, 56, 49, 41, 44, 42, 37, 33]
usa_medals = [94, 0, 174, 94, 108, 101, 93, 101, 112, 104, 121, 113, 126]


data = {
    'Years': years,
    'Russia': russia_medals,
    'Germany': germany_medals,
    'USA': usa_medals
}
df = pd.DataFrame(data)


df_melted = df.melt(id_vars='Years', var_name='Country', value_name='Medals')


plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x='Years', y='Medals', hue='Country', marker='o')


plt.title('Medal Counts by Year (1976-2024)')
plt.xlabel('Years')
plt.ylabel('Number of Medals')
plt.xticks(years) 
plt.grid(True)  


plt.show()