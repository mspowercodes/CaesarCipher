import streamlit as st
import importlib.util
import os
import sys

st.set_page_config(layout="wide")
st.title("Chapter 1: Caesar Ciphers")

# 1. Sidebar dropdown for students with exact capitalization
version = st.sidebar.selectbox(
    "Choose a script:",
    [
        "Problems 1-2: Alice's +3 Cipher",
        "Problem 3: Modified +3 Cipher",
        "Problem 4a: Encrypting a +4 Cipher",
        "Problem 4d: Decrypting a +4 Cipher",
        "Problem 5: Claire's Simplified +3 Cipher"
    ]
)

# Map dropdown choices directly to your folder paths
folder_map = {
    "Problems 1-2: Alice's +3 Cipher": ("Problems1-2", "app_p1.2.py"),
    "Problem 3: Modified +3 Cipher": ("Problem3", "app_p3.py"),
    "Problem 4a: Encrypting a +4 Cipher": ("Problem4a", "app_p4a.py"),
    "Problem 4d: Decrypting a +4 Cipher": ("Problem4d", "app_p4d.py"),
    "Problem 5: Claire's Simplified +3 Cipher": ("Problem5", "app_p5.py")
}
folder_name, file_name = folder_map[version]
file_path = os.path.join(folder_name, file_name)

# 2. Split screen into side-by-side columns
col1, col2 = st.columns(2)

with col1:
    st.header("The Script")
    st.write(f"This is the Python code running behind `{file_name}`:")
    with open(file_path, "r") as f:
        st.code(f.read(), language="python", line_numbers=True)

with col2:
    # Memory wipe cleanup to switch versions cleanly
    if "student_module" in sys.modules:
        sys.modules.pop("student_module")
        
    # Safely import and execute the chosen version inside Column 2
    spec = importlib.util.spec_from_file_location("student_module", file_path)
    student_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_module)
