import pymongo
import getDirection
import pprint

def accessRoute(start, end):
    # spliting the city start and end from given location
    try:
        start = start.split(',')
        start = start[-1]
        end = end.split(',')
        end = end[-1]
    except:
        # leave for future improvement
        pass

    client = pymongo.MongoClient("mongodb+srv://123456:TeamFalcon@cluster0.fibqu.mongodb.net/123456?retryWrites=true&w=majority")
        # create connection to mongodb atlas
    db = client.gettingStarted
    # create cluster called people
    city = db.city

    # find wheather the start and end present in database
    find = city.find_one({"start":start.lower(), "end":end.lower()})
    
    # find fails 
    if not find:

        direction = getDirection.get_direction(start, end)
        city.insert_one(direction)
        find = direction
    # f = open("find.json", 'w')
    # f.write(str(find))
    # f.close()
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(find)
    k=find['features'][0]['geometry']['coordinates']
    # print(k)
    return k
    #return find


