import streamlit as st
from streamlit.logger import get_logger
from utils.utils import add_logo

LOGGER = get_logger(__name__)

def run():
    
    st.set_page_config(
        page_title="Nicolas Cage",
        page_icon="🎬",
    )

    add_logo()

    st.write("# Dive into Nicolas Cage's Legendary Career")

    st.sidebar.success("Navigate through the options above.")

    st.markdown(
        """
        Welcome to this Nicolas Cage career explorer! This app provides a detailed look at the iconic actor's filmography, using data sourced from IMDB.
        
        **👈 Select a page from the sidebar** to start exploring the remarkable career of one of the most versatile actors of our time.
        
        ### What You’ll Find:
        - **Exploratory Analysis**: Dive into the dataset we're using for this app, with insights and clean data preparation explained in the code.
        - **Career Overview**: A deep dive into Nicolas Cage's career highlights, along with some fun and surprising insights.
        - **Nic Cage vs. The World**: Compare Nicolas Cage's career with other actors and see how he stacks up in this fun face-off!
        
        ### Need Assistance?
        - **Email**: lazaremasset@gmail.com
        - **GitHub**: Mizerness
        """
    )

if __name__ == "__main__":
    run()
