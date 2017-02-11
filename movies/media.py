#-*- coding: UTF-8 -*- 

import webbrowser

class Movie():
    '''一个打印电影的程序'''
    Valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youku):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youku_url = trailer_youku

    def show_trailer(self):
        webbrowser.open(self.trailer_youku_url)