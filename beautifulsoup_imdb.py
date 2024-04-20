import imdb

ia=imdb.IMDb()
searh= ia.get_top250_movies()
for movies in searh:
    print(movies)