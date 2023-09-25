# Restaurant
# - `Restaurant __init__()`
#   - Restaurants should be initialized with a name, as a string
# - `Restaurant name()`
#   - returns the restaurant's name
#   - should not be able to change after the restaurant is created
from review import Review
class Restaurant():
    
    def __init__(self,restaurant_name):
        self._restaurant_name = restaurant_name
    def name(self):
        return self._restaurant_name
    def restaurant_reviews(self):
        reviews = []
        for key,value in Review.all_reviews_1.items():
            if  value[0]== self._restaurant_name:
                reviews.append(value[1])
        return reviews
    def customer_reviews(self):
        customer_revs = []
        for key,value in Review.all_reviews_1.items():
            if value[0] == self._restaurant_name:
                customer_revs.append(value[2])
        return customer_revs 
    @classmethod
    def all_reviews(cls):
        return cls.reviews
res = Restaurant('MAGGIES')
res1 = Restaurant('WESTON')
# Returns a **unique** list of all customers who have reviewed a particular restaurant.
print('LIST OF ALL CUSTOMERS REVIEWS FOR WESTON: ',res1.customer_reviews())
print('LIST OF ALL CUSTOMERS REVIEWS FOR MAGGIES: ',res.customer_reviews())
# Returns a list of all reviews for that restaurant
print('LIST OF REVIEWS FOR MAGGIES: ',res.restaurant_reviews())
print('LIST OF REVIEWS FOR WESTON :',res1.restaurant_reviews())




