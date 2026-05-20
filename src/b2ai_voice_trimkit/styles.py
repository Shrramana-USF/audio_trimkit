# styles.py - Page styling and configuration for Audio Trimming Dashboard

import streamlit as st


# Page configuration
PAGE_CONFIG = {
    "page_title": "Audio Trimming Dashboard",
    "layout": "wide"
}

# CSS styling - Sidebar adapts to theme, main content has glassmorphism
GLASSMORPHISM_CSS = """
<style>
/* Hide deploy button only */
[data-testid="stAppDeployButton"] {
    display: none !important;
}
.stDeployButton {
    display: none !important;
}
button[kind="header"] {
    display: none !important;
}

/* Hide element toolbars */
.stElementToolbar, [data-testid="stElementToolbar"] {
    display: none !important;
}

/* Title spacing */
.stMainBlockContainer h1 {
    margin-bottom: -20px !important;
    padding-bottom: 0 !important;
}
.stMainBlockContainer .stMarkdown p {
    margin-top: 0 !important;
    padding-top: 0 !important;
}

/* App background - adapts to theme */

/* Main content area - glassmorphism with fixed colors */
.stMainBlockContainer, [data-testid="stMainBlockContainer"], .block-container {
    background: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    border-radius: 20px !important;
    padding: 60px 80px !important;
    max-width: calc(100% - 100px) !important;
    margin: 70px auto !important;
}

.stMainBlockContainer, .stMainBlockContainer p, .stMainBlockContainer span,
.stMainBlockContainer label, .stMainBlockContainer div {
    color: #000000 !important;
}
.stMainBlockContainer h1, .stMainBlockContainer h2, .stMainBlockContainer h3 {
    color: #000000 !important;
}

/* Buttons in main area */
.stMainBlockContainer .stButton > button {
    background: rgba(255, 255, 255, 0.4) !important;
    border: 1px solid #cccccc !important;
    border-radius: 12px;
    color: #333333 !important;
    transition: all 0.3s ease;
}
.stMainBlockContainer .stButton > button:hover {
    background: rgba(255, 255, 255, 0.6) !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

/* Expander */
[data-testid="stExpander"] {
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 15px;
    max-width: 600px;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: rgba(255, 255, 255, 0.3);
    border-radius: 15px;
    padding: 10px;
    border: 2px dashed #333;
    max-width: 600px;
}
[data-testid="stFileUploaderDropzone"] {
    background: #ffffff !important;
    border-radius: 10px;
}
[data-testid="stFileUploaderDropzone"] span,
[data-testid="stFileUploaderDropzone"] small,
[data-testid="stFileUploaderDropzone"] div {
    color: #000000 !important;
}
[data-testid="stFileUploaderDropzone"] button {
    background: #4CAF50 !important;
    color: #ffffff !important;
    border: none !important;
}

/* Header transparent */
header[data-testid="stHeader"] {
    background: transparent !important;
}

</style>
"""


# Apply page configuration and CSS styling
def apply_styles():
    st.set_page_config(**PAGE_CONFIG)
    st.markdown(GLASSMORPHISM_CSS, unsafe_allow_html=True)


# Get the logo path from package assets
def get_logo_path():
    from importlib.resources import files
    return str(files("b2ai_voice_trimkit.assets").joinpath("Logo.jpg"))


# Display logo and title side by side
def display_header(logo_path=None):
    if logo_path is None:
        logo_path = get_logo_path()
    col1, col2 = st.columns([0.7, 6], vertical_alignment="center")
    with col1:
        st.image(logo_path, width="stretch")
    with col2:
        st.title("Audio Trimming Dashboard")
        st.markdown("A tool for acoustic researchers to trim audio files efficiently.")
