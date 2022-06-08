from find_movies import *


class FindAll:
    def __init__(self, topic, val1=''):
        self.select = {
            'Genre': SortGenre,
            'Language': SortLanguage,
            'seasons': SortSeason,
            'episode': SortEpisode
        }
        self.topic = topic
        self.val = val1
        self.find_dict = 0

        self.find_sort_class()

    def find_sort_class(self):
        self.find_dict = edit_find_genre(self.select[self.topic](self.val)), self.select[self.topic](self.val)


def edit_find_genre(t_dict):
    get_dict_sort = t_dict.movies_sort
    get_values = list(get_dict_sort.values())
    try:
        get_values[0].keys()
    except AttributeError:
        get_values = get_dict_sort
    new_dict = {}
    for i in range(len(list(get_values))):
        try:
            values = list(get_values[i].keys())
        except KeyError:
            return get_values
        else:
            keys = list(get_values[i].values())
            for j in range(len(values)):
                if values[j] not in new_dict:
                    new_dict[values[j]] = []
                dict_in = new_dict[values[j]]
                dict_in.append(keys[j])
                new_dict[values[j]] = dict_in
    return new_dict


def new_dict_edit(t_dict):
    dict_keys, dict_values = list(t_dict.keys()), list(t_dict.values())
    new_dict = {}
    for i in range(len(list(dict_values))):
        try:
            values = list(dict_values[i].keys())
        except KeyError:
            return dict_values
        else:
            keys = list(dict_values[i].values())
            for j in range(len(values)):
                if values[j] not in new_dict:
                    new_dict[values[j]] = []
                dict_in = new_dict[values[j]]
                dict_in.append(keys[j])
                new_dict[values[j]] = dict_in
    return new_dict
