import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('flights')

x = data.pivot_table(index='year',columns='month',values='passengers')

sns.heatmap(
    data.corr(numeric_only=True),
    annot=True,
    fmt='.2f',
    linewidths=.5
)

plt.show()