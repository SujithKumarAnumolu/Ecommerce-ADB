from . import mongo
from bson.objectid import ObjectId

class Customer:
    @staticmethod
    def get_customer_by_email(email):
        """Fetch a customer by email."""
        return mongo.db.Customer.find_one({"email": email})

    @staticmethod
    def create_customer(customer_data):
        """Insert a new customer into the database."""
        return mongo.db.Customer.insert_one(customer_data)

    @staticmethod
    def get_customer_by_id(customer_id):
        """Fetch a customer by ID."""
        try:
            customer_id = ObjectId(customer_id)
        except Exception:
            return None
        return mongo.db.Customer.find_one({"_id": customer_id})