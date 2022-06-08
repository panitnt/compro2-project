### this file already update to csv file
### don't run it again
import copy

import pandas as pd


data = pd.read_csv('../originalNedit_data/netflix_genre.csv')
# Language,Premiere,Runtime,Seasons
# language
data_lan = data['Language']

for i in range(len(data_lan)):
    data_lan[i] = ''
data['Language'] = data_lan
data.to_csv('netflix_genre.csv', index=False)
# premiere
data_pre = data['Premiere']

for i in range(len(data_pre)):
    data_pre[i] = ''
data['Premiere'] = data_pre
data.to_csv('netflix_genre.csv', index=False)
# runtime
data_run = data['Runtime']

for i in range(len(data_run)):
    data_run[i] = ''
data['Runtime'] = data_run
data.to_csv('netflix_genre.csv', index=False)
# Seasons
data_sea = data['Seasons']

for i in range(len(data_sea)):
    data_sea[i] = ''
data['Seasons'] = data_sea
data.to_csv('netflix_genre.csv', index=False)

data = pd.read_csv('../netflix_edit_non_await.csv')

for typo in ['apocalyptic', 'coming-of-age', 'detective', 'psychological', 'period', 'anthology', 'series',
          "children's", 'medieval', 'workplace', 'animation', 'action', 'art', 'supernatural', 'mystery',
          ' mockumentary', 'military', 'survival', 'telenovela', 'dating', 'game']:
    data_new = copy.copy(data['horror'])
    for i in range(len(data_new)):
        data_new[i] = ''
    data[typo] = data_new
    data.to_csv('netflix_edit_non_await.csv', index=False)


def check(genre, word):
    word = str(word).lower()
    if genre in word:
        return True
    return False


for j in ['apocalyptic', 'coming-of-age', 'detective', 'psychological', 'period', 'anthology', 'series',
          "children's", 'medieval', 'workplace', 'animation', 'action', 'art', 'supernatural', 'mystery',
          ' mockumentary', 'military', 'survival', 'telenovela', 'dating', 'game']:
    data_genre = pd.read_csv('../originalNedit_data/netflix_genre.csv')
    data_change = copy.copy(data_genre['Genre'])
    change = j

    for i in range(len(data_change)):
        if check(change, data_change[i]):
            data_change[i] = 1
        else:
            data_change[i] = ''

    data_genre[change] = data_change
    data_genre.to_csv('netflix_genre.csv', index=False)

data = pd.read_csv('../netflix_edit_non_await.csv')
data_genre = pd.read_csv('../originalNedit_data/netflix_genre.csv')
data_sth = copy.copy(data['Genre'])
for genre in ['superhero', 'crime', 'science fiction', 'horror', 'fantasy', 'drama', 'comedy', 'sitcom', 'romantic',
              'thriller', 'musical', 'teen', 'travel', 'sport', 'true crime', 'reality', 'competition', 'anime', 'show',
              'educational', 'docuseries', 'historical']:
    for i in range(len(data_sth)):
        data_sth[i] = data_genre[genre][i]
    data[genre] = data_sth
    data.to_csv('netflix_edit.csv', index=False)

data = pd.read_csv('../netflix_edit_non_await.csv')
data_genre = pd.read_csv('../originalNedit_data/netflix_genre.csv')
data_sth = copy.copy(data['Genre'])
for genre in ['apocalyptic', 'coming-of-age', 'detective', 'psychological', 'period', 'anthology', 'series',
              "children's", 'medieval', 'workplace', 'animation', 'action', 'art', 'supernatural', 'mystery',
              ' mockumentary', 'military', 'survival','telenovela','dating','game']:
    for i in range(len(data_sth)):
        data_sth[i] = data_genre[genre][i]
    data[genre] = data_sth
    data.to_csv('netflix_edit_non_await.csv', index=False)


