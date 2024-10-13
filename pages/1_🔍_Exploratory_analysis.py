import streamlit as st
import pandas as pd
import plotly.express as px
from urllib.error import URLError
from utils.utils import extract_actors, add_logo

# Page config
add_logo()

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/imdb-movies-cleaned.csv')

# Content
st.markdown(f"<h1 style='text-align: center;'>🔍 Exploratory Analysis</h1>", unsafe_allow_html=True)

# Load the dataset
try:
    data = load_data()
except URLError as e:
    st.error(f"Error loading data: {e}")

# Selectbox for columns with "Year" as the default option
column = st.selectbox("Select a column for analysis:", data.columns, index=data.columns.get_loc("Year"))

# Display statistics based on the selected column
if column in data.select_dtypes(include=['number']).columns:
    # Numeric column
    st.subheader(f"Statistics for '{column}':")

    # Create two columns for statistics
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Average:** {data[column].mean():.2f}")
        st.write(f"**Median:** {data[column].median():.2f}")
        st.write(f"**Standard Deviation:** {data[column].std():.2f}")

    with col2:
        st.write(f"**Minimum:** {data[column].min():.2f}")
        st.write(f"**Maximum:** {data[column].max():.2f}")

    # Histogram using Plotly
    fig = px.histogram(data, x=column, title=f'Histogram of {column}', nbins=30)
    st.plotly_chart(fig)

elif column in data.select_dtypes(include=['object']).columns:
    # Categorical or URL column
    st.subheader(f"Analysis for '{column}':")
    
    if column == 'Cast':
        # Count each actor individually
        actor_counts = data['Cast'].dropna().str.split(', ').explode().value_counts()
        fig = px.bar(actor_counts.head(10), x=actor_counts.index[:10], y=actor_counts.values[:10],
                     labels={'x': 'Actors', 'y': 'Count'},
                     title='Top 10 Actors in Cast')
        st.plotly_chart(fig)

    elif data[column].str.contains('http').any():  # Check for URL presence
        st.write("Here are some sample URLs:")
        sample_urls = data[column].dropna().sample(n=min(5, data[column].count()))
        for url in sample_urls:
            st.write(url)
        
        # Display the number of URLs
        num_urls = data[column].notna().sum()
        fig = px.bar(x=['URLs'], y=[num_urls], labels={'x': 'URLs', 'y': 'Count'}, title='Total URLs')
        st.plotly_chart(fig)
        
    else:
        st.write("Value counts:")
        value_counts = data[column].value_counts()

        # Bar chart for value counts using Plotly
        fig = px.bar(value_counts.head(10), x=value_counts.index[:10], y=value_counts.values[:10],
                     labels={'x': column, 'y': 'Count'},
                     title=f'Value Counts for {column}')
        st.plotly_chart(fig)

else:
    st.warning("Please select a valid column.")
