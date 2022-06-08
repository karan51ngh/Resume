import streamlit as st
from helperFunctions import *
st.set_page_config(
    page_title="Education",
    # page_icon="pics/icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown('''
	## Education
	''')

txt('**Bachelor of Technology** (Computer Science), *Amrita School of Engineering*, Bangalore',
    '*2019-2023*')
st.markdown('''
- GPA: **8.37**
- Subjects studied:
''')

col1, col2 = st.columns(2)
with col1:
    st.markdown('''
- **Data Structures and Algorithms**
	- Linear Data Structures 
	- Graph Theory 
	- Dynamic Programming)
       
- **Operating Systems and Bash**
	- Linux commands
	- Shell Scripting
''')
with col2:
    st.markdown('''
- **Machine Learning and Data Science**
	- Data Science
	- Regression 
	- Classification	
''')

txt('**CBSE Class 12th** (Science Stream), *Anandalaya*, Gujarat',
    '*1998-2002*')
st.markdown('''
- Percentage: **90**
- Subjects studied:
''')

col1, col2 = st.columns(2)
with col1:
    st.markdown('''
- **Physics**
	- Classical Mechanics
	- Fluid Dynamics
	- Electro Magnetics

- **Maths**
	- Diferential Calculus 
	- Integral Calculus 
	- Co-ordinate Geometry
''')
with col2:
    st.markdown('''
- **Chemistry**
	- Physical Chemistry
	- Organic Chemistry 
	- Inorganic Chemistry
''')
