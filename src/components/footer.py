import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-weight:bold; color:#94A3B8; margin:0;"> Created with ❤️ by </p>  
            <p style="font-weight:bold; color:#3B82F6; margin:0; font-size: 1.1rem;"> Shivam Soni </p>
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-weight:bold; color:#64748B; margin:0;"> Created with ❤️ by </p>  
            <p style="font-weight:bold; color:#3B82F6; margin:0; font-size: 1.1rem;"> Shivam Soni </p>
        </div>
    """, unsafe_allow_html=True)
