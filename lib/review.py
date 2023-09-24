# - `Review __init__()`
#   - Reviews should be initialized with a customer, restaurant, and a rating (a number)
# - `Review rating()`
#   - returns the rating for a restaurant.
# - `Review all()`
#   - returns all of the reviews

class Review:
    all_reviews = []
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self.rating)
    
    def rating(self):
        return self.rating
    @classmethod
    def all(cls):
        return cls.all_reviews
    
# Review
# - `Review customer()`
#   - returns the customer object for that review
#   - Once a review is created, should not be able to change the customer
# - `Review restaurant()`
#   - returns the restaurant object for that given review
#   - Once a review is created, should not be able to change the restaurant
    def review_customer(self):
        return self._customer
    def review_restaurant(self):
        return self._restaurant


review1 = Review('JAN','MAGGIES',9)
review2 = Review('BIN','PIZZA INN',7)
review3 = Review('KIMUTAI','WESTON',6)

print(review1.rating)
print(review2.rating)
print(review3.rating)

print(Review.all())