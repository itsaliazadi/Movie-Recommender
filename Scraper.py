import re
import csv
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_movies():

    driver = webdriver.Chrome()

    url = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc"

    try:
        driver.get(url)
    except Exception as e:
        print(f"An error occurred: {e}")

    movies = list()
    last_height = ""

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            driver.execute_script("window.scrollBy(0,-550);")
            time.sleep(2)

            try:
                load_more_button = driver.find_element(By.CSS_SELECTOR, "span.ipc-see-more__text")
                load_more_button.click()
                print("Clicked 'load more' button.")
            except Exception:
                print("The 'load more' button is not available.")
                break

        last_height = new_height

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        movie_tags = soup.find_all("li", class_="ipc-metadata-list-summary-item")
        for movie in movie_tags:
            title = movie.find("h3", class_="ipc-title__text").text
            title = re.sub(r'^\d+\.\s*', '', title)
            description_tag = movie.find("div", class_="ipc-html-content-inner-div", role="presentation")
            
            description = description_tag.text if description_tag else "No description available"

            data = {"title": title, "description": description}

            if data not in movies:
                movies.append({"title": title, "description": description})


    with open('movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)

    print("Data written to movies.csv")

    driver.quit()

