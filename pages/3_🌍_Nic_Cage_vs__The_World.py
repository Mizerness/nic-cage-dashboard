import streamlit as st
import pandas as pd
from urllib.error import URLError
from utils.utils import extract_actors, add_logo

## Page config
st.set_page_config(page_title="Nic Cage vs. The World", page_icon="🌍")

add_logo()

## Header config
actors = extract_actors('data/imdb-movies-cleaned.csv')
selected_actor = st.sidebar.selectbox("Select an actor:", actors)
#selected_actor = "Brad Pitt"

## Load dataset
try:
    data = pd.read_csv('data/imdb-movies-cleaned.csv')
except FileNotFoundError as e:
    st.error("The dataset file was not found. Please check the file path.")
    st.stop()
except pd.errors.EmptyDataError as e:
    st.error("The dataset is empty. Please provide a valid CSV file.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
    st.stop()

## Content
st.markdown(f"<h1 style='text-align: center;'>Nicolas Cage vs. {selected_actor}</h1>", unsafe_allow_html=True)

# Count movies and calculate average ratings
try:
    # Count movies for Nicolas Cage
    cage_movies = data[data['Cast'].str.contains("Nicolas Cage", case=False, na=False)]
    cage_movie_count = len(cage_movies)
    cage_average_rating = cage_movies['Rating'].mean()

    # Count movies for selected actor
    actor_movies = data[data['Cast'].str.contains(selected_actor, case=False, na=False)]
    actor_movie_count = len(actor_movies)
    actor_average_rating = actor_movies['Rating'].mean()

    # Display results in two columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"<h1 style='text-align: center;'>{cage_movie_count}</h1>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'># of Movies</h6>", unsafe_allow_html=True)

        # Display the average rating with proper formatting
        average_rating_display = f"{cage_average_rating:.2f}" if pd.notna(cage_average_rating) else "N/A"

        # Display the average rating in a large font
        st.markdown(f"<h1 style='text-align: center;'>{average_rating_display}</h1>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>Average Rating</h6>", unsafe_allow_html=True)

    with col2:
        # Display the number of movies in a large font
        st.markdown(f"<h1 style='text-align: center;'>{actor_movie_count}</h1>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'># of Movies</h6>", unsafe_allow_html=True)

        # Display the average rating with proper formatting
        average_rating_display = f"{actor_average_rating:.2f}" if pd.notna(actor_average_rating) else "N/A"

        # Display the average rating in a large font
        st.markdown(f"<h1 style='text-align: center;'>{average_rating_display}</h1>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>Average Rating</h6>", unsafe_allow_html=True)


    # Function to get the best-rated movie and its poster URL
    def get_best_movie_and_poster(actor_name):
        actor_movies = data[data['Cast'].str.contains(actor_name, case=False, na=False)]
        if not actor_movies.empty:
            best_movie = actor_movies.loc[actor_movies['Rating'].idxmax()]
            return best_movie['Title'], best_movie['Poster'], best_movie['Rating']
        return None, None, None

    # Get the best movies and posters
    cage_title, cage_poster, cage_rating = get_best_movie_and_poster("Nicolas Cage")
    actor_title, actor_poster, actor_rating = get_best_movie_and_poster(selected_actor)

    st.markdown(f"<h3 style='text-align: center;'>Choose your fighter 🥊</h3>", unsafe_allow_html=True)

    # Display posters in two columns
    col1, col2 = st.columns(2)

    with col1:
        if cage_poster:
            st.image(cage_poster, caption=cage_title, use_column_width=True)
            st.markdown(f"<h6 style='text-align: center;'>Rating: {cage_rating:.2f}</h6>", unsafe_allow_html=True)
            st.button("Vote for Nicolas Cage", key="cage_button")

        else:
            st.error("No movies found for Nicolas Cage.")

    with col2:
        if actor_poster:
            st.image(actor_poster, caption=actor_title, use_column_width=True)
            st.markdown(f"<h6 style='text-align: center;'>Rating: {actor_rating:.2f}</h6>", unsafe_allow_html=True)
            st.button("Vote for {}".format(selected_actor), key="actor_button")

        else:
            st.error(f"No movies found for {selected_actor}.")

except Exception as e:
    st.error(f"An error occurred while processing the data: {e}")
