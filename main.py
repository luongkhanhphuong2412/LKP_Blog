import streamlit as st
from streamlit_option_menu import option_menu
import home, achivement, message
import base64

# Set page configuration
st.set_page_config(
    page_title="Cún's Webpage",
    page_icon=":dog:",
    layout="wide"
)

class Multiapp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title= 'Khanh Phuong',
                options = ['Home', 'Achievement', 'Messages'],
                icons= ['house-fill','trophy-fill', 'envelope-fill'],
                menu_icon = 'chat-text-fill',
                default_index= 1,
                styles= {
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        if app == "Home":
            home.app()
        if app == "Achievement":
            achivement.app()    
        if app == "Messages":
            message.app()        

# Create an instance of Multiapp and run it
multiapp = Multiapp()
multiapp.run()
