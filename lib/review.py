# - `Review __init__()`
#   - Reviews should be initialized with a customer, restaurant, and a rating (a number)
# - `Review rating()`
#   - returns the rating for a restaurant.
# - `Review all()`
#   - returns all of the reviews
# from customer import Customer
class Review:
    all_reviews_1 = {}
    count = 0
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.count +=1
        
        Review.all_reviews_1[Review.count] = restaurant,rating,customer
    
    def rating(self):
        return self.rating
    @classmethod
    def all(cls):
        return [value for value in cls.all_reviews_1.items()]
    
# Review
# - `Review customer()`
#   - returns the customer object for that review
#   - Once a review is created, should not be able to change the customer
# - `Review restaurant()`
#   - returns the restaurant object for that given review
#   - Once a review is created, should not be able to change the restaurant
    def customer(self):
        return self._customer
    def restaurant(self):
        return self._restaurant

# customer1 = Customer('JAN','KIMUTAI')
# customer2 = Customer('ALVIN','OMBITO')
# customer3 = Customer('DAN','NJOKA')


        

review1 = Review('JAN','MAGGIES',9)
review4 = Review('ALVIN','MAGGIES',8)
review2 = Review('SHALLON','WESTON',7)
review3 = Review('LABAN','WESTON',7)
review5 = Review('CYNTHIA','WESTON',1.4)
review6 = Review('NICOLE','WESTON',7)


# print(Review.all_reviews_1)
