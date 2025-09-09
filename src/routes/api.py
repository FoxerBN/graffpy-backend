from flask import Blueprint, jsonify
from src.services.process_service import get_system_stats
from src.services.weekly_service import generate_weekly_stats
process_api = Blueprint('process', __name__)

@process_api.route("/process", methods=["GET"])
def process():
    stats = get_system_stats()
    return jsonify(stats), 200

@process_api.route("/weekly", methods=["GET"])
def weekly():
    stats = generate_weekly_stats()
    return jsonify(stats), 200