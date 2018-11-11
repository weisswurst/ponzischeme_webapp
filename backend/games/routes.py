from flask import jsonify, Blueprint, request
from backend.games.gameIO import readGameJSON
from backend.games.gameActions import *



games = Blueprint('games', __name__)


@games.route("/game", methods=['GET'])
def get_game():
    return readGameJSON()
    """
    return jsonify(game_id=1,
                   player1 = "peter")
    """

@games.route("/game/selectTileAndCard", methods=['PUT'])
def selecttileandcard():
    """
       need input parameters:
           selected card (value is unique), tile
           (player, currentPlayer)
    """
    req = request.get_json()
    value = req['value']
    tile = req['tile']
    name = req['name']
    error = selectTileAndCard(value, tile, name)
    if error:
        return error
    else:
        return readGameJSON()
