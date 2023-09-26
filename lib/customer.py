# Customer
# - `Customer __init__()`
#   - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
# - `Customer given_name()`
#   - returns the customer's given name
#   - should be able to change after the customer is created
# - `Customer family_name()`
#   - returns the customer's family name
#   - should be able to change after the customer is created
# - `Customer full_name()`
#   - returns the full name of the customer, with the given name and the family name concatenated, Western style.
# - `Customer all()`
#   - returns **all** of the customer instances
from review import Review
class Customer():
    customers = []
    def __init__(self,given_name,family_name):
        if type(self.given_name)== str:
            self.given_name = given_name
        if type(self.family_name):
            self.family_name = family_name
        Customer.customers.append(given_name)
        self.review =[]

    def given_name(self):
        return self.given_name
    def family_name(self):
        return self.family_name
    def full_name(self):
        return (f'{self.given_name} {self.family_name}')
    @classmethod
    def all(cls):
        return [customer for customer in cls.customers]
    
    def restaurants(self):
        reviews = set()
        for key,value in Review.all_reviews_1.items():
            if value[0] == self._restaurant_name:
                reviews.append(value[2])
        return list(reviews)
    def add_review(self,restaurant,rating,customer):
        new_review=Review(self, restaurant, rating,customer)
        return new_review
    
        


    