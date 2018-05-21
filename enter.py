#!/usr/bin/env python
import media
import fresh_tomatoes

AGV = media.Movie("Agnatavasi", "family", "https://bit.ly/2rXfjO0",
                  "https://www.youtube.com/watch?v=knaCsR6dr58")

ranga = media.Movie("Rangastalam", "Family", "https://bit.ly/2IyLI8z",
                    "https://www.youtube.com/watch?v=sueMmTm-M4Y")

bharat = media.Movie("Bharat nae nenu", "political", "https://bit.ly/2s0hosm",
                     "https://www.youtube.com/watch?v=KMWS5y2gZ6E")

gang = media.Movie("Gang", "comedy", "https://bit.ly/2IZxA85",
                   "https://www.youtube.com/watch?v=vWD6kUP9RTY")

jhms = media.Movie("Jab harry met segal", "comedy", "https://bit.ly/2IRCCTZ",
                   "https://www.youtube.com/watch?v=W5MZevEH5Ns")

movies = [AGV, ranga, bharat, gang, jhms]
fresh_tomatoes.open_movies_page(movies)
