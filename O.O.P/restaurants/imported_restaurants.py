from restaurants import Restaurant

restaurant1 = Restaurant("rest1", "chinese")
print restaurant1.restaurant_name.title(), restaurant1.cuisine_type.title()
restaurant1.describe()
restaurant1.open()

restaurant2 = Restaurant("rest2", "japanese")
restaurant2.describe()
restaurant2.open()

restaurant3 = Restaurant("rest3", "italian")
restaurant3.describe()
restaurant3.open()
