from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3,random_state=42,stratify=y)


models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest Classifier": RandomForestClassifier(n_estimators=100,random_state=42)
}

results = {}

for name,model in models.items():
    scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=5,
        scoring="accuracy"
    )
    print(name)

    print("Fold scores:", scores)

    print("Mean accuracy:", scores.mean())

    print("Standard deviation:", scores.std())

    print("---------------------------")
    
    results[name] = scores.mean()

for model, accuracy in results.items():
    print(f"{model}: {accuracy:.4f}")
    
best_model = max(results, key=results.get)

print("Best model:", best_model)


    #              Complete Dataset
    #                    │
    #                    ↓
    #           Train/Test Split
    #              /          \
    #             /            \
    #            ↓              ↓
    #       Training Set      Test Set
    #            │              │
    #            │              │
    #     Cross Validation      │
    #            │              │
    #    ┌───────┼───────┐      │
    #    ↓       ↓       ↓      │
    #   LR      KNN      DT     │
    #    │       │       │      │
    #    └───────┼───────┘      │
    #            ↓              │
    #       Choose Best         │
    #          Model            │
    #            ↓              │
    #    Train Best Model       │
    #            ↓              │
    #       Final Test ─────────┘
    #            ↓
    #    Final Test Accuracy
    