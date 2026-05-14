import streamlit as st
import importlib.util
import os

st.set_page_config(layout="wide")
st.title("👩‍💻 Coding a Caesar Cipher")
st.write("Select a version from the sidebar to see how the code grows!")

# 1. Sidebar dropdown for students
version = st.sidebar.selectbox(
    "Choose a version:",
    ["Version A: A Basic +3 Cipher", "Version B: Limiting the message length"]
)

# Map dropdown choices to your exact folder paths
folder_map = {
    "Version A: A Basic +3 Cipher": ("version_A", "app_A.py"),
    "Version B: Limiting the message length": ("version_B", "app_B.py")
}
folder_name, file_name = folder_map[version]
file_path = os.path.join(folder_name, file_name)

# 2. Split screen into side-by-side columns
col1, col2 = st.columns(2)

with col1:
    st.header("📝 Read the Code")
    st.write(f"This is the Python code running behind `{file_name}`:")
    with open(file_path, "r") as f:
        st.code(f.read(), language="python")

with col2:
    st.header("🎮 Run the Live App")
    st.write("Interact with the live result here:")
    st.divider()
    
    # Imports the version code cleanly into Column 2
    spec = importlib.util.spec_from_file_location("student_module", file_path)
    student_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_module)
