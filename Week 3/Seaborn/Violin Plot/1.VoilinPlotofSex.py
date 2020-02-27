import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.violinplot(x='sex', y='total_bill', data=tips, palette='rainbow')
plt.show()
