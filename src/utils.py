from datetime import datetime


def get_timestamp() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d-%H-%M-%S")
