import sys

def calc_scores(data):
    """
    Returns:
        Characters, Players
    """
    players = dict()
    characters = dict()

    for item in data:
        if item["type"] == "tournament" or item["type"] == "game":
            for player_char_combo in item["results"]:
                if player_char_combo["player"] not in players: players[player_char_combo["player"]] = 0
                if player_char_combo["character"] not in characters: characters[player_char_combo["character"]] = 0
                players[player_char_combo["player"]] += player_char_combo["score"]
                characters[player_char_combo["character"]] += player_char_combo["score"]
        else:
            print(f"Error parsing event {item}")
            sys.exit(0)
    return(characters, players)
