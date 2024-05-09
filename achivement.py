import streamlit as st
from PIL import Image
image_certification1 = Image.open("images/DAA001.png")
image_coursera_project_management = Image.open("images/PM.png")
image_coursera_data_analytics= Image.open("images/Data.png")
image_NUS_transcript= Image.open("images/NUS.png")



def app():
    with st.container():
        st.title("MY ACHIEVEMENT🌤️")
        st.write('##')
        image_column, text_column = st.columns((0.5, 2))
        
        # Display the image in the first column
        with image_column:
            st.image(image_certification1)
         # Display text in the second column
        with text_column:
            st.subheader("Associate Data Analyst in SQL")
            st.write("Issued Apr 2024")

    with st.container():
        st.write('##')
        image_column, text_column = st.columns((0.5, 2))
        
        # Display the image in the first column
        with image_column:
            st.image(image_coursera_project_management)
         # Display text in the second column
        with text_column:
            st.subheader("Google Project Management Professional Certificate")
            st.write("Issued Apr 2024")

    with st.container():
        st.write('##')
        image_column, text_column = st.columns((0.5, 2))
        
        # Display the image in the first column
        with image_column:
            st.image(image_coursera_data_analytics)
         # Display text in the second column
        with text_column:
            st.subheader("Google Data Analytics Professional Certificate")
            st.write("Issued Nov 2023")

    with st.container():
        st.write('##')
        image_column, text_column = st.columns((0.5, 2))
        
        # Display the image in the first column
        with image_column:
            st.image(image_NUS_transcript)
         # Display text in the second column
        with text_column:
            st.subheader("NUS Enterprise Summer Programme")
            st.write("Issued July 2023")
            st.write(
                """
                - The NUS Enterprise Summer Programme is an immersive experience offered by the National University of Singapore (NUS) Enterprise,, where participants spend two weeks immersed in Singapore's vibrant entrepreneurial ecosystem.
                - The program aimed at providing participants with valuable insights and practical knowledge in entrepreneurship and innovation.
                - Key features of the NUS Enterprise Summer Programme often include: 
                  + Entrepreneurship Workshops
                  + Hands-on Projects
                  + Networking Opportunities
                  + Pitch Competitions
                  + Cultural and Social Activities
                """)
