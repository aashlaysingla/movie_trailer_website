import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","a story of a boy and his childhood friend and a toy","https://static.webshopapp.com/shops/025084/files/050611196/mural-toy-story-disney-wallpaper-poster.jpg","www.youtube.com/watch?v=tN1A2mVnrOM")

sherlock_holmes = media.Movie("Sherlock_Holmes","a spy movie","https://resizing.flixster.com/IrsRkzzvC5d7j0lf4Po-9AzVzT8=/206x305/v1.bTsxMTE2NjcyODtqOzE3OTQ5OzEyMDA7ODAwOzEyMDA","https://www.youtube.com/watch?v=Egcx63-FfTE")

fast_and_furious_8 = media.Movie("fast and furious 8","an action movie","https://in.bmscdn.com/iedb/movies/images/website/poster/large/et00041156_20-04-2016_04-46-35.jpg","https://www.youtube.com/watch?v=uisBaTkQAEs")

movies = [fast_and_furious_8,sherlock_holmes,toy_story]

fresh_tomatoes.open_movies_page(movies)

#print(toy_story.storyline)
#toy_story.show_trailer()

