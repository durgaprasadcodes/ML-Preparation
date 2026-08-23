import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

sns.scatterplot(
    data=iris,
    x = 'sepal_length',
    y = 'sepal_width',
    hue='species'
)
plt.show()