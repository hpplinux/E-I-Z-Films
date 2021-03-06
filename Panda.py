import pandas as pd
import numpy as np

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols)

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols)

m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5))

print users

print ratings

print movies


movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)


most_rated = lens.groupby('title').size().order(ascending=False)[:25]
most_rated
lens.title.value_counts()[:25]

movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
movie_stats.head()

