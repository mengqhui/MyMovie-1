"""
Module to display movie object, attributes, and instances
"""

import webbrowser


class Movie():
        """
        Class object stores movie related information
        """
        def __init__(
                self,
                movie_title,
                movie_storyline,
                poster_image,
                trailer_youtube):
                """
                Initialize instances of class Movie
                """
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
                """
                Initializing instance for opening the youtube video
                """
                webbrowser.open(self.trailer_youtube_url)
