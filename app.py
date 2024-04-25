import streamlit as st
import os

from fileingestor import FileIngestor
from loadllm import Loadllm  # Import the Loadllm class

# Set page title and favicon
st.set_page_config(page_title="RAMAN_EFFECT")

# Define page layout
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .sidebar .sidebar-content {
            background-color: #263238; /* Dark blue-grey */
            color: #ffffff; /* White text */
            padding: 20px;
            padding-top: 40px; /* Increase top padding */
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            transition: all 0.3s ease;
        }
        .sidebar .sidebar-content .stButton>button {
            background-color: #009688; /* Teal */
            color: #ffffff;
            border-color: #009688;
            border-radius: 8px;
            margin-top: 15px;
            transition: all 0.3s ease;
            box-shadow: none;
        }
        .sidebar .sidebar-content .stButton>button:hover {
            background-color: #00796b; /* Darker teal on hover */
            color: #ffffff;
            border-color: #00796b;
            box-shadow: none;
        }
        .sidebar .sidebar-content .st-expander {
            padding: 10px;
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 15px;
            transition: all 0.3s ease;
        }
        
        .custom-sidebar-item {
            margin-bottom: 20px; /* Increase bottom margin */
        }
        
        
        .sidebar .sidebar-content .st-expander .stBlock {
            padding: 10px;
            border-radius: 15px;
        }
        .sidebar .sidebar-content .st-expander .stBlock>p {
            color: #cccccc; /* Light grey text */
        }
        .sidebar .sidebar-content .st-expander .stButton>button {
            background-color: #ff5722; /* Deep orange */
            color: #ffffff;
            border-color: #ff5722;
            border-radius: 8px;
            margin-top: 15px;
            transition: all 0.3s ease;
            box-shadow: none;
        }
        .sidebar .sidebar-content .st-expander .stButton>button:hover {
            background-color: #e64a19; /* Darker orange on hover */
            color: #ffffff;
            border-color: #e64a19;
            box-shadow: none;
        }
        .sidebar .sidebar-content .stExpander>.stButton>button:before {
            content: "\\2B9C"; /* Unicode down arrow */
            font-family: 'Arial Unicode MS';
            float: right;
            margin-top: 2px;
            margin-right: 5px;
            transition: all 0.3s ease;
        }
        .sidebar .sidebar-content .stExpander.stExpanded>.stButton>button:before {
            content: "\\2B9D"; /* Unicode up arrow */
        }
        
        .title-container {
            margin-top: 10px !important; /* Decrease margin top */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar layout
st.sidebar.title(":rocket: Navigation")

# Data Dashboard section
st.sidebar.subheader(":file_folder: DATA DASHBOARD")
uploaded_file = st.sidebar.file_uploader("", type="pdf")

st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Fine Tune section
st.sidebar.subheader("FINE TUNE LLM")
fine_tune_expander = st.sidebar.expander(":wrench: Change Parameters", expanded=False)
with fine_tune_expander:
    n_gpu_layers = st.slider("Number of GPU Layers", min_value=1, max_value=100, value=40)
    n_batch = st.slider("Batch Size", min_value=1, max_value=1024, value=512)
    n_ctx = st.slider("Context Size", min_value=128, max_value=4096, value=2048)
    
st.sidebar.markdown("<br>", unsafe_allow_html=True)    

# About Us section
st.sidebar.subheader(":information_source: About Us")
st.sidebar.info(
    "Done under **FEYNMAN_ORIGINALS**.\n"
    "If you encounter any issues or would like to learn more about our project, "
    "[visit our GitHub repository](https://github.com/gauraviiitg/Raman_Effect)."
)

# Main content layout
st.title(":sparkles: *RAMAN_EFFECT* : Chat with data")

if uploaded_file:
    file_ingestor = FileIngestor(uploaded_file)
    file_ingestor.handlefileandingest(n_gpu_layers, n_batch, n_ctx)
else:
    st.write("""
    
    
    
    
    ### Instructions

    1. Clone the repository:
        ```bash
        git clone https://github.com/gauraviiitg/Raman_Effect.git
        ```
    2. Navigate to the project directory:
        ```bash
        cd Raman_Effect
        ```
    3. Install the required dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    4. Download additional models:
        - Download spaCy model:
            ```bash
            python -m spacy download en_core_web_sm
            ```
        - Download NLTK stopwords:
            ```bash
            python -m nltk.downloader stopwords
            ```
        - Download Hugging Face model:
            ```bash
            curl -OJL https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf
            ```
    5. Run the Streamlit application:
        ```bash
        streamlit run app.py
        ```
    """)

