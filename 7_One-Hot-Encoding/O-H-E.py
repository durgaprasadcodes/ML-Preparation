from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()

ohe = OneHotEncoder(sparse_output=False)

data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

data["species"] = iris.target_names[iris.target]

# One-hot encode
encoded_species = ohe.fit_transform(data[["species"]])

print(encoded_species)

# Create a DataFrame from encoded result
encoded_df = pd.DataFrame(
    encoded_species,
    columns=ohe.get_feature_names_out(["species"])
)

# Join it with the original DataFrame
data = pd.concat([data, encoded_df], axis=1)

sns.histplot(data=data,x="sepal length (cm)",y="sepal width (cm)",hue="species")

plt.show()