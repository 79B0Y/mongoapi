def handle(request, client):
    data = request.get_json()
    db = client[data['database']]
    col = db[data['collection']]
    result = list(col.find(data.get('query', {}), data.get('projection')))
    for doc in result:
        doc['_id'] = str(doc['_id'])
    return result