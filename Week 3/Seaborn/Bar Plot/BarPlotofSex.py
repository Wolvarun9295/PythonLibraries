import seaborn as sb
from matplotlib import pyplot as plt

df = sb.load_dataset('titanic')
sb.barplot(x="sex", y="survived", hue="class", data=df)
plt.show()
