import streamlit as st
import pandas as pd
import random

# Title and description
st.set_page_config(page_title="HealthAI - Intelligent Healthcare Assistant", layout="wide")
st.title("🤖 HealthAI - Intelligent Healthcare Assistant")
st.markdown("Welcome to **HealthAI**, your personal health assistant powered by AI.")

# Sample symptom data (you can replace this with a larger dataset or a model)
symptoms = [
    "Headache",
    "Fever",
    "Cough",
    "Fatigue",
    "Nausea",
    "Shortness of breath",
    "Chest pain",
    "Sore throat",
    "Runny nose",
    "Back pain"
]

# Disease prediction mock function
def predict_disease(symptom):
    disease_map = {
        "Headache": "Migraine",
        "Fever": "Viral Infection",
        "Cough": "Flu",
        "Fatigue": "Anemia",
        "Nausea": "Food Poisoning",
        "Shortness of breath": "Asthma",
        "Chest pain": "Heart Disease",
        "Sore throat": "Strep Throat",
        "Runny nose": "Common Cold",
        "Back pain": "Muscle Strain"
    }
    return disease_map.get(symptom, "Unknown")

# Layout
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Symptom Checker", "📊 Analytics", "💬 Chat Assistant", "💊 Treatment Info"])

# --- Symptom Checker ---
with tab1:
    st.header("🔍 Symptom Checker")
    selected_symptom = st.selectbox("Select a symptom for AI prediction", symptoms)

    if st.button("Predict Disease"):
        result = predict_disease(selected_symptom)
        st.success(f"🧠 Based on your symptom ({selected_symptom}), you may be experiencing: **{result}**")
        st.info("⚠️ This is a basic prediction. Always consult a healthcare professional for accurate diagnosis.")

# --- Analytics Tab ---
with tab2:
    st.header("📊 Analytics")
    sample_data = {
        "Symptom": random.choices(symptoms, k=10),
        "Occurrences": [random.randint(10, 100) for _ in range(10)]
    }
    df = pd.DataFrame(sample_data)
    st.bar_chart(df.set_index("Symptom"))

# --- Chat Assistant Tab ---
with tab3:
    st.header("💬 Health Chat Assistant")
    st.markdown("👩‍⚕️ Ask me anything about your symptoms, healthy habits, or general health advice.")
    user_question = st.text_input("💬 Your Question")
    if user_question:
        st.write("🤖 (Simulated response): I'm an AI assistant. Please consult a real doctor for emergencies.")

# --- Treatment Info Tab ---
with tab4:
    st.header("💊 Treatment Suggestions")
    st.markdown("Here are some common treatments for symptoms:")
    treatment_data = {
        "Symptom": symptoms[:5],
        "Suggested Treatment": [
            "Pain relievers, hydration",
            "Paracetamol, rest",
            "Cough syrup, steam inhalation",
            "Iron supplements, rest",
            "Oral rehydration, bland diet"
        ]
    }
    treatment_df = pd.DataFrame(treatment_data)
    st.table(treatment_df)
