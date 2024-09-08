import numpy as np
import pandas as pd
from fuzzywuzzy import process
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv("movies.csv")
df["data"] = df["title"] + " " + df["description"]

vec = TfidfVectorizer()
vecs = vec.fit_transform(df["data"].apply(lambda x: np.str_(x)))

similarity = cosine_similarity(vecs)

def recommend(movie_title):

    movie = ""

    closest_match = process.extractOne(movie_title, list(df["title"]))
    if closest_match[1] > 90:
        movie = closest_match[0]
        
    movie_index = df[df["title"] == movie].index[0]

    scores = list(enumerate(similarity[movie_index]))
    sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)[1:]
    print(sorted_scores)
    
    movie_recommendations = list()

    for index, score in sorted_scores:
        recommendation = df.iloc[index]["title"]
        movie_recommendations.append(recommendation)

    return movie_recommendations
