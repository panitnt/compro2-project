### this file already update to csv file
### don't run it again
import pandas as pd

# change to timestamp : premiere
data1 = pd.read_csv('../originalNedit_data/netflix_edit.csv')
data_time = data1['Premiere']


def edit_time(info):
    if str(info) == 'nan':
        return ''
    if str(info) == 'Awaiting release':
        return ''
    try:
        list_split = info.split(' ')
    except AttributeError:
        return info
    if len(list_split) != 3:
        return info
    month, date, year = info.split(' ')
    date = str(date)[:-1]
    if len(date) == 1:
        date = '0' + date
    year = str(year)[0:4]
    month_num = 0
    if month == 'January':
        month_num = '01'
    elif month == 'February':
        month_num = '02'
    elif month == 'March':
        month_num = '03'
    elif month == 'April':
        month_num = '04'
    elif month == 'May':
        month_num = '05'
    elif month == 'June':
        month_num = '06'
    elif month == 'July':
        month_num = '07'
    elif month == 'August':
        month_num = '08'
    elif month == 'September':
        month_num = '09'
    elif month == 'October':
        month_num = '10'
    elif month == 'November':
        month_num = '11'
    elif month == 'December':
        month_num = '12'
    return f'{year}-{month_num}-{date}'


for i in range(len(data_time)):
    data_time[i] = edit_time(data_time[i])

data1['Premiere'] = data_time
data1['Premiere_Time'] = pd.to_datetime(data1['Premiere'], format='%Y-%m-%d')
data1.to_csv('netflix_edit.csv', index=False)

# change to time stamp : runtimes
data2 = pd.read_csv('../originalNedit_data/netflix_edit.csv')
data_runtime = data2['Runtime']


def edit_runtime(info):
    if str(info) == 'nan':
        return 0, 0
    if str(info) == 'Awaiting release':
        return 0, 0
    if str(info) == 'TBA':
        return 0, 0
    try:
        list_split = info.split('–')
    except AttributeError:
        return float(info[:-4])
    if len(list_split) != 2:
        return str(info)[:-4]
    minutes1, minutes2 = list_split
    minutes1 = str(minutes1)
    minutes2 = str(minutes2)[:-4]
    return float(minutes1), float(minutes2)


data2['Runtime_min'] = data_runtime
data2['Runtime_max'] = data_runtime
data_time_min = data2['Runtime_min']
data_time_max = data2['Runtime_max']

for j in range(len(data_runtime)):
    try:
        min_i, max_i = edit_runtime(data_runtime[j])
    except ValueError:
        min_i, max_i = 0, 0
    try:
        data_time_min[j] = float(min_i)
    except ValueError:
        data_time_min[j] = min_i
    data_time_max[j] = float(max_i)
data2['Runtime_min'] = data_time_min
data2['Runtime_max'] = data_time_max
data2.to_csv('netflix_edit.csv', index=False)

# split seasons and episode
data3 = pd.read_csv('../originalNedit_data/netflix_edit.csv')
data_seasons = data3['Seasons']


def edit_seasons(info):
    if info == 'nan':
        return 0, 0
    if info == 'Awaiting release':
        return 0, 0
    if info == 'TBA':
        return 0, 0
    try:
        label_split = info.split(', ')
    except AttributeError:
        return 0, 0
    if label_split == [info]:
        num, unit = label_split[0].split(' ')
        if unit == 'season':
            return num, 0
        else:
            return 0, unit
    num_sea, unit_sea = label_split[0].split(' ')
    num_epi, unit_epi = label_split[1].split(' ')
    return float(num_sea), float(num_epi)


data3['seasons'] = data_seasons
data3['episode'] = data_seasons
data_sea_seasons = data3['seasons']
data_sea_episode = data3['episode']

for k in range(len(data_seasons)):
    try:
        sea, epi = edit_seasons(data_seasons[k])
    except ValueError:
        sea, epi = edit_seasons(data_seasons[k]), ''
    try:
        data_sea_seasons[k] = float(sea)
    except ValueError:
        data_sea_seasons[k] = sea
    try:
        data_sea_episode[k] = float(epi)
    except ValueError:
        data_sea_episode[k] = epi

data3['seasons'] = data_sea_seasons
data3['episode'] = data_sea_episode
data3.to_csv('netflix_edit.csv', index=False)
