import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
ratings = [b.text for b in soup.select('td.imdbRating strong')]

for idx in range(0, len(movies)):
    movie_string = movies[idx].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(idx))+1:-7]
    print(f"{idx+1}: {movie_title}, Rating: {ratings[idx]}")
