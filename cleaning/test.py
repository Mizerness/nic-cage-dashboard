import pandas as pd

# Load the dataset
df = pd.read_csv('data/imdb-movies-cleaned.csv')


# Define the function to extract all unique actor names from the "Cast" column
def extract_actors(file_path):
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


print(extract_actors('data/imdb-movies-cleaned.csv'))