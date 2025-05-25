def handle(request, client):
    data = request.get_json()
    db = client[data['database']]
    col = db[data['collection']]
    result = col.insert_one(data['document'])
    return {"inserted_id": str(result.inserted_id)}