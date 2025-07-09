import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('h2 > strong') #markdown list of titles with direct strong child inside h2 tags
# titles = soup.select('h2 strong') #markdown list of all titles with strong tags inside h2 tags (in general)

movie_list = []
movie_top = []


for movie in titles[::-1]:
    cleaned_movie = movie.get_text(strip=True)
    movie_list.append(cleaned_movie.split(') ')[1])
    movie_top.append(cleaned_movie.split(') ')[0])

total_movies = len(movie_list)
print (f"DONE!!\nTotal movies: {total_movies}")

# Save to CSV
with open('top_movies.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Rank', 'Movie_Title'])
    for rank, title in zip(movie_top, movie_list):
        writer.writerow([rank, title])







