from PIL import Image
from helperFunctions import txt2
import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
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

# st.image('pics/Banner.png')
# st.sidebar.image('pics/Block-Estate.png')
col1, col2 = st.columns(2)
with col1:
    image = Image.open('images/DP.png')
    st.image(image)

with col2:
    st.markdown("<h1 style = 'text-align: center'>Karan Singh Bagga</h1>",
                unsafe_allow_html=True)

    st.markdown("<h3 style = 'text-align: center'>Summary</h3>",
                unsafe_allow_html=True)
    st.info('''
	I am a CSE Junior. My fields of interest are Blockchains and
	Machine Learning. I have an interest in Cryptocurrencies, Problem
	Solving and Chess.
	''')

    st.markdown("<h3 style = 'text-align: center'> Skills </h3>",
                unsafe_allow_html=True)
    st.markdown('''
	- Programming:
		- Python
		- C/C++
		- Linux
	- Data processing:
		- SQL
		- Pandas
		- Numpy
	- Machine Learning:
		- scikit-learn
	''')
st.markdown("<h3>Social Media</h3>",
            unsafe_allow_html=True)

txt2("LinkedIn",
     '[LinkedIn/karan51ngh](https://www.linkedin.com/in/karan51ngh)')
txt2('Twitter', '[Twitter/karan51ngh](https://twitter.com/karan51ngh_tw)')
txt2('GitHub', '[Github/karan51ngh](https://github.com/karan51ngh)')
