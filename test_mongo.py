from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client.typeform_automation

    # Test insert
    result = db.test.insert_one({"test": "Hello MongoDB!"})
    print(f"✅ Connected! Inserted document with id: {result.inserted_id}")

    # Clean up
    db.test.delete_one({"_id": result.inserted_id})
    print("✅ Cleanup successful!")

except Exception as e:
    print(f"❌ Error: {e}")
