import streamlit as st
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommender System")

# -------------------------------
# 🚀 Load + Process Data (CACHED)
# -------------------------------
@st.cache_data
def prepare_data():
    movies = pd.read_csv("tmdb_5000_movies.csv")
    credits = pd.read_csv("tmdb_5000_credits.csv")

    movies = movies.merge(credits, on="title")

    movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

    # Convert JSON columns
    def convert(text):
        return [i['name'] for i in ast.literal_eval(text)]

    def convert_cast(text):
        return [i['name'] for i in ast.literal_eval(text)[:3]]

    def fetch_director(text):
        return [i['name'] for i in ast.literal_eval(text) if i['job'] == 'Director']

    def collapse(L):
        return [i.replace(" ", "") for i in L]

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert_cast)
    movies['crew'] = movies['crew'].apply(fetch_director)

    movies['genres'] = movies['genres'].apply(collapse)
    movies['keywords'] = movies['keywords'].apply(collapse)
    movies['cast'] = movies['cast'].apply(collapse)
    movies['crew'] = movies['crew'].apply(collapse)

    # Create tags
    movies['overview'] = movies['overview'].fillna('')
    movies['tags'] = movies['overview'] + movies['genres'].astype(str) + movies['keywords'].astype(str) + movies['cast'].astype(str) + movies['crew'].astype(str)

    new_df = movies[['movie_id','title','tags']].copy()
    new_df['tags'] = new_df['tags'].fillna('').str.lower()

    # Vectorization
    cv = CountVectorizer(max_features=5000, stop_words='english')
    matrix = cv.fit_transform(new_df['tags'])

    # Similarity
    similarity = cosine_similarity(matrix)

    return new_df, similarity

# -------------------------------
# 🔄 Load with spinner
# -------------------------------
with st.spinner("Loading and preparing data..."):
    new_df, similarity = prepare_data()

# -------------------------------
# 🎯 Recommendation Function
# -------------------------------
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(new_df.iloc[i[0]].title)
    return recommended_movies

# -------------------------------
# 🎬 UI
# -------------------------------
movie_list = new_df['title'].values
selected_movie = st.selectbox("🎥 Select a movie", movie_list)

if st.button("🚀 Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("🎯 Recommended Movies:")

    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.write(recommendations[i])