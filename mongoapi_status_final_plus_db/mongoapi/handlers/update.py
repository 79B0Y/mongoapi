def handle(request, client):
    data = request.get_json()
    db = client[data['database']]
    col = db[data['collection']]
    result = col.update_many(data['filter'], {'$set': data['update']})
    return {
        "matched_count": result.matched_count,
        "modified_count": result.modified_count
    }