import streamlit as st

st.set_page_config(
    page_title='SnapClass - Making Attendance faster using AI',
    page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
)

st.title("🎓 AI Attendance System - SnapClass")

try:
    from src.screens.home_screen import home_screen
    st.success("✓ home_screen imported successfully!")
except Exception as e:
    st.error(f"✗ Error importing home_screen: {e}")

try:
    from src.screens.teacher_screen import teacher_screen
    st.success("✓ teacher_screen imported successfully!")
except Exception as e:
    st.error(f"✗ Error importing teacher_screen: {e}")

try:
    from src.screens.student_screen import student_screen
    st.success("✓ student_screen imported successfully!")
except Exception as e:
    st.error(f"✗ Error importing student_screen: {e}")

st.write("All imports checked!")
