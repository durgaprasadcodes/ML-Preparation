import numpy as np
import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download("punkt")
# nltk.download("punkt_tab")
# nltk.download("stopwords")


data = pd.read_csv(r"C:\Users\rolex\OneDrive\Desktop\ML Preparation\9_Feature_Extraction\emails.csv")

# Store stopwords once
stop_words = set(stopwords.words("english"))

# Process text data

def process_text(text):

    # lowercase
    text = text.lower()

    # remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # tokenize
    tokens = word_tokenize(text)

    # remove stopwords
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # convert tokens back to sentence
    return " ".join(tokens)


# Apply preprocessing
data["processed_data"] = data["text"].apply(process_text)


# Features and target
X = data["processed_data"]
y = data["spam"]


# Split data FIRST
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# TF-IDF
tfidf = TfidfVectorizer()

X_train = tfidf.fit_transform(X_train)

X_test = tfidf.transform(X_test)

model = MultinomialNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print(accuracy)

sample_email = """
Congratulations! You have won a FREE iPhone.
Click here now to claim your prize immediately.
Limited time offer click here to win the prize !
"""

processed_email = process_text(sample_email)

email_vector = tfidf.transform([processed_email])

prediction = model.predict(email_vector)

print(prediction)

if prediction[0] == 1:
    print("🚨 This email is SPAM")
else:
    print("✅ This email is NOT SPAM")