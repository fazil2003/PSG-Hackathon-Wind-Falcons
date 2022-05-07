import overpy


def get_shops(data):
    # Initialize the API
    api = overpy.Overpass()

    query = "";
    for i in data:
        print(i[0],i[1])
        # Define the query
        query += "(node(around:100,{lat},{lon}););out;".format(lat=i[0], lon=i[1])
        
    # Call the API
    result = api.query(query)
    print(query)
    return result