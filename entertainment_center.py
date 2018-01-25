import fresh_tomatoes
import media

Goldeneye = media.Movie("Goldeneye",
                        "James Bond teams up with the lone survivor of a destroyed Russian research center to stop the hijacking of a nuclear space weapon",
                        "https://fontmeme.com/images/007-golden-eye-Poster.jpg",
                        "https://www.youtube.com/watch?v=HHFXthl5IJo",)

Die_Another_Day = media.Movie("Die Another Day",
                            "Bond circles the world in his quest to unmask a traitor, and prevent a war of catastrophic proportions",
                            "https://fontmeme.com/images/Die-Another-Day-Poster.jpg",
                            "https://www.youtube.com/watch?v=VSzixW0KQcc",)

Casino_Royale = media.Movie("Casino Royale",
                        "Armed with a license to kill, Secret Agent James Bond sets out on his first mission as 007",
                        "https://mrmoviefiend.files.wordpress.com/2010/06/casino-royale-poster-5.jpg",
                        "https://www.youtube.com/watch?v=GV_18deeAXk")

movies = [Goldeneye, Die_Another_Day, Casino_Royale]
fresh_tomatoes.open_movies_page(movies)
