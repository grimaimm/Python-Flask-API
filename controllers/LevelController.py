from flask import jsonify, request
from models.LevelModel import Level
from config import db
from flask_jwt_extended import jwt_required


@jwt_required()
def get_all_levels():
    levels = Level.query.all()
    return jsonify([level.to_dict() for level in levels])

@jwt_required()
def get_level_by_id(level_id):
    level = Level.query.get(level_id)
    if not level:
        return jsonify({"status": "error", "message": "Level not found"}), 404
    return jsonify(level.to_dict())

@jwt_required()
def add_level():
    new_level_data = request.get_json()
    new_level = Level(name=new_level_data["name"])
    db.session.add(new_level)
    db.session.commit()
    return (
        jsonify(
            {
                "message": "Level added successfully",
                "level": new_level.to_dict(),
            }
        ),
        201,
    )

@jwt_required()
def update_level(level_id):
    level = Level.query.get(level_id)
    if not level:
        return jsonify({"status": "error", "message": "Level not found"}), 404
    updated_level_data = request.get_json()
    level.name = updated_level_data.get("name", level.name)
    db.session.commit()
    return jsonify({"message": "Level updated successfully", "level": level.to_dict()})

@jwt_required()
def delete_level(level_id):
    level = Level.query.get(level_id)
    if not level:
        return jsonify({"status": "error", "message": "Level not found"}), 404
    db.session.delete(level)
    db.session.commit()
    return jsonify({"message": "Level deleted successfully"})
