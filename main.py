
import streamlit as st
from app_final_fixed import main_app_content

# Set page config
st.set_page_config(layout="wide", page_title="SMART2 Risk App")

# Display PRIME logo if available
if "logo.png" in st.session_state or True:
    st.image("logo.png", use_column_width=True)

# Run main content
main_app_content()
