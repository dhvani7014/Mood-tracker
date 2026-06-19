from data_loader import load_mood_data


def preprocess_mood_data():
    """
    Prepare mood data for machine learning.
    Separates input features from the target mood label.
    """
    data = load_mood_data()

    features = data[
        [
            "sleep_hours",
            "stress_level",
            "study_work_hours",
            "exercise_minutes",
            "screen_time_hours",
            "water_intake",
        ]
    ]

    target = data["mood"]

    return features, target


if __name__ == "__main__":
    X, y = preprocess_mood_data()

    print("Preprocessing completed successfully!")
    print("Feature columns:")
    print(X.head())

    print("\nTarget values:")
    print(y.head())