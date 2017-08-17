import media
import fresh_tomatoes

# instantiate movies
the_matrix = media.Movie("The Matrix",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=a94b1yZOBes",
                         "R")
spiderman_homecoming = media.Movie("Spiderman: Homecoming",
                                   "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                                   "https://www.youtube.com/watch?v=U0D3AOldjMU",
                                   "PG-13")
forrest_gump = media.Movie("Forrest Gump",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                            "https://www.youtube.com/watch?v=bLvqoHBptjg",
                            "PG-13")
the_lion_king = media.Movie("The Lion King",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_poster.jpg/220px-The_Lion_King_poster.jpg",
                             "https://www.youtube.com/watch?v=ba6pMRHte_E",
                             "G")
inception = media.Movie("Inception",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=d3A3-zSOBT4",
                         "PG-13")
the_dark_knight = media.Movie("The Dark Knight",
                               "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                               "https://www.youtube.com/watch?v=kmJLuwP3MbY",
                               "PG-13")
v_for_vendetta = media.Movie("V for Vendetta",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Vforvendettamov.jpg/220px-Vforvendettamov.jpg",
                              "https://www.youtube.com/watch?v=qxyUl9M_7vc",
                              "R")
captain_america_civl_war = media.Movie("Captain America: Civil War",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg",
                                       "https://www.youtube.com/watch?v=mKScYV9jzG0",
                                       "PG-13")
the_imitation_game = media.Movie("The Imitation Game",
                                 "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",
                                 "https://www.youtube.com/watch?v=T40uC-SznNs",
                                 "PG-13")

# store all movies in array for fresh_tomatoes
movies = [the_matrix, the_lion_king, inception, the_imitation_game, the_dark_knight,
          v_for_vendetta, spiderman_homecoming, captain_america_civl_war]

# open webpage with movie tiles
fresh_tomatoes.open_movies_page(movies)
