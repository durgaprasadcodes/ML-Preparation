import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.boxenplot(x="total_bill",data=tips)

plt.show()