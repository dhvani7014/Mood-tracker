import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from preprocess import preprocess_mood_data


def train_mood_model():
    """
    Train a simple machine learning model to predict mood.
    """
    X, y = preprocess_mood_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("Model training completed successfully!")
    print(f"Model accuracy: {accuracy:.2f}")

    joblib.dump(model, "models/mood_model.pkl")
    print("Model saved to models/mood_model.pkl")


if __name__ == "__main__":
    train_mood_model()