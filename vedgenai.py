import streamlit as st
import openai

# ---- SET YOUR OPENAI API KEY ----
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ---- APP CONFIG ----
st.set_page_config(page_title="VedgenAI", page_icon="🤖", layout="wide")
st.title("VedgenAI 🌟")

# ---- INNOVATIVE FEATURES WITH IMAGES ----
st.header("Innovative Features of VedgenAI")

features = [
    {
        "title": "Hyper-Realistic Synthetic Humans",
        "description": "Generate fully customizable, photorealistic 3D humans with diverse ethnicities, body types, ages, and attire. Includes micro-expressions and natural movements for high-fidelity simulations.",
        "image": "https://i.ibb.co/KqzqDqG/synthetic-human.png"
    },
    {
        "title": "Context-Aware Scenario Generation",
        "description": "AI can place synthetic humans in complex, real-world environments—like crowded streets, offices, or industrial settings. Dynamic lighting, weather, and perspective adjustments for realistic model training.",
        "image": "https://i.ibb.co/ZY0vQzV/context-scenario.png"
    },
    {
        "title": "AI-Powered Interaction & Feedback",
        "description": "Enables interactive conversation simulations with real-time analysis and response adaptation for training or demo purposes.",
        "image": "https://i.ibb.co/9qVZw3D/ai-feedback.png"
    }
]

# Display each feature in columns with image
cols = st.columns(3)
for col, feature in zip(cols, features):
    with col:
        st.image(feature['image'], use_column_width=True)
        st.markdown(f"### {feature['title']}")
        st.write(feature['description'])
        st.markdown("---")

# ---- USER INPUT SECTION ----
st.header("Ask VedgenAI Anything 🤖")
user_input = st.text_input("Enter your question here:")

if st.button("Submit") and user_input:
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        st.success(f"VedgenAI says: {answer}")
    except Exception as e:
        st.error(f"Error: {e}")

# ---- FOOTER ----
st.markdown("---")
st.markdown("Made with ❤️ by VedgenAI")
