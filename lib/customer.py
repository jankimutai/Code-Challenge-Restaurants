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
class Customer():
    customers = []
    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(given_name)

    def given_name(self):
        return self.given_name
    def family_name(self):
        return self.family_name
    def full_name(self):
        return (f'{self.given_name} {self.family_name}')
    @classmethod
    def all(cls):
        return [customer for customer in cls.customers]
customer1 = Customer('JAN','KIMUTAI')
customer2 = Customer('ALVIN','OMBITO')
customer3 = Customer('DAN','NJOKA')
print(Customer.all())
   
    