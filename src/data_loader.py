import pandas as pd


def load_mood_data(file_path="data/mood_data.csv"):
    """
    Load mood tracking data from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data


if __name__ == "__main__":
    mood_data = load_mood_data()
    print("Mood data loaded successfully!")
    print(mood_data.head())