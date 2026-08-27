from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

dataset=pd.read_csv(r"C:\Users\rolex\OneDrive\Desktop\ML Preparation\8_Train_Test_Split\diabetes_dataset.csv")

X=dataset.drop("diabetes",axis=1)
y=dataset["diabetes"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42)

le=LabelEncoder()

X_train["gender"]=le.fit_transform(X_train["gender"])
X_test["gender"]=le.transform(X_test["gender"])

ohe=OneHotEncoder(sparse_output=False,handle_unknown="ignore")

smoking_history_train=ohe.fit_transform(X_train[["smoking_history"]])
smoking_history_test=ohe.transform(X_test[["smoking_history"]])


smoking_history_train=pd.DataFrame(smoking_history_train,columns=ohe.get_feature_names_out(["smoking_history"]),index=X_train.index)
smoking_history_test=pd.DataFrame(smoking_history_test,columns=ohe.get_feature_names_out(["smoking_history"]),index=X_test.index)

X_train=X_train.drop("smoking_history",axis=1)
X_test=X_test.drop("smoking_history",axis=1)

X_train=pd.concat([X_train,smoking_history_train],axis=1)
X_test=pd.concat([X_test,smoking_history_test],axis=1)

pd.set_option("display.max_columns",None)
print(X_train)
# print(X_train.shape)
# print(X_test.shape)