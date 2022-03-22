"""Restaurant rating lister."""
#create a function
#open the file reads the ratings and restaurants
#stores the info in a dictionary, and spits them
#alphabetical order

# prompt the user for a restaurant name
# prompt for restaurant score
# store new restaurant + ratings in dictionary 
# print all in alph order 

from re import S


def get_restaurant_and_ratings(file_name):
    file = open(file_name)
    restaurants_and_ratings = {}
    
    
    
    restaurant_input = input("What restaurant would you like to rate?: ")
    # rating_input = input("What rating would you like to give?(1-5): ")
    rating_input = ":" + input("What rating would you like to give?(1-5): ")
    restaurant_and_rating_input = [restaurant_input + rating_input]

    sort_file = sorted(file) + restaurant_and_rating_input
    sorted_file = sorted(sort_file)
    # print(sorted_file)
    
    for line in sorted_file:
        line = line.rstrip().split(":") # order matters! 
        restaurant = line[0]
        rating = line[1]
        restaurants_and_ratings[restaurant] = restaurants_and_ratings.get(restaurant, 0) + int(rating)


    # restaurants_and_ratings[restaurant_input] = restaurants_and_ratings.get(restaurant_input, int(rating_input)) 
    

    
    for key, value in restaurants_and_ratings.items():
        print(f'{key} is rated at {value}.')
        
    file = file.close()
    
    

get_restaurant_and_ratings("scores.txt")