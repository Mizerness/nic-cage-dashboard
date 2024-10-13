import pandas as pd
import streamlit as st

# Define the function to extract all unique actor names from the "Cast" column
def extract_actors(file_path):
    # Load the dataset from the specified CSV file
    df = pd.read_csv(file_path)
    
    # Initialize a dictionary to count occurrences of each actor
    actor_count = {}
    
    # Iterate over each row in the "Cast" column
    for cast_list in df['Cast']:
        # Ensure cast_list is a string, skip if it's not (like NaN or None)
        if isinstance(cast_list, str):
            # Split the cast string by commas and strip any extra spaces around names
            actors = [actor.strip() for actor in cast_list.split(',')]
            # Count each actor's appearances
            for actor in actors:
                if actor in actor_count:
                    actor_count[actor] += 1
                else:
                    actor_count[actor] = 1
    
    # Filter actors who have appeared in at least 5 movies
    all_actors = {actor for actor, count in actor_count.items() if count >= 5}
    
    return all_actors

# Define the function to extract all unique actor names from the "Cast" column
def extract_genre(file_path):
    # Load the dataset from the specified CSV file
    df = pd.read_csv(file_path)
    
    # Initialize a dictionary to count occurrences of each actor
    actor_count = {}
    
    # Iterate over each row in the "Cast" column
    for cast_list in df['Genre']:
        # Ensure cast_list is a string, skip if it's not (like NaN or None)
        if isinstance(cast_list, str):
            # Split the cast string by commas and strip any extra spaces around names
            actors = [actor.strip() for actor in cast_list.split(',')]
            # Count each actor's appearances
            for actor in actors:
                if actor in actor_count:
                    actor_count[actor] += 1
                else:
                    actor_count[actor] = 1
    
    # Filter actors who have appeared in at least 5 movies
    all_actors = {actor for actor, count in actor_count.items() if count >= 5}
    
    return all_actors



def add_logo():
  st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] {
            background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlvNgetEBhUikAQS1CPYOE1qjsjhlSCFH8mA&s);
            background-repeat: no-repeat;
            background-size: 100px 100px;
            padding-top: 60px;
            padding-bottom: 40px; /* Adds some space between the image and the rest of the content */
            background-position: 20px 20px;
        }
        [data-testid="stSidebarNav"]::before {
            content: "Menu";
            margin-left: 20px;
            margin-top: 10px; /* Brings the "Menu" text closer to the image */
            font-size: 30px;
            position: relative;
            top: 80px; /* Adjusts the position so it's closer to the image */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

