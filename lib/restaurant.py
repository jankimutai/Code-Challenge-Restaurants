# Restaurant
# - `Restaurant __init__()`
#   - Restaurants should be initialized with a name, as a string
# - `Restaurant name()`
#   - returns the restaurant's name
#   - should not be able to change after the restaurant is created

class Restaurant():
    our_reviews = []
    def __init__(self,restaurant_name):
        self._restaurant_name = restaurant_name
    def name(self):
        return self._restaurant_name
# Restaurant
# - `Restaurant reviews()`
#   - returns a list of all reviews for that restaurant
# - `Restaurant customers()`
#   - Returns a **unique** list of all customers who have reviewed a particular restaurant.
    def review_restaurant():
        pass
    def customer_review():
        pass

restaurant1 = Restaurant('MAGGIES')
restaurant2 = Restaurant('CHICKEN INN')
restaurant3 = Restaurant('PIZZA INN')

print(restaurant1.name())
print(restaurant2.name())
print(restaurant3.name())
