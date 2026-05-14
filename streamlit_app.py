import streamlit as st
import importlib.util
import os
import sys

st.set_page_config(layout="wide")
st.title("👩‍💻 Coding a Caesar Cipher")
st.write("Select a version from the sidebar to see how the code grows!")

# 1. Sidebar dropdown for students with exact capitalization
version = st.sidebar.selectbox(
    "Choose a version:",
    [
        "Version A: The +3 cipher", 
        "Version B: Limiting the message length",
        "Version C: Choosing the shift",
        "Version D: Encrypt or decrypt"
    ]
)

# Map dropdown choices directly to your folder paths
folder_map = {
    "Version A: The +3 cipher": ("version_A", "app_A.py"),
    "Version B: Limiting the message length": ("version_B", "app_B.py"),
    "Version C: Choosing the shift": ("version_C", "app_C.py"),
    "Version D: Encrypt or decrypt": ("version_D", "app_D.py")
}
folder_name, file_name = folder_map[version]
file_path = os.path.join(folder_name, file_name)

# 2. Split screen into side-by-side columns
col1, col2 = st.columns(2)

with col1:
    st.header("📝 Read the Code")
    st.write(f"This is the Python code running behind `{file_name}`:")
    with open(file_path, "r") as f:
        st.code(f.read(), language="python", line_numbers=True)

with col2:
    st.header("🎮 Run the Live App")
    st.write("Interact with the live result here:")
    st.divider()
    
    # Memory wipe cleanup to switch versions cleanly
    if "student_module" in sys.modules:
        sys.modules.pop("student_module")
        
    # Safely import and execute the chosen version inside Column 2
    spec = importlib.util.spec_from_file_location("student_module", file_path)
    student_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_module)
