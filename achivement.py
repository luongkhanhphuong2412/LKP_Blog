import streamlit as st

def app():
    st.title("MY ACHIEVEMENT🌤️")

    st.write('## Associate Data Analyst in SQL')
    st.write("Issued Apr 2024")

    # Create a row layout with two columns
    image_column, text_column = st.columns((0.5, 2))

    # Display the image in the left column
    with image_column:
        st.image("images/DAA001.png")

    # Display text in the right column
    with text_column:
        st.subheader("Associate Data Analyst in SQL")
        st.write("Issued Apr 2024")

    st.write('## Google Project Management Professional Certificate')
    st.write("Issued Apr 2024")

    # Create a row layout with two columns
    image_column, text_column = st.columns((0.5, 2))

    # Display the image in the left column
    with image_column:
        st.image("images/PM.png")

    # Display text in the right column
    with text_column:
        st.subheader("Google Project Management Professional Certificate")
        st.write("Issued Apr 2024")

    st.write('## Google Data Analytics Professional Certificate')
    st.write("Issued Nov 2023")

    # Create a row layout with two columns
    image_column, text_column = st.columns((0.5, 2))

    # Display the image in the left column
    with image_column:
        st.image("images/Data.png")

    # Display text in the right column
    with text_column:
        st.subheader("Google Data Analytics Professional Certificate")
        st.write("Issued Nov 2023")

    st.write('## NUS Enterprise Summer Programme')
    st.write("Issued July 2023")

    # Create a row layout with two columns
    image_column, text_column = st.columns((0.5, 2))

    # Display the image in the left column
    with image_column:
        st.image("images/NUS.png")

    # Display text in the right column
    with text_column:
        st.subheader("NUS Enterprise Summer Programme")
        st.write("Issued July 2023")
        st.write(
            """
            - The NUS Enterprise Summer Programme is an immersive experience offered by the National University of Singapore (NUS) Enterprise, where participants spend two weeks immersed in Singapore's vibrant entrepreneurial ecosystem.
            - The program aimed at providing participants with valuable insights and practical knowledge in entrepreneurship and innovation.
            - Key features of the NUS Enterprise Summer Programme often include: 
              + Entrepreneurship Workshops
              + Hands-on Projects
              + Networking Opportunities
              + Pitch Competitions
              + Cultural and Social Activities
            """
        )
