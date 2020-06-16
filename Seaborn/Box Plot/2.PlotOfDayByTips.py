import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
sns.boxplot(x='day', y='tip', data=df)
plt.show()
