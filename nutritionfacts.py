def get_database():
    from pymongo import MongoClient
    from connection_string import my_connection_string
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = my_connection_string

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    if client:
        print('Database Connected.')
    else:
        print('Database Connection Failed.')
    # Create the database for our example (we will use the same database)
    return client['WWPointTracker-OSU']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database()

