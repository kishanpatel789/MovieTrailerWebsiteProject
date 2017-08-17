class Movie():
    """This class provides a way to store movie-related information."""
    def __init__(self, movie_title, poster_image, trailer_youtube, movie_rating):
        """The inputs are the movie's title, the URL of the movie's poster,
        the URL of the movie's trailer, and the movie's rating."""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        
