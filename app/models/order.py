from . import mongo
from bson.objectid import ObjectId
from datetime import datetime

class Order:
    @staticmethod
    def create_order(order_data):
        """Create a new order and insert it into the database."""
        order_data["orderDate"] = datetime.utcnow()  # Ensure the order date is set to now
        result = mongo.db.Order.insert_one(order_data)
        return result.inserted_id

    @staticmethod
    def get_order_by_id(order_id):
        """Fetch an order by its ID."""
        try:
            order_id = ObjectId(order_id)
        except Exception:
            return None
        return mongo.db.Order.find_one({"_id": order_id})

    @staticmethod
    def update_order_status(order_id, status):
        """Update the status of an order."""
        try:
            order_id = ObjectId(order_id)
        except Exception:
            return None
        return mongo.db.Order.update_one({"_id": order_id}, {"$set": {"status": status}})

    @staticmethod
    def get_all_orders():
        """Fetch all orders."""
        orders = mongo.db.Order.find()
        return [
            {**order, "_id": str(order["_id"])} for order in orders
        ]

    @staticmethod
    def get_order_by_id(order_id):
        """Fetch a single order by its ID."""
        try:
            order_id = ObjectId(order_id)
        except Exception:
            return None
        return mongo.db.Order.find_one({"_id": order_id})

    @staticmethod
    def update_order_status(order_id, status):
        """Update the status of an order."""
        try:
            order_id = ObjectId(order_id)
        except Exception:
            return None
        return mongo.db.Order.update_one({"_id": order_id}, {"$set": {"status": status}})

    @staticmethod
    def get_orders_by_customer_id(customer_id):
        """Fetch orders by customer ID."""
        try:
            customer_id = ObjectId(customer_id)
        except Exception:
            print("Invalid customer ID format.")
            return []

        orders = list(mongo.db.Order.find({"customerId": customer_id}))
        if not orders:
            print(f"No orders found for customer ID: {customer_id}")
        return orders

