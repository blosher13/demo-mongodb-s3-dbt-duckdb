import os
from dotenv import load_dotenv
from pymongo import MongoClient, server_api

from data_creation import (
    schools,
    students,
    staff,
    incidents,
    medications,
    care_plans,
)

load_dotenv()

uri = os.getenv("MONGODB_URI")
DATABASE_NAME = "bb_cdw_demo"  # <-- change to whatever you want the DB called

client = MongoClient(
    uri,
    server_api=server_api.ServerApi(version="1", strict=True, deprecation_errors=True),
)

try:

    client.admin.command("ping")
    print("Connected successfully")

    db = client[DATABASE_NAME]

    collections = {
        "schools": schools,
        "students": students,
        "staff": staff,
        "incidents": incidents,
        "medications": medications,
        "care_plans": care_plans,
    }

    for collection_name, records in collections.items():

        if not records:
            print(f"Skipping '{collection_name}' — no records to insert")
            continue

        result = db[collection_name].insert_many(records)
        print(f"Inserted {len(result.inserted_ids)} documents into '{collection_name}'")

    client.close()

except Exception as e:
    raise Exception("The following error occurred: ", e)