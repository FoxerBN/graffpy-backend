from flask import Blueprint, jsonify
from src.services.process_service import get_system_stats
from src.services.seven_days_data import get_seven_days_data
process_api = Blueprint('process', __name__)

@process_api.route("/process", methods=["GET"])
def process():
    stats = get_system_stats()
    return jsonify(stats), 200

@process_api.route("/weekly", methods=["GET"])
def weekly():
    stats = get_seven_days_data()
    return jsonify(stats), 200