import datetime
import pymongo
from pymongo import MongoClient
from mongoengine import *
import os
from os import environ
from visit_data import myFeildList

MONGO_HOST = os.getenv("host")

#establishing a connection
client = MongoClient(MONGO_HOST, 27017)
client = MongoClient('mongodb://root:pass@localhost:27017')
connect('mongoengine_UmuziProspects', MONGO_HOST, port=27017)

#Accessing database
db = client['UmuziProspects'] #creating database named "UmuziProspects"
my_collectection = db['Visitor'] #creating collection inside database "UmuziProspect"

 #fucnctionality class with its functions

class Visitor():
    
    def __init__(self, visit_data):
        self.visit_data = visit_data

    def create_visitor(self): #Saving a visitor into UmuziProspects database
      try:
        create_visitor = my_collectection.insert_many(self.visit_data)  #inserting multiple records 
      except TypeError:
        return "visitor not created"
      return "visitor created"
      
    def delete_visitor(self,person_to_delete): # this function only deletes one document where Visitor_name is "Skara"
      try:
        delete_visitor = my_collectection.delete_one(person_to_delete)
      except TypeError:
        return "document not deleted"
      return "document deleted"
      
  # Deletting  all documents in Visitor

  
    def delete_many(self): # this function only deletes many document 
      try:
        delete_many = my_collectection.delete_many(self.visit_data)
      except TypeError:
        return "documents not deleted"
      return "all document deleted"
      

  # # #Updating one collection function

    def update_visitor(self,visitor_to_update, new_info): 
      try:
        update_visitor = my_collectection.update_one(visitor_to_update, new_info)
      except TypeError:
        return "visitor not updated"
      return "visitor updated"
  #   #print(delete_Visitor(person_to_update,new_info))

    def display_all_info(self):
      for my_data in my_collectection.find():
        return my_data



#print(show_all_info(my_collectection))
# visitor_one = Visitor()
# print(visitor_one.create_visitor())
# visitor_two =Visitor(myFeildList)
# person_to_delete = {"visitor_name": "Skara"}
# print(visitor_two.delete_Visitor(person_to_delete))
visitor = Visitor(myFeildList)
print(visitor.display_all_info())