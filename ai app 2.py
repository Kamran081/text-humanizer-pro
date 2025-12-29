import streamlit as st
from humanizer import humanize_text
from utils import visualize_similarity, export_doc
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Text Humanizer Pro", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    h1, h2, h3 { color: #1f77b4; }
    .caption { font-size: 14px; color: #6c757d; }
    </style>
""", unsafe_allow_html=True)

# Title and branding
st.image("logo.png", width=120)  # Optional: add your crew logo here
st.title("📝 Text Humanizer Pro")
st.caption("⚡ Tactical Rewrite Mode: Activate the Humanizer and flex your originality.")

# Input
text = st.text_area("📥 Paste GPT-generated text here:", height=200)

# Action
if st.button("🚀 Humanize Text"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        polished, similarity, sentiment, readability = humanize_text(text)

        st.subheader("✅ Humanized Output")
        st.write(polished)

        st.subheader("📊 Analysis")
        st.write(f"**Similarity with original:** {round(similarity, 3)}")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Readability Score:** {readability}")

        fig, ax = plt.subplots()
        ax.bar(["Similarity"], [similarity], color="#1f77b4")
        ax.set_ylim(0, 1)
        ax.set_title("Plagiarism Reduction")
        st.pyplot(fig)

        if st.button("📤 Export to Word"):
            export_doc(polished, "output.docx")
            st.success("✅ Exported to output.docx")
