def handle(request, client):
    data = request.get_json()
    db = client[data['database']]
    col = db[data['collection']]
    result = list(col.aggregate(data['pipeline']))
    for doc in result:
        if '_id' in doc:
            doc['_id'] = str(doc['_id'])
    return result