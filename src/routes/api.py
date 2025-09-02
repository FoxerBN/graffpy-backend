from flask import Blueprint, jsonify
from src.services.process_service import get_system_stats
process_api = Blueprint('process', __name__)

@process_api.route("/process", methods=["GET"])
def process():
    stats = get_system_stats()
    return jsonify(stats), 200