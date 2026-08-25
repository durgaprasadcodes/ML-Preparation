from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


iris = load_iris()
le = LabelEncoder()

data = pd.DataFrame(iris.data,columns=iris.feature_names)
data["species"] = iris.target_names[iris.target]
data["encoded_species"] = le.fit_transform(data["species"])


sns.scatterplot(data=data ,x="petal length (cm)",y="petal width (cm)",hue="encoded_species",size="species")

plt.show()

