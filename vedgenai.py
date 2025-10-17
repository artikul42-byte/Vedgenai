import streamlit as st
import openai
from time import sleep

# --- OpenAI API Key ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Page Config ---
st.set_page_config(page_title="VedgenAI", layout="wide")

# --- Header ---
st.title("VedgenAI 🚀")
st.subheader("Innovative AI Features Showcase")

# --- Innovative Features Section ---
st.markdown("### Our Innovative Features")

# Columns for feature cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Hyper-Realistic Synthetic Humans**")
    st.write("Generate fully customizable, photorealistic 3D humans with diverse ethnicities, body types, ages, and attire. Includes micro-expressions and natural movements for high-fidelity simulations.")

with col2:
    st.markdown("**Context-Aware Scenario Generation**")
    st.write("Place synthetic humans in complex, real-world environments—like crowded streets, offices, or industrial settings. Dynamic lighting, weather, and perspective adjustments for realism.")

with col3:
    st.markdown("**Intelligent Automation & Insights**")
    st.write("AI generates data-driven insights, automates repetitive tasks, and adapts to user preferences for smarter decision-making.")

# --- Research Feature Section ---
st.markdown("### Research Feature")
st.write(
    "VedgenAI can perform advanced research tasks, summarizing large volumes of information, extracting key insights, "
    "and generating concise reports from data or documents provided by the user. Perfect for learning, business analysis, or academic work."
)

st.markdown("---")

# --- User Input Section ---
st.subheader("Ask VedgenAI Anything")
user_input = st.text_input("Type your question here:")

if st.button("Submit"):
    if not user_input:
        st.warning("Please type something!")
    else:
        # Show spinner while AI thinks
        with st.spinner("VedgenAI is researching
