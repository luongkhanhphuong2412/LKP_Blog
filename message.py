import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

def app():
        # Function to load Lottie animation from URL
    def load_lottie_url(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
        # Load Lottie animation for coding section
    lottie_coding_url = "https://lottie.host/607d26e5-ee73-4eef-8bbe-a92271c0d46e/aWRQzCgaIM.json"
    lottie_coding = load_lottie_url(lottie_coding_url)
    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")
    with st.container():
        st.title("Get in touch with me!💖")
        st.write("##")

        # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/luongkhanhphuong2412@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your lovely name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_coding, height=300, key="messages")
