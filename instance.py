import fresh_tomatoes

import media


inception = media.Movie("Inception", "A mind blowing drama about multi-layered dreams", "http://www.impawards.com/2010/posters/inception_xlg.jpg", "https://www.youtube.com/watch?v=66TuSJo4dZM")

the_insider = media.Movie("The insider", "The story of the man who blew the whistle on a cigarete major", "https://lh3.googleusercontent.com/bYP6OVjfskfh3uW-pvQiyoABaGXjiWA92Ic8Rxl2lqmczZ0mUohIjtv0req_YJjLA3zs=w300", "https://www.youtube.com/watch?v=5rkvxi5hdbA")

wild_tales = media.Movie("Wild tales", "Six stories about men & women going wild", "https://images-na.ssl-images-amazon.com/images/M/MV5BNzAzMjA1ODAxOV5BMl5BanBnXkFtZTgwODg4NTQzNDE@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=_I0EamOH_LA")

as_good_as_it_gets = media.Movie("As good as it gets", "An apalling misanthrope manages to find love", "https://images-na.ssl-images-amazon.com/images/M/MV5BNWMxZTgzMWEtMTU0Zi00NDc5LWFkZjctMzUxNDIyNzZiMmNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=rrRl2QQKkI8")

the_hunt = media.Movie("The hunt", "The lie is spreading", "https://upload.wikimedia.org/wikipedia/en/thumb/4/44/The_Hunt_%282012_film%29.jpg/220px-The_Hunt_%282012_film%29.jpg", "https://www.youtube.com/watch?v=9Umv4CyxTdg")

invincible = media.Movie("Invincible", "Dreams are not lived on the sidelines", "https://upload.wikimedia.org/wikipedia/en/f/f9/Invincible_movie.jpg", "https://www.youtube.com/watch?v=Aux_hRJYED8")

#print (inception.story)

#inception.show_trailer()

movies = [inception, the_insider, wild_tales, as_good_as_it_gets, the_hunt, invincible]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__name__)
#print(media.Movie.__module__)
