import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

print(tips.head())
sns.histplot(x='total_bill',data=tips,y='tip',kde=True)

plt.show()