import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.swarmplot(x='total_bill', y='size', data=tips)
plt.show()
