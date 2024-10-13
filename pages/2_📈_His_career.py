import streamlit as st
import pandas as pd
import plotly.express as px  # Import Plotly Express
from utils.utils import extract_genre, add_logo

# Load the dataset
df = pd.read_csv('data/imdb-movies-cleaned.csv')

# Filter the DataFrame for movies that include 'Nicolas Cage' in the 'Cast' column
cage_movies = df[df['Cast'].str.contains('Nicolas Cage', na=False)]

#add_logo()

# Sidebar for filtering
st.sidebar.title("Filter Options")
# Create buttons for chart selection
button_selected = st.sidebar.radio("Chart Type", ("# of movies", "ratings"), index=0, horizontal=True)
year_range = st.sidebar.slider("Year Range", 
                                int(cage_movies['Year'].min()), 
                                int(cage_movies['Year'].max()), 
                                (int(cage_movies['Year'].min()), int(cage_movies['Year'].max())))  # Double slider for year range

rating_filter = st.sidebar.slider("Rating", 0.0, 10.0, (0.0, 10.0), step=0.1)  # Step for one decimal place

# Extract genres for the multiselect filter
all_genres = extract_genre('data/imdb-movies-cleaned.csv')
genre_filter = st.sidebar.multiselect("Select Genre", all_genres)

# Function to check for genres
def check_genre(row):
    row_genres = [genre.strip() for genre in row['Genre'].split(',')]  # Split genres by comma and strip whitespace
    
    if not genre_filter:  # If no genre is selected, return True
        return True
    
    # Check if one genre is selected (e.g., "Action")
    if len(genre_filter) == 1:
        return genre_filter[0] in row_genres  # Return True if the single selected genre is in the row's genres

    # Check if multiple genres are selected
    return all(g in row_genres for g in genre_filter)  # Return True if all selected genres are in the row's genres

# Apply filters
filtered_movies = cage_movies[
    (cage_movies['Year'].between(year_range[0], year_range[1])) &  # Filter by year range
    (cage_movies['Rating'].between(rating_filter[0], rating_filter[1], inclusive='both')) &  # Filter by rating
    (cage_movies.apply(check_genre, axis=1))  # Apply genre filter
].dropna(subset=['Genre', 'Rating'])  # Drop rows with NaN in 'Genre' or 'Rating'

