import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Function to load Lottie animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Load Lottie animation for coding section
lottie_coding_url = "https://lottie.host/3088300b-6ef1-4a19-ad0a-fa4fb141d75e/H4PoeWE5YO.json"
lottie_coding = load_lottie_url(lottie_coding_url)

# Streamlit layout
st.set_page_config(
    page_title="Cún's Webpage",
    page_icon=":dog:",
    layout="wide"
)
with st.container():
# Header Section
    st.header("Hi everyone :wave:")

    # Creating two columns layout
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown("### I AM **<font color='red'>LUONG KHANH PHUONG</font>** :hatching_chick:", unsafe_allow_html=True)
        st.title("A Data Analytics Student")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

    with left_column:
        st.write(":point_right: I am deeply passionate about transforming raw data into actionable insights. I specialize in <span style='color:#a52a2a;'>data analysis</span>, <span style='color:#a52a2a;'>data modelling</span>, <span style='color:#a52a2a;'>data visualization</span> and have a proven record of providing valuable insights to my organization, helping them improve their performance and operations.", unsafe_allow_html= True)
        st.write(":point_right: My goal is to continue leveraging data to help businesses reach their objectives.")
        st.write("[Know more about me:>](https://www.linkedin.com/in/iamkapi2412/)")

# Introduce about myself:
with st.container():
    st.write("___")
    st.markdown("## LET ME **<font color='red'>INTRODUCE</font>** ABOUT MYSELF", unsafe_allow_html= True)

    left_column, right_column= st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
        Currently, I'm second-year student at the International School of Vietnam National University, I've been refining my skills in data analysis and visualization.
        - I'm skilled in Python and SQL, using them to efficiently manipulate data and extract valuable insights. Additionally, I'm proficient in data visualization tools like PowerBI, which I use to create clear and compelling visuals for decision-making.")

        - Throughout my academic journey, I've tackled projects demanding critical thinking and problem-solving. Whether it's analyzing datasets for trends or crafting interactive dashboards, I thrive on challenges that let me leverage my analytical skills.

        - My approach to data analysis combines technical prowess with a deep understanding of business needs. I excel at distilling complex information into clear narratives and presenting findings effectively to stakeholders.

        - With a passion for uncovering meaningful insights, I'm excited to bring my skills to your organization as a Data Analyst.
        """
        )
    with right_column:
        lottie_coding_url = "https://lottie.host/09c5154e-938a-463a-944a-54f04f69a5ab/sIAiNjzV8v.json"
        lottie_coding = load_lottie_url(lottie_coding_url)
        st_lottie(lottie_coding, height=300, key="hi")

# Professional skillset: 

with st.container():
    st.write("---")
    st.header("MY PROFESSIONAL SKILLSET")
    my_sql_logo = st.image('MYSQL_logo.png')
    st.write("MySQL")
