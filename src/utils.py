from datetime import datetime


def get_timestamp() -> str:
    times = [datetime.year, datetime.month, datetime.day,
             datetime.hour, datetime.minute, datetime.second]
    return "-".join(times)
