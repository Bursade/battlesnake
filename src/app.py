"""
Battlesnake's server.
"""


import logging
import os

from flask import Flask
from flask import request

import logic

app = Flask(__name__)


@app.get("/")
def handle_info():
    """
    This function is called when you register your Battlesnake
    on play.battlesnake.com
    See https://docs.battlesnake.com/guides/
    getting-started#step-4-register-your-battlesnake
    """
    print("INFO")
    return logic.get_info()


@app.post("/start")
def handle_start():
    """
    This function is called everytime your Battlesnake enters a game.
    It's purely for informational purposes, you don't have to make
    any decisions here.
    request.json contains information about the game that's about to be played.
    """
    data = request.get_json()

    print(f"{data['game']['id']} START")
    return "ok"


@app.post("/move")
def handle_move():
    """
    This function is called on every turn and is how your Battlesnake decides
    where to move.
    Valid moves are "up", "down", "left", or "right".
    """
    data = request.get_json()

    move = logic.choose_move(data)

    return {"move": move}


@app.post("/end")
def handle_end():
    """
    This function is called when a game your Battlesnake was in has ended.
    It's purely for informational purposes, you don't have to make
    any decisions here.
    """
    data = request.get_json()

    print(f"{data['game']['id']} END")
    return "ok"


@app.after_request
def identify_server(response):
    """

    """
    response.headers["Server"] = "BattlesnakeOfficial/starter-snake-python"
    return response


if __name__ == "__main__":
    logging.getLogger("werkzeug").setLevel(logging.ERROR)

    HOST = "0.0.0.0"
    PORT = int(os.environ.get("PORT", "8080"))

    print(f"\nRunning Battlesnake server at http://{HOST}:{PORT}")
    app.env = 'development'
    app.run(host=HOST, port=PORT, debug=True)
