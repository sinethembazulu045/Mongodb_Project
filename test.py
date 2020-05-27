import unittest
from visit_data import myFeildList
from mongo_db import Visitor
import pytest

class Testing_functions(unittest.TestCase):

  def test_create_visitor(self):
      visitor = Visitor(myFeildList)
      assert visitor.create_visitor() == "visitor created"

  def test_visitor_not_created(self):
        visitor = Visitor("data")
        assert visitor.create_visitor() == 'visitor not created'

  def test_delete_visitor(self):
      visitor =Visitor(myFeildList)
      person_to_delete = {"visitor_name":"Skara"}
      assert visitor.delete_visitor(person_to_delete) == "document deleted"
    

  def test_update_visitor(self):
      visitor = Visitor(myFeildList)
      visitor_to_update= {"visitor_name": "Sfiso"} 
      new_info= {"$set": {"gender":"male"}}
      assert visitor.update_visitor(visitor_to_update,new_info) == "visitor updated"

  def test_visitor_not_updated(self):
      visitor = Visitor(myFeildList)
      visitor_to_update = {"visitor_name": "Sfiso"} 
      new_info = {"$set": {"gender":"male"}}
      assert visitor.update_visitor(visitor_to_update,new_info) != "visitor not updated"


if __name__ == '__main__':
    unittest.main()

