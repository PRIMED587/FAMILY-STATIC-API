from flask import Flask, jsonify, request
from flask_cors import CORS
from src.datastructure import FamilyStructure
from src.utils import generate_sitemap

app = Flask(__name__)
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404


@app.route('/members', methods=['POST'])
def add_member():
    member = request.get_json()
    if not member or "first_name" not in member or "age" not in member or "lucky_numbers" not in member:
        return jsonify({"error": "Missing required fields"}), 400
    jackson_family.add_member(member)
    return jsonify(member), 200


@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404