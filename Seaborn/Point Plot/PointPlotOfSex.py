import seaborn as sb
from matplotlib import pyplot as plt

df = sb.load_dataset('titanic')
sb.pointplot(x="sex", y="survived", hue="class", data=df)
plt.show()
