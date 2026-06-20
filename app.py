import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Mood Tracker",
    page_icon="🌤️",
    layout="wide"
)


st.markdown(
    """
    <style>
    :root {
        --primary: #8b5cf6;
        --secondary: #667eea;
        --accent: #ec4899;
        --card-bg: #171a23;
        --card-border: #2b3040;
        --text-main: #f9fafb;
        --text-muted: #cbd5e1;
        --soft-bg: #0f1117;
        --shadow: rgba(0, 0, 0, 0.35);
    }

    .stApp {
        background-color: #0f1117;
        color: #f9fafb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1250px;
    }

    .hero-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.8rem;
        border-radius: 30px;
        color: white;
        box-shadow: 0 18px 45px rgba(102, 126, 234, 0.28);
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 3.4rem;
        font-weight: 900;
        margin-bottom: 0.6rem;
        color: white;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        line-height: 1.7;
        color: #f3f4f6;
        max-width: 900px;
    }

    .dashboard-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 24px;
        padding: 1.6rem;
        box-shadow: 0 12px 30px var(--shadow);
        margin-bottom: 1.4rem;
        backdrop-filter: blur(10px);
    }

    .section-title {
        color: var(--text-main);
        font-size: 1.8rem;
        font-weight: 850;
        margin-bottom: 1rem;
    }

    .section-caption {
        color: var(--text-muted);
        font-size: 1rem;
        margin-bottom: 1rem;
    }

    .result-good {
        background: linear-gradient(135deg, #16a34a 0%, #22c55e 100%);
        color: white;
        padding: 1.6rem;
        border-radius: 24px;
        font-size: 1.7rem;
        font-weight: 900;
        text-align: center;
        box-shadow: 0 14px 32px rgba(34, 197, 94, 0.25);
    }

    .result-okay {
        background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
        color: #1f2937;
        padding: 1.6rem;
        border-radius: 24px;
        font-size: 1.7rem;
        font-weight: 900;
        text-align: center;
        box-shadow: 0 14px 32px rgba(245, 158, 11, 0.25);
    }

    .result-bad {
        background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
        color: white;
        padding: 1.6rem;
        border-radius: 24px;
        font-size: 1.7rem;
        font-weight: 900;
        text-align: center;
        box-shadow: 0 14px 32px rgba(220, 38, 38, 0.25);
    }

    .tip-box {
        background: var(--card-bg);
        color: var(--text-main);
        border-left: 6px solid var(--primary);
        border-radius: 18px;
        padding: 1.1rem 1.2rem;
        margin-top: 1rem;
        box-shadow: 0 8px 22px var(--shadow);
        line-height: 1.6;
    }

    .stSlider label {
        color: #f9fafb !important;
        font-weight: 700 !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #ec4899 100%);
        color: white !important;
        border: none;
        border-radius: 16px;
        padding: 0.85rem 1rem;
        font-size: 1.05rem;
        font-weight: 800;
        box-shadow: 0 12px 26px rgba(102, 126, 234, 0.25);
    }

    .stButton > button:hover {
        color: white !important;
        border: none;
        transform: translateY(-1px);
    }

    div[data-testid="stMetric"] {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 18px;
        padding: 1rem;
        box-shadow: 0 8px 22px var(--shadow);
    }

    div[data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-weight: 700;
    }

    div[data-testid="stMetricValue"] {
        color: var(--text-main) !important;
        font-weight: 900;
    }

    section[data-testid="stSidebar"] {
        background: #171a23;
        border-right: 1px solid #2b3040;
    }

    section[data-testid="stSidebar"] * {
        color: #f9fafb !important;
    }

    .sidebar-tip {
        background: #222638;
        border-radius: 16px;
        padding: 1rem;
        color: #f9fafb;
        border: 1px solid #2b3040;
        line-height: 1.6;
    }

    .footer-text {
        text-align: center;
        color: var(--text-muted);
        margin-top: 2.5rem;
        font-size: 0.95rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def load_model():
    return joblib.load("models/mood_model.pkl")


def predict_mood(
    model,
    sleep_hours,
    stress_level,
    study_work_hours,
    exercise_minutes,
    screen_time_hours,
    water_intake,
):
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


def get_mood_details(mood):
    if mood == "Good":
        return (
            "😊",
            "Good",
            "Your habits look strong today. Keep maintaining your routine.",
            "result-good",
        )

    if mood == "Okay":
        return (
            "😐",
            "Okay",
            "Your mood looks balanced, but a little more rest, movement, or hydration may help.",
            "result-okay",
        )

    return (
        "😟",
        "Bad",
        "Your mood may be low today. Try reducing stress, resting, drinking water, and taking a short break.",
        "result-bad",
    )


def habit_score(
    sleep_hours,
    stress_level,
    exercise_minutes,
    screen_time_hours,
    water_intake,
):
    score = 0

    if 7 <= sleep_hours <= 9:
        score += 25
    elif 5 <= sleep_hours < 7 or 9 < sleep_hours <= 10:
        score += 15
    else:
        score += 6

    if stress_level <= 3:
        score += 25
    elif stress_level <= 6:
        score += 15
    else:
        score += 5

    if exercise_minutes >= 30:
        score += 20
    elif exercise_minutes >= 10:
        score += 12
    else:
        score += 4

    if screen_time_hours <= 5:
        score += 15
    elif screen_time_hours <= 8:
        score += 9
    else:
        score += 3

    if water_intake >= 7:
        score += 15
    elif water_intake >= 4:
        score += 9
    else:
        score += 3

    return min(score, 100)


with st.sidebar:
    st.title("🧠 Mood Tracker")
    st.write("Predict your mood using simple lifestyle habits.")

    st.markdown("### Inputs Used")
    st.write("🛌 Sleep hours")
    st.write("😣 Stress level")
    st.write("📚 Study/work hours")
    st.write("🏃 Exercise minutes")
    st.write("📱 Screen time")
    st.write("💧 Water intake")

    st.markdown("---")
    st.markdown(
        """
        <div class="sidebar-tip">
        <b>Tip:</b><br>
        Try changing sleep, stress, and exercise values to see how your mood prediction changes.
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">🌤️ Mood Tracker</div>
        <div class="hero-subtitle">
            A machine learning dashboard that predicts your mood from sleep, stress, work hours,
            exercise, screen time, and water intake.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


left_col, right_col = st.columns([1.25, 0.85], gap="large")

with left_col:
    st.markdown(
        """
        <div class="dashboard-card">
            <div class="section-title">📝 Enter Your Daily Details</div>
            <div class="section-caption">
                Adjust the sliders below to describe your day.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    input_col1, input_col2 = st.columns(2)

    with input_col1:
        sleep_hours = st.slider("🛌 Sleep Hours", 0, 12, 7)
        stress_level = st.slider("😣 Stress Level", 1, 10, 5)
        study_work_hours = st.slider("📚 Study/Work Hours", 0, 12, 6)

    with input_col2:
        exercise_minutes = st.slider("🏃 Exercise Minutes", 0, 120, 30)
        screen_time_hours = st.slider("📱 Screen Time Hours", 0, 15, 6)
        water_intake = st.slider("💧 Water Intake", 0, 12, 6)

    st.write("")
    predict_button = st.button("🔮 Predict My Mood", use_container_width=True)

with right_col:
    score = habit_score(
        sleep_hours,
        stress_level,
        exercise_minutes,
        screen_time_hours,
        water_intake,
    )

    st.markdown(
        f"""
        <div class="dashboard-card">
            <div class="section-title">📊 Wellness Snapshot</div>
            <div class="section-caption">
                A quick visual score based on your current habits.
            </div>
            <h2 style="color: var(--text-main); margin-bottom: 0;">{score}/100</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(score / 100)

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:
        st.metric("Sleep", f"{sleep_hours}h")
        st.metric("Exercise", f"{exercise_minutes}m")

    with metric_col2:
        st.metric("Stress", f"{stress_level}/10")
        st.metric("Water", f"{water_intake} glasses")


st.markdown("---")

if predict_button:
    try:
        model = load_model()

        mood = predict_mood(
            model,
            sleep_hours,
            stress_level,
            study_work_hours,
            exercise_minutes,
            screen_time_hours,
            water_intake,
        )

        emoji, mood_label, message, css_class = get_mood_details(mood)

        result_col, summary_col = st.columns([0.9, 1.1], gap="large")

        with result_col:
            st.markdown("## Prediction Result")
            st.markdown(
                f"""
                <div class="{css_class}">
                    {emoji} Predicted Mood: {mood_label}
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="tip-box">
                    <b>Personalized Tip</b><br>
                    {message}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with summary_col:
            st.markdown("## Input Summary")

            summary_data = pd.DataFrame(
                {
                    "Habit": [
                        "Sleep Hours",
                        "Stress Level",
                        "Study/Work Hours",
                        "Exercise Minutes",
                        "Screen Time Hours",
                        "Water Intake",
                    ],
                    "Value": [
                        sleep_hours,
                        stress_level,
                        study_work_hours,
                        exercise_minutes,
                        screen_time_hours,
                        water_intake,
                    ],
                }
            )

            st.dataframe(summary_data, use_container_width=True, hide_index=True)

    except FileNotFoundError:
        st.error("Model file not found. Please run `python src/train_model.py` first.")


st.markdown(
    """
    <div class="footer-text">
        Built with Python, Streamlit, Pandas, Scikit-learn, and GitHub.
    </div>
    """,
    unsafe_allow_html=True,
)