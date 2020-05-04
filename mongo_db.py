import datetime
import pymongo
from pymongo import MongoClient
from mongoengine import *

#establishing a connection 

client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://root:pass@localhost:27017')
connect('mongoengine_UmuziProspects', host='localhost', port=27017)

#Accessing database
db = client['UmuziProspects'] #creating database named "UmuziProspects"
my_collectection = db['Visitor'] #creating collection inside database "UmuziProspect"

myFeildList = [
  {"visitor_name": "Sfiso", "visitors_age": 28, "date of visit": "2020-11-3","time of visit": "11:00 am", "assistance_name": "Sindisiw", "comments": "She knew her job"},
  {"visitor_name": "Nkosikhona", "visitors_age": 32, "date of visit": "2020-18-6", "time of visit": "13:00 pm", "assistance_name": "Fanakhe", "comments": "She was open, someone who is easy to talk to"},
  {"visitor_name": "Skara", "visitors_age": 36, "date of visit": "2020-14-5", "time of visit": "14:00 pm","assistance_name": "Mazethi","comments": "Helful"},
]

        ###### fucnctionality functions


#Saving a visitor into UmuziProspects database

def create_visitor(*args): 
  result = my_collectection.insert_many(myFeildList)
  return result

#print(create_visitor(my_collectection))

# Deletting one document

def delete_Visitor(*args): # this function only deletes one document where Visitor_name is "Skara"
  myquery = { "Visitor_name": "Skara" }
  my_collectection.delete_one(myquery)
  for result in mycol.find():
    return result

# Deletting  all documents in Visitor

def delete_all(*args): # this function Deletes all documents in the "Visitor" collection
  result = my_collectection.delete_many({})
  return result.deleted_count, " documents deleted."

#Updating one collection function

def update_Visitor(*args): 
    my_query = { "visitor_name": "Sfiso"}
    new_values = { "$set": { "vistor_name": "Philani" } }
    my_collectection.update_one(my_query, new_values)
    for result in my_collectection.find(): # print "Visitors" after the update
         return result

#Updating many collection



