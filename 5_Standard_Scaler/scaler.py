import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

dataset = load_breast_cancer()
df = pd.DataFrame(dataset.data,columns=dataset.feature_names)

X = df
y = dataset.target


X_tarin,X_test,y_train,y_test = train_test_split(X,y,test_size=.3,random_state=42)

scaler = StandardScaler()

X_tarin = scaler.fit_transform(X_tarin)
X_test  = scaler.transform(X_test)

# Mean --> 0
# Standardivation --> 1