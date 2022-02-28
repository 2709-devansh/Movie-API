import csv
import pandas as pd

df = pd.read_csv('final_csv.csv')

C = df['vote_average'].mean()
m = df['vote_count'].quantile(0.9)
q_movies = df.copy().loc[df['vote_count'] >= m]

def calc_weighted_rating(x, m = m, C = C):
    v = x['vote_count']
    R = x['vote_average']
    return(
        ((v/(v+m))*R)+((m/(v+m))*C)
    )

q_movies['score'] = q_movies.apply(calc_weighted_rating, axis = 1)
q_movies = q_movies.sort_values('score', ascending = False)

output = q_movies[['original_title', 'vote_count', 'vote_average', 'score', 'poster_link', 'release_date', 'runtime', 'overview']].head(10).values.tolist()