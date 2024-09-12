# Movie-Recommender

# Overview
The **Movie Recommender** is a Python-based application that provides personalized movie recommendations based on user input. The project utilizes web scraping to gather movie data, along with machine learning techniques such as cosine similarity for recommending movies. The application features a user-friendly graphical interface built with custom tkinter.

# Features
* Movie Recommendations: Get personalized recommendations based on the movie you input.
* Web Scraping: Automatically scrapes data from the IMDb Top 1000 Movies page.
* Natural Language Processing: Uses the fuzzywuzzy library for fuzzy matching of movie titles, ensuring better user experience.
* Cosine Similarity: Implements cosine similarity to calculate the similarity between movies based on their descriptions.
* Graphical User Interface: Built with Tkinter and CustomTkinter for an appealing user experience.
* Alternative Movie Suggestions: If the input movie title doesn't match any in the database, the application suggests alternative movies based on fuzzy matching.

# Technologies Used
* Pandas: For data manipulation and analysis.
* FuzzyWuzzy: For fuzzy matching of movie titles.
* Scikit-learn: For cosine similarity.
* BeautifulSoup: For web scraping content from IMDb.
* Selenium: For automating web browsing tasks.
* Custom Tkinter: For creating the graphical user interface.
  
# Getting Started
Make sure you have the following installed on your machine:
* Python (version 3.x)
* Pip
* Clone this repository to your local machine:

git clone https://github.com/itsaliazadi/Movie-Recommender

Change into the project directory:
cd movie-recommender

Install the required packages:
pip install pandas numpy fuzzywuzzy scikit-learn beautifulsoup4 selenium customtkinter

Navigate to the project directory in your terminal.
First, you may need to run the scraper to populate the movie dataset(You can also use movies.csv):
python Scraper.py

Run the main application:
python main.py
