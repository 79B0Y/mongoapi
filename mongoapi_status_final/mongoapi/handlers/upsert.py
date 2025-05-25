def handle(request, client):
    data = request.get_json()
    db = client[data['database']]
    col = db[data['collection']]
    result = col.update_one(data['filter'], {'$set': data['update']}, upsert=True)
    return {
        "matched_count": result.matched_count,
        "modified_count": result.modified_count,
        "upserted_id": str(result.upserted_id) if result.upserted_id else None
    }