# Display the filtered movies with one decimal place for ratings
if not filtered_movies.empty:
    st.markdown(f"<h1 style='text-align: center;'>📈 His career</h1>", unsafe_allow_html=True)

    # Prepare data for charting
    chart_data = filtered_movies.groupby('Year').agg({'Rating': 'mean', 'Title': 'count'}).reset_index()
    chart_data.columns = ['Year', 'Average Rating', 'Number of Movies']

    # Display the appropriate chart based on button selected
    if button_selected == "# of movies":
        fig_movies = px.bar(chart_data, x='Year', y='Number of Movies', 
                            title='Number of Movies Featuring Nicolas Cage by Year',
                            labels={'Number of Movies': 'Number of Movies'},
                            color='Number of Movies', 
                            color_continuous_scale=px.colors.sequential.Blues)
        st.plotly_chart(fig_movies)  # Display the Plotly chart
    else:
        fig_ratings = px.bar(chart_data, x='Year', y='Average Rating', 
                             title='Average Ratings of Movies Featuring Nicolas Cage by Year',
                             labels={'Average Rating': 'Average Rating'},
                             color='Average Rating', 
                             color_continuous_scale=px.colors.sequential.Oranges)
        st.plotly_chart(fig_ratings)  # Display the Plotly chart


    # Get the top 3 movies with the highest ratings
    top_movies = filtered_movies.nlargest(3, 'Rating')[['Title', 'Poster', 'Rating']]

    st.markdown(f"<h3 style='text-align: center;'>Best movies from Nic Cage between {year_range[0]} and {year_range[1]}</h3>", unsafe_allow_html=True)

    # Create three columns for displaying the posters
    col1, col2, col3 = st.columns(3)

    # Display the movie posters
    if len(top_movies) > 0:
        with col1:
            if len(top_movies) > 0:
                st.image(top_movies.iloc[0]['Poster'], use_column_width=True)
                st.write(f"**{top_movies.iloc[0]['Title']}**")
                st.write(f"Rating: {top_movies.iloc[0]['Rating']:.1f}")

        with col2:
            if len(top_movies) > 1:
                st.image(top_movies.iloc[1]['Poster'], use_column_width=True)
                st.write(f"**{top_movies.iloc[1]['Title']}**")
                st.write(f"Rating: {top_movies.iloc[1]['Rating']:.1f}")

        with col3:
            if len(top_movies) > 2:
                st.image(top_movies.iloc[2]['Poster'], use_column_width=True)
                st.write(f"**{top_movies.iloc[2]['Title']}**")
                st.write(f"Rating: {top_movies.iloc[2]['Rating']:.1f}")

    # Assuming cage_movies contains the filtered dataset
    # Split the genres and explode them into separate rows
    genre_counts = filtered_movies['Genre'].str.get_dummies(sep=', ').sum().reset_index()
    genre_counts.columns = ['Genre', 'Count']

    # Get the top 8 genres and sum the rest as "Other"
    top_genres = genre_counts.nlargest(10, 'Count')
    other_count = genre_counts.loc[~genre_counts['Genre'].isin(top_genres['Genre'])]['Count'].sum()

    # Create a new DataFrame with the "Other" category
    if other_count > 0:
        other_row = pd.DataFrame({'Genre': ['Other'], 'Count': [other_count]})
        final_genre_counts = pd.concat([top_genres, other_row], ignore_index=True)
    else:
        final_genre_counts = top_genres

    # Create a pie chart using Plotly Express
    fig_genre_distribution = px.pie(final_genre_counts, 
                                 names='Genre', 
                                 values='Count', 
                                 title='Distribution of Movie Genres',
                                 color='Genre', 
                                 color_discrete_sequence=px.colors.qualitative.Plotly)

    # Display the pie chart in Streamlit
    st.plotly_chart(fig_genre_distribution)

    # Assuming cage_movies contains the filtered dataset
    # Split the genres and create a new DataFrame with separate rows for each genre
    genre_duration = filtered_movies.copy()
    genre_duration['Genre'] = genre_duration['Genre'].str.split(', ')  # Convert genre strings to lists
    genre_duration = genre_duration.explode('Genre')  # Explode the genres into separate rows

    # Group by Year and Genre to calculate the average duration
    average_duration_per_genre = genre_duration.groupby(['Year', 'Genre'])['Duration (min)'].mean().reset_index()

    # Count occurrences of each genre to find the top genres
    genre_counts = genre_duration['Genre'].value_counts().reset_index()
    genre_counts.columns = ['Genre', 'Count']

    # Get the top 10 genres
    top_genres = genre_counts.nlargest(10, 'Count')['Genre']

    # Add a dropdown for genre selection
    selected_genres = st.multiselect(
    'Select up to 3 genres:',
    options=top_genres.tolist(),
    default=top_genres.tolist()[:3],  # Pre-select the top 3 genres
    max_selections=3  # Limiting selection to max 3 genres
    )

    # Filter the average duration data to include only the selected genres
    filtered_duration = average_duration_per_genre[average_duration_per_genre['Genre'].isin(selected_genres)]

    # Create a line chart using Plotly Express
    fig_duration_evolution = px.line(
    filtered_duration, 
    x='Year', 
    y='Duration (min)', 
    color='Genre', 
    title='Average Duration of Movies per Genre Over the Years',
    labels={'Duration (min)': 'Average Duration (min)', 'Year': 'Year'},
    markers=True
)

    # Display the line chart in Streamlit
    st.plotly_chart(fig_duration_evolution)

    # Prepare data for director scatter plot
    director_ratings = filtered_movies.groupby('Director')['Rating'].mean().reset_index()
    director_ratings.columns = ['Director', 'Average Rating']

    # Sort by Average Rating from lowest to highest
    director_ratings = director_ratings.sort_values(by='Average Rating')

    # Create a scatter plot for average ratings by director
    fig_director_ratings = px.scatter(
    director_ratings, 
    x='Director', 
    y='Average Rating', 
    title='Average Ratings of Movies by Director',
    labels={'Average Rating': 'Average Rating', 'Director': 'Director'},
    hover_name='Director', 
    color='Average Rating', 
    color_continuous_scale=px.colors.sequential.Reds
    )

    # Display the scatter plot in Streamlit
    st.plotly_chart(fig_director_ratings)

    with st.expander("Raw data"):
        st.dataframe(cage_movies)

else:
    st.write("No movies found for the selected filters.")
