from datetime import datetime


def get_today_date():
    return datetime.now().strftime(
        "%d%m%Y%H%M%S"
    )  # 12/05/2022 00:24:02 ficará 12052022002402
