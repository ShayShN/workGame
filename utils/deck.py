import random

def create_card(rank:str,suite:str) -> dict:
    return dict(rank = rank, suite = suite, value = rank)

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    p1 = p1_card.get("value")
    p2 = p2_card.get("value")
    if p1 > p2:
        return "p1"
    if p1 < p2:
        return "p2"
    if p1 == p2:
        return "WAR"
   
          
def create_deck() -> list[dict]:
    rank = [i for i in range(2, 15)]
    suite = [i for i in ("H","C","D","S")]
    arr = []
    
    for r in rank:
        for s in suite:
                arr.append(create_card(r, s))
    return arr


def shuffle(deck:list[dict]) -> list[dict]:
    temp = deck
    while True:
        for i in range(1000):
            index1 = random.randrange(52)
            index2 = random.randrange(52)
            if index1 == index2:
                continue
            else:
                temp[index1], temp[index2] = temp[index2], temp[index1]
        return temp
                   
       




