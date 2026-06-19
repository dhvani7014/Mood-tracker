import joblib
import pandas as pd


def predict_mood(
    sleep_hours,
    stress_level,
    study_work_hours,
    exercise_minutes,
    screen_time_hours,
    water_intake,
):
    """
    Predict mood using the trained machine learning model.
    """
    model = joblib.load("models/mood_model.pkl")

    input_data = pd.DataFrame(
        [
            {
                "sleep_hours": sleep_hours,
                "stress_level": stress_level,
                "study_work_hours": study_work_hours,
                "exercise_minutes": exercise_minutes,
                "screen_time_hours": screen_time_hours,
                "water_intake": water_intake,
            }
        ]
    )

    prediction = model.predict(input_data)
    return prediction[0]


if __name__ == "__main__":
    predicted_mood = predict_mood(
        sleep_hours=7,
        stress_level=3,
        study_work_hours=5,
        exercise_minutes=30,
        screen_time_hours=5,
        water_intake=7,
    )

    print("Predicted Mood:", predicted_mood)