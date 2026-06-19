from data_loader import load_mood_data


def summarize_mood_data():
    """
    Display basic summary statistics for the mood dataset.
    """
    data = load_mood_data()

    print("Mood Data Summary")
    print("-----------------")
    print(f"Total records: {len(data)}")
    print(f"Average sleep hours: {data['sleep_hours'].mean():.2f}")
    print(f"Average stress level: {data['stress_level'].mean():.2f}")
    print(f"Average study/work hours: {data['study_work_hours'].mean():.2f}")
    print(f"Average exercise minutes: {data['exercise_minutes'].mean():.2f}")
    print(f"Average screen time hours: {data['screen_time_hours'].mean():.2f}")
    print(f"Average water intake: {data['water_intake'].mean():.2f}")

    print("\nMood counts:")
    print(data["mood"].value_counts())


if __name__ == "__main__":
    summarize_mood_data()