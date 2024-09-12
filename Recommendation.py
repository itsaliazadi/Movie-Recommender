import numpy as np
import pandas as pd
from fuzzywuzzy import process
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("C:\\Users\\User\\Desktop\\Movie Recommender\\Movie-Recommender\\movies.csv")

df["data"] = df["title"] + " " + df["description"]

# Initializing a TF-IDF Vectorizer to convert the text data into numerical vectors
vec = TfidfVectorizer()
# Fitting the vectorizer on the data
vecs = vec.fit_transform(df["data"].apply(lambda x: np.str_(x)))

# Calculating the cosine similarity matrix for the movie vectors
similarity = cosine_similarity(vecs)

def recommend(movie_title):

    movie = ""

    # Finding the closest match to the provided movie title using fuzzy matching
    closest_match = process.extractOne(movie_title, list(df["title"]))
    
    # If the match confidence is greater than 90, use the closest match;
    # Otherwise, return it to ask the user if it's what they're looking for
    if closest_match[1] > 90:
        movie = closest_match[0]
    else:
        return closest_match[0]
    
    try:

        movie_index = df[df["title"] == movie].index[0]

        # Get the similarity scores for all movies against the selected movie
        scores = list(enumerate(similarity[movie_index]))
        # Sorting the scores and taking the top 10
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:11]
        
        movie_recommendations = list()

        # Collecting the titles of the recommended movies based on sorted scores
        for index, score in sorted_scores:
            recommendation = df.iloc[index]["title"]
            movie_recommendations.append(recommendation)

        return movie_recommendations
    
    except:
        
        movie_recommendations = list()
        return movie_recommendations
