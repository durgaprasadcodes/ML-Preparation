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

def predict(area_sqft,bedrooms,bathrooms,age_years,location_score,distance_to_city_km):
    new_house = pd.DataFrame([{
        "area_sqft": area_sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age_years": age_years,
        "location_score": location_score,
        "distance_to_city_km": distance_to_city_km
    }])

    prediction = model.predict(new_house)[0]

    formatted = format_currency(
        prediction,
        "INR",
        locale="en_IN"
    )

    return formatted,{
        "area_sqft": area_sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age_years": age_years,
        "location_score": location_score,
        "distance_to_city_km": distance_to_city_km
    }
print(predict(780,4,4,10,8,2))
