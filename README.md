# Mood Tracker

Mood Tracker is a machine learning web app that predicts a user's mood based on daily lifestyle habits such as sleep, stress, study/work hours, exercise, screen time and water intake.

## Live Demo

Try the app here: https://moodtrackerdd.streamlit.app/

## Features

* Predicts mood as **Good**, **Okay**, or **Bad**
* Uses daily habit inputs such as:

  * Sleep hours
  * Stress level
  * Study/work hours
  * Exercise minutes
  * Screen time
  * Water intake
* Includes a trained machine learning model
* Generates a larger sample dataset for better predictions
* Shows a wellness score based on lifestyle inputs
* Displays styled dark-themed charts for mood insights
* Built with a clean Streamlit dashboard interface

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Matplotlib
* Joblib
* Git and GitHub

## Project Structure

```text
mood tracker/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── mood_data.csv
│
├── src/
│   ├── data_loader.py
│   ├── data_summary.py
│   ├── generate_dataset.py
│   ├── preprocess.py
│   ├── predict.py
│   └── train_model.py
│
├── models/
│   └── mood_model.pkl
```

## How It Works

1. A mood dataset is created using lifestyle habit values.
2. The dataset is loaded and preprocessed.
3. A machine learning model is trained to classify mood.
4. The trained model is used inside a Streamlit app.
5. Users enter daily habit values and receive a mood prediction.
6. The app also displays mood data insights using charts.

## Installation

Clone the repository:

```bash
git clone https://github.com/dhvani7014/Mood-tracker.git
cd Mood-tracker
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Generate Dataset

To generate the mood dataset:

```bash
python src/generate_dataset.py
```

This creates or updates:

```text
data/mood_data.csv
```

## Train the Model

To train the machine learning model:

```bash
python src/train_model.py
```

This saves the trained model locally inside:

```text
models/mood_model.pkl
```

Note: The `models/` folder is ignored by Git because it contains generated model files.

## Run the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Machine Learning Model

The app uses a classification model to predict one of three mood categories:

* Good
* Okay
* Bad

The model is trained using features such as sleep hours, stress level, study/work hours, exercise minutes, screen time hours and water intake.

## Visualizations

The app includes dark-themed charts such as:

* Mood distribution chart
* Average habit values by mood category

These visualizations help show how lifestyle habits relate to mood patterns.

## Future Improvements

* Add user login
* Save daily mood entries from the app
* Add calendar-based mood history
* Deploy the app online
* Add more advanced ML models
* Improve dataset quality with real user input
* Add downloadable mood reports

