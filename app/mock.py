import random
from datetime import datetime

USERS = ["anthony", "nina", "joe"]
ACTIONS = [("GOOD", 1), ("BAD", -1)]


def format_date(date: datetime) -> str:
    return date.strftime("%d-%m-%Y %H:%M:%S")


def new_message() -> dict:
    action = random.choice(ACTIONS)
    return {
        "player_id": random.choice(USERS),
        "action": action[0],
        "score": random.randrange(0, 100) * action[1],
        "timestamp": format_date(datetime.utcnow()),
    }
