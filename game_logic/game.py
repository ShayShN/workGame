import utils.deck as f

def create_player(name:str = "AI") -> dict:
    thisdict = dict(player = name, hand = [], won_pile = [])
    return thisdict


def init_game()->dict:
    p1 = create_player("shay")
    p2 = create_player()
    newdeck = f.create_deck()
    f.shuffle(newdeck)
    p1["hand"] = newdeck[:,26]
    p2["hand"] = newdeck[26,:]
    game_dict = dict(deck = newdeck, player_1 = p1, player_2 = p2)
    return game_dict
    
    
    
    

def play_round(p1:dict,p2:dict):
    player1 = p1["hand"][0]
    player2 = p2["hand"][0]
    checking = f.compare_cards(player1, player2)
    if checking == "p1":
        p1["won_pile"].append(player1)
        p1["won_pile"].append(player2)
    elif checking == "p2":
        p2["won_pile"].append(player1)
        p2["won_pile"].append(player2)
    else:
        return
    return p1, p2
        