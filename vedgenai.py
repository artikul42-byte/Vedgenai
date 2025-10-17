import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page configuration
st.set_page_config(
    page_title="VedgenAI",
    page_icon="🤖",
    layout="wide"
)

# App header
st.title("VedgenAI")
st.write("Your AI assistant exploring everything!")

# Innovative Features section
st.subheader("Innovative Features of VedgenAI")
st.markdown("""
1. **Hyper-Realistic Synthetic Humans**: Generate fully customizable, photorealistic 3D humans with diverse ethnicities, body types, ages, and attire.  
2. **Context-Aware Scenario Generation**: Place synthetic humans in complex, real-world environments—dynamic lighting, weather, and perspective adjustments included.  
3. **Intelligent Conversational AI**: Engage with AI that understands context, emotions, and user intent.  
4. **Advanced Knowledge Integration**: Access real-time knowledge from multiple domains for precise answers.  
""")

# User input section
st.subheader("Ask VedgenAI anything!")
user_question = st.text_input("Type your question here:")

# AI response
if user_question:
    with st.spinner("VedgenAI is researching..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are VedgenAI, a helpful AI assistant."},
                    {"role": "user", "content": user_question}
                ]
            )
            answer = response.choices[0].message.content
            st.success(answer)
        except Exception as e:
            st.error(f"Oops! Something went wrong: {e}")
