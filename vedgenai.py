# vedgenai.py
import subprocess
import sys

# -----------------------------
# Install packages if missing
# -----------------------------
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import streamlit as st
except ImportError:
    install("streamlit")
    import streamlit as st

try:
    from openai import OpenAI
except ImportError:
    install("openai")
    from openai import OpenAI

# -----------------------------
# Initialize OpenAI client
# -----------------------------
# Add your OpenAI API key in Streamlit Secrets: OPENAI_API_KEY
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -----------------------------
# App Layout
# -----------------------------
st.set_page_config(page_title="VedgenAI", page_icon="🤖")
st.title("VedgenAI - AI Innovations Showcase")

# Innovative Features Section
st.header("🌟 Innovative Features of VedgenAI")
st.markdown("""
1. **Hyper-Realistic Synthetic Humans**  
   Generate fully customizable, photorealistic 3D humans with diverse ethnicities, body types, ages, and attire.

2. **Context-Aware Scenario Generation**  
   AI can place synthetic humans in complex, real-world environments like crowded streets, offices, or industrial settings.

3. **Dynamic AI Chat**  
   Ask questions and get intelligent responses powered by OpenAI models.
""")

st.markdown("---")

# -----------------------------
# Initialize chat memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # Store conversation history

# -----------------------------
# AI Chat Section
# -----------------------------
st.header("💬 Chat with VedgenAI")
user_input = st.text_input("Enter your question here:")

if user_input:
    # Add user's message to conversation
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("VedgenAI is thinking... 🤖"):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
            )
            answer = response.choices[0].message.content
            # Add AI response to conversation
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error(f"Error: {e}")

# Display full chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**VedgenAI:** {msg['content']}")
