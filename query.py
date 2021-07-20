from nutritionfacts import get_database
from getPoints import getPoints

db = get_database()

# Access Collection
RESTAURANT = "12TH AVE BREAD CO"

collection_name = db[RESTAURANT]

items = collection_name.find()
# loop through food items for that restautant collection
for item in items:
    # if that item has points stored, get value
    points = item.get('points')

    # else query website for point total and store result in db
    if not points:
        points = getPoints(item['calories'], item['sugar'], item['saturatedFat'], item['protein'])
        collection_name.update_one({"_id": item["_id"]}, {"$set": {"points": points}})

    print(item['name'], points, "Points")