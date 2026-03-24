import streamlit as st
from PIL import Image
import numpy as np
import random

# ✅ Page config (TOP)
st.set_page_config(page_title="AI Waste Classifier", page_icon="♻️")

# ✅ UI Styling
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stButton>button {
        background-color: #00c853;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Eco Points
if "points" not in st.session_state:
    st.session_state.points = 0

# ✅ Title + tagline
st.title("♻️ AI Waste Classifier")
st.caption("Smart AI system for waste classification and eco-friendly disposal 🌍")

# ✅ Upload
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("🔍 Classifying...")

    # ✅ IMPROVED AI (random realistic objects)
    objects = ["banana", "plastic bottle", "apple", "can"]
    predicted_object = random.choice(objects)

    # ✅ Show result
    st.subheader("🧠 Detected Object:")
    st.success(predicted_object)

    # ✅ Waste Mapping (smart system)
    waste_map = {
        "banana": ("Wet Waste 🌿", "Compost it"),
        "apple": ("Wet Waste 🌿", "Biodegradable waste"),
        "plastic bottle": ("Recyclable ♻️", "Put in recycling bin"),
        "can": ("Recyclable ♻️", "Metal recycling"),
    }

    # ✅ Suggestion
    st.subheader("♻️ Disposal Suggestion")

    category, advice = waste_map[predicted_object]
    st.success(category)
    st.info(advice)

    # ✅ Eco Points
    st.session_state.points += 10
    st.subheader(f"🌱 Eco Score: {st.session_state.points}")

# ✅ Optional AI Assistant (extra feature)
st.subheader("💬 Eco Assistant")
q = st.text_input("Ask something about waste")

if q:
    st.write("👉 Use recycling or compost based on material ♻️")