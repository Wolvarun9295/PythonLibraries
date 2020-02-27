import seaborn as sns

tips = sns.load_dataset('iris')
sns.violinplot(x='species', y='sepal_length', data=tips, palette='rainbow')
