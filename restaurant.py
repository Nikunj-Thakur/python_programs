class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        #self.status = "Open"

    def describe_restaurant(self):
        print(f"The name of restaurant is {self.name}")
        print(f"This restauranrt offers {self.cuisine} cuisine")

    def open_restaurant(self, status):
        self.status=status
        print(f"The restaurant {self.name} is currently {self.status}\n")


restuarant0=Restaurant("Aroma","Indian")
print(restuarant0.name + " " + restuarant0.cuisine)
restuarant0.describe_restaurant()
restuarant0.open_restaurant("Closed")

restaurant1=Restaurant("Nepalses-Chef","Nepalese")
print(restaurant1.name + " " + restaurant1.cuisine)
restaurant1.describe_restaurant()
restaurant1.open_restaurant("Open")

restaurant2=Restaurant("Micro-Brewery","English")
print(restaurant2.name + " " + restaurant2.cuisine)
restaurant2.describe_restaurant()
restaurant2.open_restaurant("Mon-Fri")