"""Restaurant rating lister."""
#create a function
#open the file reads the ratings and restaurants
#stores the info in a dictionary, and spits them
#alphabetical order

def get_restaurant_and_ratings(file_name):
    file = open(file_name)
    restaurants_and_ratings = {}
    sorted_file = sorted(file)
    # print(sorted_file)
    for line in sorted_file:
        line = line.rstrip().split(":") # order matters! 
        restaurant = line[0]
        rating = line[1]
        restaurants_and_ratings[restaurant] = restaurants_and_ratings.get(restaurant, 0) + int(rating)
  
    
    for key, value in restaurants_and_ratings.items():
        print(f'{key} is rated at {value}.')
    file = file.close()

get_restaurant_and_ratings("scores.txt")