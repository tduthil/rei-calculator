# utils/state_management.py
import streamlit as st
from datetime import datetime

def initialize_state():
    """Initialize session state variables"""
    if 'saved_properties' not in st.session_state:
        st.session_state['saved_properties'] = []
    if 'initialized' not in st.session_state:
        st.session_state['initialized'] = True

def save_property_analysis(property_data: dict):
    """Save property analysis to session state"""
    initialize_state()  # Ensure state is initialized
    property_data['timestamp'] = datetime.now().isoformat()
    st.session_state['saved_properties'].append(property_data)
    st.success("Property analysis calculated and saved!")

def clear_saved_properties():
    """Clear all saved properties"""
    initialize_state()  # Ensure state is initialized
    st.session_state['saved_properties'] = []
    st.success("All saved properties have been cleared!")
    st.rerun()

def get_saved_properties():
    """Get list of saved properties"""
    initialize_state()  # Ensure state is initialized
    return st.session_state['saved_properties']