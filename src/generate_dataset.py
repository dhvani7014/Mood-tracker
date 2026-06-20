import random
import pandas as pd


def assign_mood(
    sleep_hours,
    stress_level,
    study_work_hours,
    exercise_minutes,
    screen_time_hours,
    water_intake,
):
    """
    Assign mood label based on lifestyle habits.
    This creates a more balanced dataset for model training.
    """
    score = 0

    if 7 <= sleep_hours <= 9:
        score += 2
    elif 5 <= sleep_hours < 7:
        score += 1
    else:
        score -= 2

    if stress_level <= 3:
        score += 2
    elif stress_level <= 6:
        score += 0
    else:
        score -= 3

    if study_work_hours <= 6:
        score += 1
    elif study_work_hours <= 9:
        score += 0
    else:
        score -= 1

    if exercise_minutes >= 30:
        score += 2
    elif exercise_minutes >= 10:
        score += 1
    else:
        score -= 1

    if screen_time_hours <= 5:
        score += 1
    elif screen_time_hours <= 8:
        score += 0
    else:
        score -= 2

    if water_intake >= 7:
        score += 1
    elif water_intake >= 4:
        score += 0
    else:
        score -= 1

    if score >= 4:
        return "Good"
    elif score >= 0:
        return "Okay"
    else:
        return "Bad"


def generate_mood_dataset(num_records=200):
    """
    Generate sample mood tracking data.
    """
    records = []

    for day in range(1, num_records + 1):
        sleep_hours = random.randint(3, 10)
        stress_level = random.randint(1, 10)
        study_work_hours = random.randint(1, 12)
        exercise_minutes = random.randint(0, 90)
        screen_time_hours = random.randint(2, 12)
        water_intake = random.randint(2, 10)

        mood = assign_mood(
            sleep_hours,
            stress_level,
            study_work_hours,
            exercise_minutes,
            screen_time_hours,
            water_intake,
        )

        records.append(
            {
                "date": f"2026-06-{(day % 30) + 1:02d}",
                "sleep_hours": sleep_hours,
                "stress_level": stress_level,
                "study_work_hours": study_work_hours,
                "exercise_minutes": exercise_minutes,
                "screen_time_hours": screen_time_hours,
                "water_intake": water_intake,
                "mood": mood,
            }
        )

    data = pd.DataFrame(records)
    data.to_csv("data/mood_data.csv", index=False)

    print("Generated mood dataset successfully!")
    print(data["mood"].value_counts())


if __name__ == "__main__":
    generate_mood_dataset()