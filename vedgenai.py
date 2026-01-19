import streamlit as st
from openai import OpenAI

# Page config
st.set_page_config(page_title="VedgenAI", layout="wide")

# Title
st.title("VedgenAI 🚀")
st.markdown("Welcome to VedgenAI - Explore innovative AI features!")

# Innovative Features Section
st.header("Innovative Features")
st.markdown("""
1. **Hyper-Realistic Synthetic Humans**  
   Generate fully customizable, photorealistic 3D humans with diverse ethnicities, body types, ages, and attire.
   
2. **Context-Aware Scenario Generation**  
   AI can place synthetic humans in complex, real-world environments with dynamic lighting, weather, and perspectives.

3. **Intelligent Content Assistance**  
   Generate text, summaries, or code snippets with context-aware AI support.
""")

# Cards / Columns for Quick Feature Overview
st.header("Feature Overview")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("3D Human Modeling")
    st.image("https://via.placeholder.com/150", use_column_width=True)
    st.write("Create photorealistic humans with full control over appearance and expressions.")

with col2:
    st.subheader("Scenario Generation")
    st.image("https://via.placeholder.com/150", use_column_width=True)
    st.write("Place humans in realistic environments with AI-driven adjustments.")

with col3:
    st.subheader("AI Text & Code")
    st.image("https://via.placeholder.com/150", use_column_width=True)
    st.write("Generate AI-assisted text, summaries, and code in real-time.")

# Interactive AI Query Section
st.header("Ask VedgenAI")
user_input = st.text_input("Type your question here:")

if user_input:
    with st.spinner("VedgenAI is thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": user_input}]
            )
            answer = response.choices[0].message.content
            st.success(answer)
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.markdown("Made with ❤️ by VedgenAI")
