import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/home/bridgelabz/Desktop/gapminder-FiveYearData.csv')
sns.boxplot(x='lifeExp', y='continent', data=df)
plt.show()
