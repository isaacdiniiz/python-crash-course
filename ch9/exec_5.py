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
 

class IceCreamStand(Restaurant):
    
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("These are the flavors currently available\n")
        for flavor in self.flavors:
            print(f"- {flavor}")


icecream = IceCreamStand('Sorveteria do Aldo', 'Sorvetes', ['chocolate', 'baunilha'])

icecream.describe_restaurant()
icecream.open_restaurant()
icecream.show_flavors()