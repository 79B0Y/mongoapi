def handle(request, client):
    try:
        data = request.get_json()
        db_name = data['database']
        collection_name = data.get('collection')

        db = client[db_name]

        if collection_name:
            col = db[collection_name]
            col.insert_one({"init": True})  # 触发创建数据库和集合
            collections = db.list_collection_names()
            return {
                "created": True,
                "database": db_name,
                "collections": collections
            }
        else:
            # 创建一个临时集合再删除它，确保数据库创建
            tmp_col = db["__init__"]
            tmp_col.insert_one({"_": 1})
            db.drop_collection("__init__")
            return {
                "created": True,
                "database": db_name,
                "collections": db.list_collection_names()
            }

    except Exception as e:
        return {
            "error": str(e),
            "created": False
        }
