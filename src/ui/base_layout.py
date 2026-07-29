import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #0F172A !important; /* Deep Slate Dark Background */
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #1E293B !important; /* Slightly lighter Slate for cards */
                padding: 2.5rem !important;
                border-radius: 1.5rem !important; /* Professional smooth corners */
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2) !important; /* Subtle depth shadow */
                border: 1px solid #334155 !important;
            }
        </style>  
        """, unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #F8FAFC !important; /* Clean minimal light background for dashboard */
            }
            
            /* Changing text color for light background in dashboard */
            .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
                color: #0F172A !important;
            }
        </style>  
        """, unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>
            /* Importing Modern Tech Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

            /* Hide Top Bar of streamlit */
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top: 1.5rem !important;    
            }

            /* Main Headings */
            h1 {
                font-family: 'Space Grotesk', sans-serif !important;
                font-size: 3rem !important;
                font-weight: 700 !important;
                letter-spacing: -1px !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #3B82F6 !important; /* Modern Blue Accent */
            }

            /* Sub-headings */
            h2 {
                font-family: 'Space Grotesk', sans-serif !important;
                font-size: 1.8rem !important;
                font-weight: 600 !important;
                line-height: 1 !important;
                margin-bottom: 0rem !important;
            }
                
            /* Body Text */
            h3, h4, p, label, div {
                font-family: 'Outfit', sans-serif !important;    
            }

            /* Primary Button (e.g., Create Account / Enroll) */
            button[kind="primary"] {
                border-radius: 1rem !important;
                background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%) !important;
                color: white !important;
                padding: 12px 24px !important;
                font-weight: 600 !important;
                border: none !important;
                box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3) !important;
                transition: all 0.3s ease !important;
            }

            /* Secondary Button (e.g., Go Back / Logout) */
            button[kind="secondary"] {
                border-radius: 1rem !important;
                background-color: #F1F5F9 !important;
                color: #475569 !important;
                padding: 12px 24px !important;
                font-weight: 600 !important;
                border: 1px solid #CBD5E1 !important;
                transition: all 0.3s ease !important;
            }

            /* Tertiary Button (e.g., Unenroll/Delete) */
            button[kind="tertiary"] {
                border-radius: 1rem !important;
                background-color: #FEF2F2 !important;
                color: #DC2626 !important; /* Warning Red */
                padding: 12px 24px !important;
                font-weight: 600 !important;
                border: 1px solid #FCA5A5 !important;
                transition: all 0.3s ease !important;
            }

            /* Universal Hover Effect for all buttons */
            button:hover {
                transform: translateY(-2px) !important;
                filter: brightness(1.1) !important;
            }
            
            /* Input Fields Styling (Text boxes, etc) */
            div[data-baseweb="input"] {
                border-radius: 0.75rem !important;
            }
        </style>  
        """, unsafe_allow_html=True)