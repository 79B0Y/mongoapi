from flask import Flask, request, jsonify
from pymongo import MongoClient
from .config_loader import load_config
from .handlers import insert, find, update, delete, upsert, aggregate, create_database
import logging

config = load_config()
logging_enabled = config.get("logging", {}).get("enabled", False)

if logging_enabled:
    logging.basicConfig(
        filename=config["logging"].get("file", "mongoapi.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def get_status(client):
    try:
        db_names = client.list_database_names()
        structure = {db: client[db].list_collection_names() for db in db_names}
        return {
            "service_name": "mongoapi",
            "connected": True,
            "uri": config["mongodb"]["uri"],
            "databases": structure
        }
    except Exception as e:
        return {
            "service_name": "mongoapi",
            "connected": False,
            "uri": config["mongodb"]["uri"],
            "error": str(e)
        }

def run():
    client = MongoClient(config["mongodb"]["uri"])
    app = Flask(__name__)

    if logging_enabled:
        logging.info("MongoDB connected to %s", config["mongodb"]["uri"])
        try:
            dbs = client.list_database_names()
            logging.info("Initial database list: %s", dbs)
        except Exception as e:
            logging.error("Error getting database list: %s", e)

    @app.route('/status', methods=['GET'])
    def status_route():
        return jsonify(get_status(client))

    @app.route('/create_database', methods=['POST'])
    def create_database_route():
        return jsonify(create_database.handle(request, client))

    @app.route('/insert', methods=['POST'])
    def insert_route():
        result = insert.handle(request, client)
        if logging_enabled:
            logging.info("Insert operation executed.")
        return jsonify(result)

    @app.route('/find', methods=['POST'])
    def find_route(): return jsonify(find.handle(request, client))

    @app.route('/update', methods=['POST'])
    def update_route(): return jsonify(update.handle(request, client))

    @app.route('/delete', methods=['POST'])
    def delete_route(): return jsonify(delete.handle(request, client))

    @app.route('/upsert', methods=['POST'])
    def upsert_route(): return jsonify(upsert.handle(request, client))

    @app.route('/aggregate', methods=['POST'])
    def aggregate_route(): return jsonify(aggregate.handle(request, client))

    app.run(host=config["server"]["host"], port=config["server"]["port"])