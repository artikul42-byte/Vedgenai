import streamlit as st
import openai
import os

# ----------------- Set OpenAI API key -----------------
# Make sure you set OPENAI_API_KEY in Streamlit secrets
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

# ----------------- Streamlit App -----------------
st.set_page_config(page_title="VedgenAI", layout="wide")

st.title("VedgenAI 🤖")
st.write("Welcome to VedgenAI! Explore our innovative AI features below, then try asking a question.")

# ----------------- Innovative Features Section -----------------
st.subheader("✨ Innovative Features")

features = [
    {
        "title": "Hyper-Realistic Synthetic Humans",
        "description": "Generate fully customizable, photorealistic 3D humans with diverse ethnicities, body types, ages, and attire. Include micro-expressions and natural movements for high-fidelity simulations."
    },
    {
        "title": "Context-Aware Scenario Generation",
        "description": "AI can place synthetic humans in complex, real-world environments—like crowded streets, offices, or industrial settings. Dynamic lighting, weather, and perspective adjustments for realistic model training."
    },
    {
        "title": "Intelligent Content Creation",
        "description": "Generate contextually relevant text, images, or audio for marketing, storytelling, or training purposes with minimal input."
    },
    {
        "title": "Real-Time Interaction",
        "description": "Seamlessly interact with AI models for Q&A, advice, or scenario simulations, making your experience both informative and immersive."
    }
]

cols = st.columns(2)
for i, feature in enumerate(features):
    with cols[i % 2]:
        st.markdown(f"### {feature['title']}")
        st.write(feature['description'])
        st.write("---")

# ----------------- AI Chat Section -----------------
st.subheader("Ask VedgenAI anything!")

user_input = st.text_input("Type your question here:")

if user_input:
    with st.spinner("VedgenAI is thinking..."):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=user_input,
                max_tokens=150
            )
            answer = response.choices[0].text.strip()
        except Exception as e:
            answer = f"Error: {e}"

    st.markdown(f"**VedgenAI says:** {answer}")

# ----------------- Footer -----------------
st.write("---")
st.write("Made with ❤️ using Streamlit & OpenAI")
