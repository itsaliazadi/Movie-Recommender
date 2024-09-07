import re
import csv
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_movies():
    # Initializing the Chrome WebDriver
    driver = webdriver.Chrome()

    # URL for the IMDb Top 1000 Movies page
    url = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc"

    try:
        driver.get(url)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 

    movies = list()
    last_height = "" # Initializing last_height to track scrolling

    # Loop to scroll and load more movies until all are loaded
    while True:
        # Scrolling to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Waiting for the page to load

        # Getting the new height of the page after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Checking if we've reached the end of the page
        if new_height == last_height:
            # If new height is the same, scroll up a bit and attempt to click the load more button
            driver.execute_script("window.scrollBy(0,-550);")
            time.sleep(2)

            # Try to find and click the "load more" button
            try:
                load_more_button = driver.find_element(By.CSS_SELECTOR, "span.ipc-see-more__text")
                load_more_button.click()
                print("Clicked 'load more' button.")
            except Exception:
                print("The 'load more' button is not available.")
                break

        # Updating last_height for the next iteration
        last_height = new_height

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        movie_tags = soup.find_all("li", class_="ipc-metadata-list-summary-item")
        for movie in movie_tags:
            title = movie.find("h3", class_="ipc-title__text").text
            # Removing the ranking number from the title
            title = re.sub(r'^\d+\.\s*', '', title)
            description_tag = movie.find("div", class_="ipc-html-content-inner-div", role="presentation")

            # Using the extracted description or a default message if not available
            description = description_tag.text if description_tag else "No description available"

            # Creating a dictionary for each movie
            data = {"title": title, "description": description}

            # Checking for duplicates before appending to the list
            if data not in movies:
                movies.append({"title": title, "description": description})

    # Writing the collected movies data to a CSV file
    with open('movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'description']  # Define the header for the CSV file
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)

    print("Data written to movies.csv")

    driver.quit()


