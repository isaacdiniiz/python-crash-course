class Restaurant:
    
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The {self.restaurant_name}'s cuisine type is {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!\n")
        
    def numbers_served(self):
        print(f"{self.restaurant_name} served {self.number_served} clients!")
    
    def set_numbers_served(self, clients):
        self.number_served = clients
        
    def increment_numbers_served(self, new_clients):
        self.number_served += new_clients
        


restaurant = Restaurant('Bar do Aldo', 'coração de boi')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.numbers_served()

restaurant.set_numbers_served(27)
restaurant.numbers_served()

restaurant.increment_numbers_served(10)
restaurant.numbers_served()