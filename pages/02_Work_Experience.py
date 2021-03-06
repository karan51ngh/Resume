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
## Work Experience
''')

txt('**President(voluntary), CodeChef ASEB Chapter**',
    '08/2021-present')
st.markdown('''
- Organised 20 **competitive programming** contests. 
- Created several **medium level** Problem Solving questions.
- Created several Graphic Images using Canva
***
''')
txt('**Technical Member (voluntary), Google Developer Students Club (ASEB)**',
    '08/2021 – Present')
st.markdown('''
- Conducted a Seminar on **Economics of Bitcoin**.
	- [Event Link](https://gdsc.community.dev/events/details/developer-student-clubs-amrita-school-of-engineering-bengaluru-presents-economics-of-bitcoin/)
- Conducted a Hands-on **Linux** workshop.
	- [Event Link](https://gdsc.community.dev/events/details/developer-student-clubs-amrita-school-of-engineering-bengaluru-presents-introduction-to-linux-for-programmers-1/)
- Conducted a Hands-on **C++** workshop.
	- [Event Link](https://gdsc.community.dev/events/details/developer-student-clubs-amrita-school-of-engineering-bengaluru-presents-introduction-to-c-session-1/)
***
''')
txt('**Cryptocurrency Traader, Self Enployed**',
    '08/2021 – 10/2021')
st.markdown('''
- Made **profits** worth **$400** by trading **ERC-20** tokens
	- [Link Of Transactions](https://blockscout.com/xdai/mainnet/address/0x05780eE7d7e45012A7C44f474cF610894E6f0d44/transactions)
- Began trading with an initial amount of $0
''')
