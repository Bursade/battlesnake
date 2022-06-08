import random
from typing import List, Dict

"""
Battlesnake's logic and helper functions.
"""

def get_info() -> dict:
    """
    This controls your Battlesnake appearance and author permissions.
    For customization options, see https://docs.battlesnake.com/references/personalization

    TIP: If you open your Battlesnake URL in browser you should see this data.
    """
    return {
        "apiversion": "1",
        "author": "unknown",
        "color": "#0066ff",
        "head": "beluga",
        "tail": "bolt",
    }


def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_snake = data["you"]      # A dictionary describing your snake's position on the board
    my_head = my_snake["head"]  # A dictionary of coordinates like {"x": 0, "y": 0}
    my_body = my_snake["body"]  # A list of coordinate dictionaries like [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}]
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'
    board = data['board']
    max_height = board['height'] - 1 # The maximum possible value for the "x" coordinate
    max_width = board['width'] - 1 # The maximum possible value for the "y" coordinate

    # Uncomment the lines below to see what this data looks like in your output!
    print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    print(f"All board data this turn: {data}")
    print(f"My Battlesnake this turn is: {my_snake}")
    print(f"My Battlesnakes head this turn is: {my_head}")
    print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    # Step 0: Don't allow your Battlesnake to move back on it's own neck.
    possible_moves = _avoid_my_neck(my_head, my_neck, possible_moves)

    # Step 1 - Don't hit walls.
    possible_moves = _avoid_the_walls(board_height, board_width, my_head, possible_moves)

    # TODO: Step 2 - Don't hit yourself.
    # Use information from `my_body` to avoid moves that would collide with yourself.

    # TODO: Step 3 - Don't collide with others.
    # Use information from `data` to prevent your Battlesnake from colliding with others.

    # TODO: Step 4 - Find food.
    # Use information in `data` to seek out and find food.
    # food = data['board']['food']

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = random.choice(possible_moves)
    # TODO: Explore new strategies for picking a move that are better than random

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move


def _avoid_my_neck(my_head: dict, my_neck: dict, possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates for the head of my Battlesnake.
            e.g. {"x": 3, "y": 5}
    my_neck: Dictionary of x/y coordinates for the neck of my Battlesnake.
            e.g. {"x": 3, "y": 4}
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        if "left" in possible_moves: possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        if "right" in possible_moves: possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        if "down" in possible_moves: possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        if "up" in possible_moves: possible_moves.remove("up")

    return possible_moves

def _avoid_the_walls(board_height: int, board_width: int, my_head: dict, possible_moves: List[str]) -> List[str]:
    """
    board_height: An integer number representing the height of the board. This will be the lenght of the "y" axis.
            e.g 11
    board_width: An integer number representing the width of the board. This will be the lenght of the "x" axis.
            e.g 5         
    my_head: Dictionary of x/y coordinates for the head of my Battlesnake.
            e.g. {"x": 3, "y": 5}
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]    
    """
    
    if my_head["x"] == max_width:  # my head is on the right side of the board
        if "right" in possible_moves: possible_moves.remove("right")
    elif my_head["x"] == 0:  # my head is on the left side of the board
        if "left" in possible_moves: possible_moves.remove("left") 
    
    if my_head["y"] == max_height:  # my head is on the top of the board
        if "up" in possible_moves: possible_moves.remove("up")
    elif my_head["y"] == 0:  # my head is on the bottom of the board
        if "down" in possible_moves: possible_moves.remove("down")

    return possible_moves
