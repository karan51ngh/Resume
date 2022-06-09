import streamlit as st
from helperFunctions import *
st.set_page_config(
    page_title="Work Experience",
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
## My Projects
''')

txt('**Implementation of a Blockchain to store Land**',
    '01/2022 – 06/2022')
st.markdown('''
- Implemented a **Blockchain** in Python 
- Implemented **Mining** and **Proof of Work** mechanism using the **SHA256** Hashing Algorithm
- Hosted the blockchain on **streamlit cloud**
- Hosted Link: [Streamlit Cloud](https://share.streamlit.io/karan51ngh/plot-chain/main/landLedger.py)
- Repository Link: [Github](https://github.com/karan51ngh/Plot-Chain)
***
''')
txt('**Machine Learning Case Studies**',
    '06/2021 – 09/2021')
st.markdown('''
- Usage of various **Regression** Algorithms
- Usage of various **Classification** Algorithms
- Case Studies of Titanic Dataset and PUBG Dataset
- Repository Link: [Github](https://github.com/karan51ngh/machineLearning)
''')
