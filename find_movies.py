import pandas as pd
import numpy as np


class SortMovies:
    def __init__(self):
        self.movies = pd.read_csv('netflix_edit_non_await.csv', parse_dates=['Premiere_Time'])
        self.movies = self.movies.set_index('Title')
        self.movies.sort_index()
        self.movies_sort = {}


class SortGenre(SortMovies):
    def __init__(self, genre=''):
        super().__init__()
        self.genre = genre
        self.show_info()

    def show_info(self):
        try:
            self.movies_sort = self.movies[self.movies[self.genre] == 1.0][
                ['Genre', 'Language', 'Premiere_Time', 'Runtime_min', 'Runtime_max', 'seasons', 'episode']].to_dict()
        except KeyError:
            self.movies_sort = self.movies[['Genre']].to_dict()


class SortLanguage(SortMovies):
    def __init__(self, language=''):
        super().__init__()
        self.language_ori = language
        self.language = language
        self.show_info()

    def show_info(self):
        if self.language_ori == '':
            self.movies_sort = self.movies[['Language']].to_dict()
        else:
            try:
                self.movies_sort = self.movies[self.movies.Language == self.language][[
                    'Genre', 'Language', 'Premiere_Time', 'Runtime_min', 'Runtime_max', 'seasons', 'episode']].to_dict()
            except KeyError:
                self.movies_sort = self.movies[['Language']].to_dict()


class SortSeason(SortMovies):
    def __init__(self, seasons=0):
        super().__init__()
        self.seasons_ori = seasons
        if seasons == '':
            self.seasons = np.float(10000)
        else:
            self.seasons = np.float(seasons)
        self.show_info()

    def show_info(self):
        if self.seasons_ori == '':
            self.movies_sort = self.movies[['seasons']].to_dict()
        else:
            try:
                self.movies_sort = self.movies[self.movies['seasons'] == self.seasons][[
                    'Genre', 'Language', 'Premiere_Time', 'Runtime_min', 'Runtime_max', 'seasons', 'episode']].to_dict()
            except KeyError:
                self.movies_sort = self.movies[['seasons']].to_dict()


class SortEpisode(SortMovies):
    def __init__(self, episode=0):
        super().__init__()
        self.episode_ori = episode
        if episode == '':
            self.episode = np.float(10000)
        else:
            self.episode = np.float(episode)
        self.show_info()

    def show_info(self):
        if self.episode_ori == '':
            self.movies_sort = self.movies[['episode']].to_dict()
        else:
            try:
                self.movies_sort = self.movies[self.movies.episode == self.episode][[
                    'Genre', 'Language', 'Premiere_Time', 'Runtime_min', 'Runtime_max', 'seasons', 'episode']].to_dict()
            except KeyError:
                self.movies_sort = self.movies[['episode']].to_dict()


class SortFromInput(SortMovies):
    def __init__(self):
        super().__init__()
        self.movies = self.movies.reset_index()
        self.movies_sort = self.movies.set_index('Premiere_Time')
        self.movies_sort = self.movies_sort.sort_index()
        # self.movies_sort.resample('D')
        self.movies_dict = ''

    def show_info(self, type1='', kw1='', type2='', kw2='', kw3=0):
        if kw1 == '':  # genre
            pass
        else:
            try:
                self.movies_sort = self.movies_sort[self.movies_sort[kw1] == 1.0]
            except KeyError:
                pass

        if kw2 == '':  # language
            pass
        else:
            try:
                self.movies_sort = self.movies_sort[self.movies_sort[type2] == kw2]
            except KeyError:
                pass

        if kw3 == ():  # time
            pass
        else:
            t_start, t_end = kw3
            try:
                self.movies_sort = self.movies_sort.loc[t_start:t_end]
            except FutureWarning:
                pass
            except KeyError:
                pass

        self.movies_sort = self.movies_sort.reset_index()
        self.movies_sort = self.movies_sort.set_index('Title')

        self.movies_dict = self.movies_sort[['Genre', 'Language', 'Premiere', 'Runtime', 'Seasons']].to_dict()
        # print(self.movies_dict)


class ListTopic(SortMovies):
    def __init__(self, column_ind):
        super().__init__()

        self.column_unique = list(self.movies[column_ind].unique())
        self.column_unique.sort()


class GroupGenre:
    def __init__(self):
        self.data = pd.read_csv('netflix_edit_non_await.csv')
        self.genre = ['superhero', 'crime', 'science fiction', 'horror', 'fantasy', 'drama', 'comedy', 'sitcom',
                      'romantic', 'thriller', 'musical', 'teen', 'travel', 'sport', 'true crime', 'reality',
                      'competition', 'anime', 'show', 'educational', 'docuseries', 'historical', 'apocalyptic',
                      'coming-of-age', 'detective', 'psychological', 'period', 'anthology', 'series',
                      "children's", 'medieval', 'workplace', 'animation', 'action', 'art', 'supernatural',
                      'mystery', 'mockumentary', 'military', 'survival', 'telenovela', 'dating', 'game']
        self.data_out = {}
        self.count_each_genre()

    def count_each_genre(self):
        for gen in self.genre:
            count = len(self.data[self.data[gen] == 1])
            self.data_out[gen] = count
