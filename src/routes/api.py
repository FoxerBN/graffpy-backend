from flask import Blueprint, jsonify

process_api = Blueprint('process', __name__)

@process_api.route('/process', methods=['GET'])
def process():
    return jsonify({"CPU": "34%"}), 200