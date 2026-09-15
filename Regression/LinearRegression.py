import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from babel.numbers import format_currency

dataset = pd.read_csv(r"C:\Users\rolex\OneDrive\Desktop\ML Preparation\Regression\house_price_dataset.csv")

df = pd.DataFrame(dataset)

X, y = df.drop("price", axis=1), df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)



new_house = pd.DataFrame([{
    "area_sqft": 720,
    "bedrooms": 3,
    "bathrooms": 2,
    "age_years": 4,
    "location_score": 4,
    "distance_to_city_km": 0
}])

prediction = model.predict(new_house)[0]

formatted = format_currency(
    prediction,
    "INR",
    locale="en_IN"
)

print("Predicted Price:", formatted)

min_value = min(y_test.min(), y_pred.min())
max_value = max(y_test.max(), y_pred.max())

plt.scatter(y_test, y_pred, color="r", alpha=.5)

plt.title("House Price Prediction")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--"
)

plt.show()

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