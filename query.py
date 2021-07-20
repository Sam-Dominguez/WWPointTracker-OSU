from nutritionfacts import get_database
from getPoints import get_points_from_list
from pymongo import MongoClient
from meal import Meal

db = get_database()

# Access Collection
RESTAURANT = "12TH AVE BREAD CO"

collection: MongoClient = db[RESTAURANT]

meal: Meal = Meal(collection)
items = collection.find()

print(items[0])
