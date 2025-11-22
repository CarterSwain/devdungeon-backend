from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__)

# Temporary data
players = []
regions = [
    {"id": 1, "name": "Beginner’s Hall", "difficulty": 1},
    {"id": 2, "name": "Middleware Marsh", "difficulty": 2},
]


@bp.route("/players", methods=["GET"])
def list_players():
    return jsonify(players)


@bp.route("/players", methods=["POST"])
def create_player():
    data = request.get_json()
    player = {
        "id": len(players) + 1,
        "username": data.get("username"),
        "level": 1,
        "xp": 0,
    }
    players.append(player)
    return jsonify(player), 201


@bp.route("/regions", methods=["GET"])
def list_regions():
    return jsonify(regions)
