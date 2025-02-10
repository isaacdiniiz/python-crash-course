class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The {self.restaurant_name}'s cuisine type is {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!\n")


restaurant = Restaurant('Bar do Aldo', 'coração de boy')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant('Clube do bolinha', 'Alcool congelador de mentes')
restaurant_3 = Restaurant('Sitio do Shelby', 'Drogas pesadas')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()