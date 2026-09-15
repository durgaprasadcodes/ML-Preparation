import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

dataset = pd.read_csv(r"C:\Users\rolex\OneDrive\Desktop\ML Preparation\Regression\house_price_dataset.csv")

df = pd.DataFrame(dataset)

X,y = df.drop("price",axis=1),df["price"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3,random_state=42)

model = LinearRegression()

model.fit(X_train,y_train)


new_house = pd.DataFrame([{
    "area_sqft": 720,
    "bedrooms": 3,
    "bathrooms": 2,
    "age_years": 4,
    "location_score": 4,
    "distance_to_city_km": 0
}])

print(model.predict(new_house))


# y_pred = model.predict(X_test)

# mae = mean_absolute_error(y_test,y_pred)
# mse = mean_squared_error(y_test,y_pred)
# r2 =  r2_score(y_test,y_pred)

# print("mae :",mae)
# print("mse :",mse)
# print("r2s :",r2)

# print(df.corr(numeric_only=True)["price"].sort_values(ascending=False))

# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.columns)


# scores = cross_val_score(
#     model,
#     X,
#     y,
#     cv=5,
#     scoring="r2"
# )

# print("CV Scores:", scores)
# print("Mean CV R²:", scores.mean())

# print("Intercept:", model.intercept_)

# coefficients = pd.DataFrame({
#     "Feature": X.columns,
#     "Coefficient": model.coef_
# })

# print(coefficients)