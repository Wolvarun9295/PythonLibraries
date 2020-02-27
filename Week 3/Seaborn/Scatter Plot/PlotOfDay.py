import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.set(color_codes=True)
ax = sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()
