import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('final_csv.csv')
df = df[df['compare_criterias'].notna()]

count = CountVectorizer(stop_words = 'english')
count_matrix = count.fit_transform(df['compare_criterias'])
similarity = cosine_similarity(count_matrix, count_matrix)
indices = pd.Series(df.index, index = df['original_title'])

def get_recommendations(title, cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['original_title'].iloc[movie_indices].values.tolist()