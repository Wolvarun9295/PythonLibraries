import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.swarmplot(x='total_bill', y='day', data=tips)
plt.show()
