from flask import jsonify

def handle(request, client):
    data = request.get_json()
    db_name = data["database"]
    col_name = data.get("collection")

    db = client[db_name]
    created = False

    if col_name:
        col = db[col_name]
        col.insert_one({"init": True})
        col.delete_many({"init": True})
        created = True

    collections = db.list_collection_names()
    return {
        "created": created or bool(collections),
        "database": db_name,
        "collections": collections
    }