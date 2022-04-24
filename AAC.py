from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient
        self.client = MongoClient('mongodb://%s:%s@localhost:54763/?authSource=AAC' % (username, password))
        self.database = self.client['AAC']
        
    # Implementing the C(reate) in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
            
    # Implementing the R(ead) in CRUD
    def read(self, query=None):
        if query is not None:
            result = list(self.database.animals.find(query, {"_id": False})) # query should be dictionary (key: "value")
            return result           
        else:
            raise Exception("Nothin to search, because query is empty")
            return False
    
    # Implementing Read All method
    def read_all(self, data):
        if data == None:
            raise Exception("Entries can not be found")
        else:
            cursor = self.database.animals.find(data,{'_id':False})
            return cursor
            
    # Implementing the U(pdate) in CRUD
    def update(self, data, updateOperation):
        if data is not None and updateOperation is not None:
            result = self.database.animals.update_one(data, updateOperation) # data should be dictinary (key: "value"), updateOperation shoud be dictionary that includes the operation (example: $set)
            if result.matched_count == result.modified_count:
                return {"updatedSuccessfully":"true"}
            else:
                raise Exception("No matching object to update")
        else:
            raise Exception("Nothing to update, because data parameter is empty")
    
    # Implementing the D(elete) in CRUD
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data) # data should be dictinary (key: "value")
            if result.deleted_count == 1:
                return {"deletedSuccessfully":"true"}
            else:
                raise Exception("No matching object to delete")
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            