from datetime import datetime


def get_today_date():
    return datetime.now().strftime("%d%m%Y%H%M%S")
