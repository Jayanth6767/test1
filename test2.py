import pymongo
client = pymongo.MongoClient("mongodb+srv://jayanth:chillu345@cluster0.pjpanwj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
