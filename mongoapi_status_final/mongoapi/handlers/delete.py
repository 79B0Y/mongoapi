def handle(request, client):
    data = request.get_json()
    db = client[data['database']]
    col = db[data['collection']]
    result = col.delete_many(data['filter'])
    return {"deleted_count": result.deleted_count}