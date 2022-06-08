import random
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from find_movies_sort import *


class WindowApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="news")

        self.column_sort = ['Genre', 'Language', 'seasons', 'episode']
        self.column_sort_graph = ['Genre', 'Language', 'Premiere_Time']
        self.genre_all = ['superhero', 'crime', 'science fiction', 'horror', 'fantasy', 'drama', 'comedy', 'sitcom',
                          'romantic', 'thriller', 'musical', 'teen', 'travel', 'sport', 'true crime', 'reality',
                          'competition', 'anime', 'show', 'educational', 'docuseries', 'historical', 'apocalyptic',
                          'coming-of-age', 'detective', 'psychological', 'period', 'anthology', 'series',
                          "children's", 'medieval', 'workplace', 'animation', 'action', 'art', 'supernatural',
                          'mystery', 'mockumentary', 'military', 'survival', 'telenovela', 'dating', 'game']
        self.premiere_time = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
        self.premiere = {2015: ('2015-01-01', '2015-12-31'), 2016: ('2016-01-01', '2016-12-31'),
                         2017: ('2017-01-01', '2017-12-31'), 2018: ('2018-01-01', '2018-12-31'),
                         2019: ('2019-01-01', '2019-12-31'), 2020: ('2020-01-01', '2020-12-31'),
                         2021: ('2021-01-01', '2021-12-31'), 2022: ('2022-01-01', '2022-12-31')}

        self.first_choice = 'find your movies'
        self.choose_func_choice = self.column_sort[random.randint(0, 3)]
        self.choose_about_choice = self.column_sort[0]
        self.genre_choose = self.genre_all[random.randint(0, 3)]
        self.type_plot = 'line'

        self.create_widget()

    def create_widget(self):
        # create label frame : choose function of this program
        self.window_frame = ttk.LabelFrame(self, text='choose function that you want', labelanchor=tk.N)
        self.window_frame.grid(row=0, column=0, columnspan=2)
        self.columnconfigure(0, weight=1)
        self.choose_func = tk.StringVar()
        self.choice1 = ttk.Radiobutton(self.window_frame, text='find by category', value='find your movies',
                                       variable=self.choose_func, command=self.inside_find_func)
        self.choice1.grid(row=0, column=1, padx=5)
        self.choice2 = ttk.Radiobutton(self.window_frame, text='input your movies', value='input your movies',
                                       variable=self.choose_func, command=self.inside_input_func)
        self.choice2.grid(row=0, column=0, padx=5)
        self.choice3 = ttk.Radiobutton(self.window_frame, text='about Netflix', value='about Netflix',
                                       variable=self.choose_func, command=self.inside_about_func)
        self.choice3.grid(row=0, column=2, padx=5)
        # create reset program
        self.reset_button = tk.Button(self.window_frame, text='reset program', command=self.reset_menu)
        self.reset_button.grid(row=0, column=3)
        # create quit program
        self.quit_button = tk.Button(self.window_frame, text='quit', command=self.quit, fg='#C02200')
        self.quit_button.grid(row=0, column=4)

    def reset_menu(self):
        self.choose_func.set('')
        self.choose_func.set(self.first_choice)
        self.delete_frame()
        self.create_widget()

    def inside_find_func(self):
        self.delete_input()
        self.delete_about()

        self.find_func = ttk.LabelFrame(self, text='find your movies', labelanchor=tk.N)
        self.find_func.grid(row=1, column=0, columnspan=2)
        self.choose_func_menu = ttk.Menubutton(self.find_func, text='topic menu')
        self.choose_func_menu_box = tk.Menu(self.choose_func_menu)
        for topic in self.column_sort:
            self.choose_func_menu_box.add_radiobutton(label=topic, command=lambda x=topic: self.sort_find_func1(x))
        self.choose_func_menu['menu'] = self.choose_func_menu_box
        self.choose_func_menu.grid(row=0, column=0)

        self.to_label = tk.Label(self.find_func, text='->')
        self.to_label.grid(row=0, column=1)

        self.topic_find = tk.StringVar()
        self.topic_find_box = ttk.Combobox(self.find_func, textvariable=self.topic_find)
        self.topic_find_box.grid(row=0, column=2)

        self.show_button = tk.Button(self.find_func, text='show', command=self.show_find_func)
        self.show_button.grid(row=0, column=3)

        self.clear_input = tk.Button(self.find_func, text='clear', command=self.clear_input_find, fg='#C02200')
        self.clear_input.grid(row=0, column=4)

    def sort_find_func1(self, menu):
        self.choose_func_choice = menu
        self.topic_find.set('')
        if menu == 'Genre':
            menu_sort = self.genre_all
        else:
            menu_sort = ListTopic(menu).column_unique
        self.topic_find_box['values'] = menu_sort
        self.topic_find_box['state'] = 'readonly'

    def show_find_func(self):
        self.show_find_func_frame_destroy()
        self.status_destroy()
        self.show_find_func_frame = ttk.LabelFrame(self, text='show', labelanchor=tk.N, width=250, height=200)
        self.show_find_func_frame.grid(row=2, column=0, columnspan=2)
        self.table_find_func = ttk.Treeview(self.show_find_func_frame)
        self.table_find_func.grid(row=0, column=0)
        self.data_sort_from_class()

    def data_sort_from_class(self):
        find = FindAll(self.choose_func_choice, val1=self.topic_find.get())
        data, data_ori = find.find_dict
        if self.choose_func_choice == 'Genre':
            data_movies = list(data_ori.movies_sort.keys())
        else:
            data_movies = list(data_ori.movies_sort)
        data_keys = list(data.keys())
        data_values = list(data.values())

        self.table_find_func['columns'] = data_movies
        self.table_find_func.column('#0', width=120, anchor=tk.N)
        for col in range(len(data_movies)):
            self.table_find_func.column(col, width=65, anchor='c')
            self.table_find_func.heading(col, text=data_movies[col], anchor='c')
        for ind in range(len(data)):
            self.table_find_func.insert('', 'end', iid=ind, text=data_keys[ind], values=data_values[ind])

        count_data_find = len(data_keys)
        self.count_data_find = ttk.Label(self.show_find_func_frame, text=f'It have {count_data_find} data(s).')
        self.count_data_find.grid(row=1, column=0)
        self.update_status_box(count_data_find)

    def clear_input_find(self):
        self.topic_find.set('')
        self.show_find_func_frame_destroy()
        self.count_data_find_destroy()
        self.status_destroy()

    def inside_about_func(self):
        self.delete_find()
        self.delete_input()

        self.about_func = ttk.LabelFrame(self, text='visualize data about movies')
        self.about_func.grid(row=1, column=0, columnspan=2)

        self.choice_about_menu = ttk.Menubutton(self.about_func, text='choose topic to plot')
        self.choice_about = tk.Menu(self.choice_about_menu)
        for ab in self.column_sort_graph:
            self.choice_about.add_radiobutton(label=ab, command=lambda x=ab: self.choose_type_plot(x))
        self.choice_about_menu['menu'] = self.choice_about
        self.choice_about_menu.grid(row=0, column=0)

    def choose_type_plot(self, menu):
        self.type_plot_frame_destroy()

        self.choose_about_choice = menu

        self.type_plot_frame = ttk.LabelFrame(self, text='choose plot type')
        self.type_plot_frame.grid(row=3, column=1)

        self.type_plot = tk.StringVar()
        self.type_plot1 = ttk.Radiobutton(self.type_plot_frame, text='line', value='line',
                                          variable=self.type_plot, command=lambda x='line': self.canvas_about_func1(x))
        self.type_plot3 = ttk.Radiobutton(self.type_plot_frame, text='pie', value='pie',
                                          variable=self.type_plot, command=lambda x='pie': self.canvas_about_func1(x))
        self.type_plot4 = ttk.Radiobutton(self.type_plot_frame, text='bar', value='bar',
                                          variable=self.type_plot, command=lambda x='bar': self.canvas_about_func1(x))
        self.type_plot5 = ttk.Radiobutton(self.type_plot_frame, text='barh', value='barh',
                                          variable=self.type_plot, command=lambda x='barh': self.canvas_about_func1(x))
        if self.choose_about_choice in ['Premiere_Time']:
            self.type_plot1.grid(row=0, column=0, stick=tk.W)
        if self.choose_about_choice in ['Language']:
            self.type_plot3.grid(row=2, column=0, stick=tk.W)
        if self.choose_about_choice in ['Language', 'seasons', 'episode']:
            self.type_plot4.grid(row=3, column=0, stick=tk.W)
        if self.choose_about_choice in ['Genre', 'Language', 'seasons', 'episode']:
            self.type_plot5.grid(row=4, column=0, stick=tk.W)

    def canvas_about_func1(self, plot_type):
        self.show_about_graph_destroy()
        self.movies_for_plot = pd.read_csv('netflix_edit_non_await.csv', parse_dates=['Premiere_Time'])
        self.show_about_graph = ttk.LabelFrame(self, text='graph', labelanchor=tk.N)
        self.show_about_graph.grid(row=3, column=0)
        self.fig_canvas = Figure(figsize=(9, 9))
        self.axes_canvas = self.fig_canvas.add_subplot()

        self.fig_show = FigureCanvasTkAgg(self.fig_canvas, master=self.show_about_graph)
        self.fig_show.get_tk_widget().grid(row=0, column=0, sticky='news')

        self.plot_about_func()

    def plot_about_func(self):
        self.axes_canvas.clear()
        if self.choose_about_choice == 'Premiere_Time':
            text_self = self.movies_for_plot.Premiere_Time.dt.year
            self.movies_for_plot.groupby(text_self).count()['Title'].plot(kind='line', ax=self.axes_canvas,
                                                                          ylabel='movie(s)', title='Premiere_Time')
        elif self.choose_about_choice == 'Genre':
            data_dict = GroupGenre().data_out
            self.axes_canvas.barh(list(data_dict.keys()), data_dict.values())
            self.axes_canvas.set(xlabel='count movies', title='Genre')
        elif self.type_plot.get() == 'pie':
            self.movies_for_plot[self.choose_about_choice].value_counts().plot(kind='pie', ax=self.axes_canvas,
                                                                               autopct='%1.1f%%', ylabel='',
                                                                               title=self.choose_about_choice)
        elif self.type_plot.get() == 'bar':
            self.movies_for_plot[self.choose_about_choice].value_counts().plot(kind='bar', ax=self.axes_canvas,
                                                                               ylabel='count',
                                                                               title=self.choose_about_choice)
        elif self.type_plot.get() == 'barh':
            self.movies_for_plot[self.choose_about_choice].value_counts().plot(kind='barh', ax=self.axes_canvas,
                                                                               title=self.choose_about_choice)
        else:
            pass
        self.axes_canvas.set()
        self.fig_show.draw()

    def inside_input_func(self):
        self.find_func_destroy()
        self.show_find_func_frame_destroy()
        self.status_destroy()

        self.about_func_destroy()
        self.show_about_graph_destroy()
        self.type_plot_frame_destroy()
        self.show_about_graph_destroy()
        self.status_destroy()

        self.input_func = ttk.LabelFrame(self, text='find your movies(selected)', labelanchor=tk.N)
        self.input_func.grid(row=1, column=0, columnspan=2)

        self.input_func_genre = ttk.LabelFrame(self.input_func, text='choose genre')
        self.input_func_genre.grid(row=0, column=0)
        self.input_func_genre_str = tk.StringVar()
        self.input_func_genre_choose = ttk.Combobox(self.input_func_genre, textvariable=self.input_func_genre_str)
        self.input_func_genre_choose['values'] = self.genre_all
        self.input_func_genre_choose['state'] = 'readonly'
        self.input_func_genre_choose.grid(row=0, column=0)

        self.input_func_language = ttk.LabelFrame(self.input_func, text='choose language')
        self.input_func_language.grid(row=0, column=1)
        self.input_func_language_str = tk.StringVar()
        self.input_func_language_choose = ttk.Combobox(self.input_func_language,
                                                       textvariable=self.input_func_language_str)
        self.input_func_language_choose['values'] = ListTopic('Language').column_unique
        self.input_func_language_choose['state'] = 'readonly'
        self.input_func_language_choose.grid(row=0, column=0)

        self.input_func_time = ttk.LabelFrame(self.input_func, text='choose premiere time')
        self.input_func_time.grid(row=0, column=2)
        self.input_func_time_int = tk.DoubleVar()
        self.input_func_time_choose = ttk.Combobox(self.input_func_time, textvariable=self.input_func_time_int)
        self.input_func_time_choose['values'] = self.premiere_time
        self.input_func_time_choose['state'] = 'readonly'
        self.input_func_time_int.set(self.premiere_time[-1])
        self.input_func_time_choose.grid(row=0, column=0)

        self.clear_input_func = tk.Button(self.input_func, text='reset', command=self.reset_input_func)
        self.clear_input_func.grid(row=1, column=1, sticky=tk.W)

        self.input_func_button = tk.Button(self.input_func, text='show', command=self.before_show_input_func)
        self.input_func_button.grid(row=1, column=1, sticky=tk.E)

    def reset_input_func(self):
        self.input_func_genre_str.set('')
        self.input_func_language_str.set('')
        self.input_func_time_int.set(self.premiere_time[-1])
        self.show_input_func_frame_destroy()
        self.status.destroy()

    def before_show_input_func(self):
        self.show_input_func_frame_destroy()
        self.status_destroy()

        sort_input = SortFromInput()
        sort_input.show_info(type1='Genre', kw1=self.input_func_genre_str.get(), type2='Language',
                             kw2=self.input_func_language_str.get(), kw3=self.premiere[self.input_func_time_int.get()])
        data_dict = sort_input.movies_dict
        self.data_change_dict = new_dict_edit(data_dict)

        self.show_input_func_frame = ttk.LabelFrame(self, text='show', labelanchor=tk.N, width=250, height=200)
        self.show_input_func_frame.grid(row=3, column=0, columnspan=2)
        self.table_input_func = ttk.Treeview(self.show_input_func_frame)
        self.table_input_func.grid(row=0, column=0)

        self.data_sort_to_input_func()

    def data_sort_to_input_func(self):
        column_name = ['Genre', 'Language', 'Premiere', 'Runtime', 'Seasons']
        data_keys = list(self.data_change_dict.keys())
        data_values = list(self.data_change_dict.values())

        self.table_input_func['columns'] = column_name
        self.table_input_func.column('#0', width=120, anchor=tk.N)
        for col in range(len(column_name)):
            self.table_input_func.column(col, width=65, anchor='c')
            self.table_input_func.heading(col, text=column_name[col], anchor='c')
        for ind in range(len(self.data_change_dict)):
            self.table_input_func.insert('', 'end', iid=ind, text=data_keys[ind], values=data_values[ind])

        count_data_input = len(data_keys)
        self.count_data_input = ttk.Label(self.show_input_func_frame, text=f'It have {count_data_input} data(s).')
        self.count_data_input.grid(row=1, column=0)
        self.update_status_box(count_data_input)

    def clear_input_func_table(self):
        self.topic_find.set('')
        self.show_find_func_frame_destroy()
        self.count_data_find_destroy()

    def delete_find(self):
        self.find_func_destroy()
        self.show_find_func_frame_destroy()
        self.status_destroy()

    def delete_about(self):
        self.about_func_destroy()
        self.show_about_graph_destroy()
        self.type_plot_frame_destroy()
        self.show_about_graph_destroy()
        self.status_destroy()

    def delete_input(self):
        self.input_func_destroy()
        self.show_input_func_frame_destroy()
        self.status_destroy()

    def delete_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    # single delete
    # find func
    def find_func_destroy(self):
        try:
            self.find_func.destroy()
        except AttributeError:
            pass

    def show_find_func_frame_destroy(self):
        try:
            self.show_find_func_frame.destroy()
        except AttributeError:
            pass

    def count_data_find_destroy(self):
        try:
            self.count_data_find.destroy()
        except AttributeError:
            pass

    # about func
    def about_func_destroy(self):
        try:
            self.about_func.destroy()
        except AttributeError:
            pass

    def type_plot_frame_destroy(self):
        try:
            self.type_plot_frame.destroy()
        except AttributeError:
            pass

    def show_about_graph_destroy(self):
        try:
            self.show_about_graph.destroy()
        except AttributeError:
            pass
        try:
            self.fig_show.get_tk_widget().destroy()
        except AttributeError:
            pass

    # input func
    def input_func_destroy(self):
        try:
            self.input_func.destroy()
        except AttributeError:
            pass

    def show_input_func_frame_destroy(self):
        try:
            self.show_input_func_frame.destroy()
        except AttributeError:
            pass

    def update_status_box(self, num_check):
        self.status = ttk.LabelFrame(self, text='loading status...', labelanchor=tk.N)
        self.status.grid(row=4, column=0)
        if num_check == 0:
            label_text = "data not found"
        else:
            label_text = "loading complete"
        self.text_status = ttk.Label(self.status, text=label_text)
        self.text_status.grid(row=0, column=0)

    def status_destroy(self):
        try:
            self.status.destroy()
        except AttributeError:
            pass

    def update_func(self):
        delay = 1000
        self.after(delay, self.update_func)

    def run(self):
        self.update_func()
        self.parent.mainloop()
