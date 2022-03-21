"""Restaurant rating lister."""
#create a function
#open the file reads the ratings and restaurants
#stores the info in a dictionary, and spits them
#alphabetical order

def get_restaurant_and_ratings(file_name):
    file = open(file_name)
    restaurants_and_ratings = {}
    for line in file:
        line = line.rstrip()
        line = line.split(":")
        restaurant = line[0]
        rating = line[1]
        restaurants_and_ratings[restaurant] = restaurants_and_ratings.get(restaurant, 0) + int(rating)
    print(restaurants_and_ratings)
    

get_restaurant_and_ratings("scores.txt")