from factory.database import Database
from factory.validation import Validator
from bson import ObjectId


class Task(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()

        self.collection_name = 'task'  # collection name

        self.fields = {
            "taskName": "string",
            "owner": "string"
        }
        self.create_required_fields = ["taskName","owner"]
        self.create_optional_fields = []

        self.update_required_fields = ["taskName"]
        self.update_optional_fields = []


    def create(self, user):
        # Validator will throw error if invalid
        self.validator.validate(user, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(user, self.collection_name)
        return "Inserted Id " + res

    def find(self, user):  # find all
        return self.db.find(user, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)    
    def update(self, id, user):
        self.validator.validate(user, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, user,self.collection_name)   
    def delete(self, id):
        return self.db.delete(id, self.collection_name)


        
